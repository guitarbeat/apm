import chalk from 'chalk';

export class Spinner {
  constructor() {
    this.timer = null;
    this.frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'];
    this.currentFrame = 0;
    this.text = '';
    this.isSpinning = false;

    // Bind cleanup to ensure it can be removed
    this.cleanup = this.cleanup.bind(this);
  }

  start(text = '') {
    if (this.isSpinning) {
      this.update(text);
      return this;
    }

    this.text = text;
    this.isSpinning = true;

    // If not TTY, just log the text and return
    if (!process.stdout.isTTY) {
      console.log(chalk.cyan(`[wait] ${text}`));
      return this;
    }

    // Hide cursor
    process.stdout.write('\x1B[?25l');

    // Register cleanup on process exit/interrupt
    process.on('exit', this.cleanup);
    process.on('SIGINT', this.cleanup);
    process.on('SIGTERM', this.cleanup);

    this.render();
    this.timer = setInterval(() => {
      this.currentFrame = (this.currentFrame + 1) % this.frames.length;
      this.render();
    }, 80);

    return this;
  }

  render() {
    if (!process.stdout.isTTY) return;

    const frame = this.frames[this.currentFrame];
    // Clear current line and write
    process.stdout.write(`\r\x1B[K${chalk.cyan(frame)} ${this.text}`);
  }

  cleanup() {
    if (process.stdout.isTTY) {
      process.stdout.write('\x1B[?25h'); // Show cursor
    }
    if (this.timer) {
      clearInterval(this.timer);
      this.timer = null;
    }
  }

  stop(text = '', symbol = '✓') {
    if (!this.isSpinning) return this;

    this.isSpinning = false;

    if (this.timer) {
      clearInterval(this.timer);
      this.timer = null;
    }

    // Remove event listeners
    process.removeListener('exit', this.cleanup);
    process.removeListener('SIGINT', this.cleanup);
    process.removeListener('SIGTERM', this.cleanup);

    if (!process.stdout.isTTY) {
      if (text) console.log(chalk.green(`[done] ${text}`));
      return this;
    }

    // Clear line and print final message
    process.stdout.write('\r\x1B[K'); // Clear line
    if (text) {
      const symbolColored = symbol === '✓' ? chalk.green(symbol) :
                            symbol === '✖' ? chalk.red(symbol) :
                            symbol === '!' ? chalk.yellow(symbol) : symbol;
      console.log(`${symbolColored} ${text}`);
    }

    // Show cursor
    process.stdout.write('\x1B[?25h');
    return this;
  }

  fail(text = '') {
    return this.stop(text, '✖');
  }

  succeed(text = '') {
    return this.stop(text, '✓');
  }

  warn(text = '') {
    return this.stop(text, '!');
  }

  update(text) {
    this.text = text;
    if (!this.isSpinning) this.render();
    return this;
  }
}
