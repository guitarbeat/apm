import chalk from 'chalk';

const frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'];

export class Spinner {
  constructor(text = '') {
    this.text = text;
    this.interval = null;
    this.frameIndex = 0;
    this.isSpinning = false;

    // Ensure cursor is restored on exit
    this._handleExit = this._handleExit.bind(this);
    process.on('SIGINT', this._handleExit);
    process.on('exit', this._handleExit);
  }

  start(text) {
    if (text) this.text = text;
    if (this.isSpinning) return this;

    this.isSpinning = true;
    process.stdout.write('\x1B[?25l'); // Hide cursor

    this.interval = setInterval(() => {
      const frame = frames[this.frameIndex];
      this.frameIndex = (this.frameIndex + 1) % frames.length;
      process.stdout.write(`\r${chalk.cyan(frame)} ${this.text}`);
    }, 80);

    return this;
  }

  stop() {
    if (!this.isSpinning) return this;

    clearInterval(this.interval);
    this.interval = null;
    this.isSpinning = false;
    process.stdout.write('\r\x1B[K'); // Clear line
    process.stdout.write('\x1B[?25h'); // Show cursor
    return this;
  }

  succeed(text) {
    this.stop();
    const message = text || this.text;
    console.log(`${chalk.green('✔')} ${message}`);
    return this;
  }

  fail(text) {
    this.stop();
    const message = text || this.text;
    console.log(`${chalk.red('✖')} ${message}`);
    return this;
  }

  update(text) {
    if (text) this.text = text;
    return this;
  }

  _handleExit() {
    if (this.isSpinning) {
      this.stop();
    }
  }
}
