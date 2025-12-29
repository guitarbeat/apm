import chalk from 'chalk';

export class Spinner {
  constructor() {
    this.interval = null;
    this.frameIndex = 0;
    this.frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'];
    this.message = '';
    this.isSpinning = false;
    this.isTTY = process.stdout.isTTY && !process.env.CI; // Disable in CI as well

    if (this.isTTY) {
      // Ensure cursor is restored on exit
      const restoreCursor = () => {
        if (this.isSpinning) {
          this.stop();
        }
        process.stdout.write('\x1B[?25h');
      };

      process.on('SIGINT', () => {
        restoreCursor();
        process.exit(0);
      });

      process.on('SIGTERM', () => {
        restoreCursor();
        process.exit(0);
      });

      // Also handle normal exit just in case
      process.on('exit', () => {
        if (this.isSpinning) {
            process.stdout.write('\x1B[?25h');
        }
      });
    }
  }

  start(message) {
    if (this.isSpinning) {
      this.stop();
    }
    this.message = message;
    this.isSpinning = true;

    if (this.isTTY) {
      process.stdout.write('\x1B[?25l'); // Hide cursor
      this.render();
      this.interval = setInterval(() => {
        this.frameIndex = (this.frameIndex + 1) % this.frames.length;
        this.render();
      }, 80);
    } else {
      console.log(`${chalk.cyan('i')} ${message}...`);
    }
  }

  render() {
    if (!this.isSpinning || !this.isTTY) return;
    process.stdout.write(`\r${chalk.cyan(this.frames[this.frameIndex])} ${this.message}`);
  }

  stop(message = '', type = 'success') {
    if (!this.isSpinning) return;

    if (this.isTTY) {
      clearInterval(this.interval);
      process.stdout.write('\x1B[?25h'); // Show cursor
      process.stdout.write('\r\x1B[K'); // Clear line
    }

    this.isSpinning = false;

    if (message) {
      let icon = '';
      switch (type) {
        case 'success':
          icon = chalk.green('✔');
          break;
        case 'error':
          icon = chalk.red('✖');
          break;
        case 'warn':
          icon = chalk.yellow('⚠');
          break;
        case 'info':
          icon = chalk.blue('ℹ');
          break;
      }
      console.log(`${icon} ${message}`);
    }
  }

  succeed(message) {
    this.stop(message, 'success');
  }

  fail(message) {
    this.stop(message, 'error');
  }

  warn(message) {
    this.stop(message, 'warn');
  }

  info(message) {
    this.stop(message, 'info');
  }
}

export const spinner = new Spinner();
