import chalk from 'chalk';

export class Spinner {
  constructor(message = '') {
    this.message = message;
    this.timer = null;
    this.frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'];
    this.i = 0;
    this.isSpinning = false;
  }

  start(msg) {
    if (msg) this.message = msg;
    this.isSpinning = true;

    if (!process.stdout.isTTY) {
      console.log(chalk.cyan('ℹ'), this.message);
      return this;
    }

    process.stdout.write('\u001B[?25l'); // Hide cursor
    this.timer = setInterval(() => {
      // Clear line (\r\u001B[K) before writing frame
      process.stdout.write(`\r\u001B[K${chalk.cyan(this.frames[this.i++ % this.frames.length])} ${this.message}`);
    }, 80);
    return this;
  }

  stop(symbol, msg) {
    this.isSpinning = false;
    if (this.timer) {
      clearInterval(this.timer);
      this.timer = null;
      process.stdout.write('\r\u001B[K'); // Clear line
      process.stdout.write('\u001B[?25h'); // Show cursor
    }
    console.log(`${symbol} ${msg || this.message}`);
    return this;
  }

  succeed(msg) { return this.stop(chalk.green('✔'), msg); }
  fail(msg) { return this.stop(chalk.red('✖'), msg); }

  set message(msg) {
    this._msg = msg;
    if (this.isSpinning && !process.stdout.isTTY && msg) console.log(chalk.cyan('ℹ'), msg);
  }
  get message() { return this._msg; }
}
