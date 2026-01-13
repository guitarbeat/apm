import chalk from 'chalk';

export class Spinner {
  constructor(text = '') {
    this.text = text;
    this.interval = null;
    this.frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'];
    this.currentFrame = 0;
    this.isSpinning = false;
  }

  start(text) {
    if (text) this.text = text;
    if (this.isSpinning) return this;

    // If not TTY, just log the text once and return
    if (!process.stdout.isTTY) {
      console.log(this.text);
      return this;
    }

    this.isSpinning = true;
    process.stdout.write('\x1B[?25l'); // Hide cursor

    // Restore cursor on exit
    if (!Spinner.isCursorHandlerAttached) {
      const restoreCursor = () => process.stdout.write('\x1B[?25h');
      // Use exit code 1 to indicate interruption/failure
      process.on('SIGINT', () => { restoreCursor(); process.exit(1); });
      process.on('SIGTERM', () => { restoreCursor(); process.exit(1); });
      Spinner.isCursorHandlerAttached = true;
    }

    this.interval = setInterval(() => {
      this.render();
      this.currentFrame = (this.currentFrame + 1) % this.frames.length;
    }, 80);

    return this;
  }

  render() {
    // Clear current line
    process.stdout.write('\r\x1B[K');

    // Write frame + text
    const frame = chalk.cyan(this.frames[this.currentFrame]);
    process.stdout.write(`${frame} ${this.text}`);
  }

  stop() {
    if (!this.isSpinning) return;

    clearInterval(this.interval);
    this.isSpinning = false;
    process.stdout.write('\r\x1B[K'); // Clear line
    process.stdout.write('\x1B[?25h'); // Show cursor
  }

  succeed(text) {
    this.stop();
    const symbol = chalk.green('✔');
    console.log(`${symbol} ${text || this.text}`);
  }

  fail(text) {
    this.stop();
    const symbol = chalk.red('✖');
    console.log(`${symbol} ${text || this.text}`);
  }

  info(text) {
    this.stop();
    const symbol = chalk.blue('ℹ');
    console.log(`${symbol} ${text || this.text}`);
  }
}
