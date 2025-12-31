import chalk from 'chalk';

export class Spinner {
  constructor(text = '') {
    this.text = text;
    this.frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'];
    this.interval = 80;
    this.timer = null;
    this.frameIndex = 0;
    this.isSpinning = false;

    // Bind handleSignal to this instance
    this.handleSignal = this.handleSignal.bind(this);
  }

  start(text) {
    if (text) this.text = text;
    this.isSpinning = true;

    // Check if TTY
    if (process.stdout.isTTY) {
      process.stdout.write('\x1B[?25l'); // Hide cursor
      this.timer = setInterval(() => {
        this.render();
      }, this.interval);

      // Handle signals to ensure cursor is restored
      process.on('SIGINT', this.handleSignal);
      process.on('SIGTERM', this.handleSignal);
    } else {
      console.log(this.text);
    }
    return this;
  }

  render() {
    const frame = this.frames[this.frameIndex];
    this.frameIndex = (this.frameIndex + 1) % this.frames.length;
    process.stdout.write(`\r${chalk.cyan(frame)} ${this.text}`);
    // Clear the rest of the line to remove artifacts from longer text
    process.stdout.write('\x1B[K');
  }

  stop() {
    if (this.isSpinning) {
      this.isSpinning = false;
      clearInterval(this.timer);
      if (process.stdout.isTTY) {
        process.stdout.write('\r'); // Return to start
        process.stdout.clearLine(0); // Clear line
        process.stdout.write('\x1B[?25h'); // Show cursor

        // Remove signal listeners
        process.removeListener('SIGINT', this.handleSignal);
        process.removeListener('SIGTERM', this.handleSignal);
      }
    }
    return this;
  }

  succeed(text) {
    this.stop();
    console.log(`${chalk.green('✔')} ${text || this.text}`);
    return this;
  }

  fail(text) {
    this.stop();
    console.log(`${chalk.red('✖')} ${text || this.text}`);
    return this;
  }

  info(text) {
    this.stop();
    console.log(`${chalk.blue('ℹ')} ${text || this.text}`);
    return this;
  }

  warn(text) {
    this.stop();
    console.log(`${chalk.yellow('⚠')} ${text || this.text}`);
    return this;
  }

  handleSignal() {
    this.stop();
    process.exit(0);
  }
}
