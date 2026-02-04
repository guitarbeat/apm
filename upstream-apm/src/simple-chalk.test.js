import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';

describe('simple-chalk', () => {
  beforeEach(() => {
    vi.resetModules();
  });

  afterEach(() => {
    vi.unstubAllGlobals();
  });

  it('should format colors when TTY is present', async () => {
    vi.stubGlobal('process', {
        ...process,
        stdout: { isTTY: true },
        env: {}
    });
    // Re-import to trigger top-level TTY check
    const chalk = (await import('./simple-chalk.js?t=1')).default;
    expect(chalk.red('foo')).toBe('\x1b[31mfoo\x1b[39m');
  });

  it('should NOT format colors when TTY is missing', async () => {
    vi.stubGlobal('process', {
        ...process,
        stdout: { isTTY: undefined },
        env: {}
    });
    const chalk = (await import('./simple-chalk.js?t=2')).default;
    expect(chalk.red('foo')).toBe('foo');
  });

  it('should NOT format colors when NO_COLOR is set', async () => {
    vi.stubGlobal('process', {
        ...process,
        stdout: { isTTY: true },
        env: { NO_COLOR: '1' }
    });
    const chalk = (await import('./simple-chalk.js?t=3')).default;
    expect(chalk.red('foo')).toBe('foo');
  });

  it('should handle multiple arguments', async () => {
    vi.stubGlobal('process', {
        ...process,
        stdout: { isTTY: true },
        env: {}
    });
    const chalk = (await import('./simple-chalk.js?t=4')).default;
    expect(chalk.red('foo', 'bar')).toBe('\x1b[31mfoo bar\x1b[39m');
  });

  it('should stringify null/undefined', async () => {
    vi.stubGlobal('process', {
        ...process,
        stdout: { isTTY: true },
        env: {}
    });
    const chalk = (await import('./simple-chalk.js?t=5')).default;
    expect(chalk.red(null)).toBe('\x1b[31mnull\x1b[39m');
    expect(chalk.red(undefined)).toBe('\x1b[31mundefined\x1b[39m');
  });

  it('should format nested properties correctly', async () => {
    vi.stubGlobal('process', {
        ...process,
        stdout: { isTTY: true },
        env: {}
    });
    const chalk = (await import('./simple-chalk.js?t=6')).default;
    expect(chalk.cyan.bold('foo')).toBe('\x1b[36m\x1b[1mfoo\x1b[22m\x1b[39m');
  });
});
