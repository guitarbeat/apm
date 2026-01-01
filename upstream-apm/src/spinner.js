import chalk from 'chalk';

export class Spinner {
  constructor(text = '') {
    this.text = text;
    this.interval = null;
    this.frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'];
    this.currentFrame = 0;
    this.isSpinning = false;

    // Ensure cursor is restored on process exit or signal
    this.restoreCursor = () => process.stdout.write('\u001B[?25h');
    process.on('exit', this.restoreCursor);
    process.on('SIGINT', () => {
      this.restoreCursor();
      process.exit();
    });
  }

  start(text) {
    if (text) this.text = text;
    this.isSpinning = true;
    this.currentFrame = 0;

    // Hide cursor
    process.stdout.write('\u001B[?25l');

    this.interval = setInterval(() => {
      this.render();
      this.currentFrame = (this.currentFrame + 1) % this.frames.length;
    }, 80);

    return this;
  }

  render() {
    if (!this.isSpinning) return;

    // Clear line and print frame + text
    process.stdout.write(`\r\x1b[K${chalk.cyan(this.frames[this.currentFrame])} ${this.text}`);
  }

  stop() {
    if (!this.isSpinning) return;

    clearInterval(this.interval);
    this.isSpinning = false;
    this.interval = null;

    // clear line
    process.stdout.write('\r\x1b[K');

    // Show cursor
    this.restoreCursor();

    return this;
  }

  succeed(text) {
    this.stop();
    if (text) this.text = text;
    console.log(`${chalk.green('✔')} ${this.text}`);
    return this;
  }

  fail(text) {
    this.stop();
    if (text) this.text = text;
    console.log(`${chalk.red('✖')} ${this.text}`);
    return this;
  }

  info(text) {
    this.stop();
    if (text) this.text = text;
    console.log(`${chalk.blue('ℹ')} ${this.text}`);
    return this;
  }
}
