import { Spinner } from '../src/spinner.js';
import { describe, it, expect, vi, afterEach } from 'vitest';
import chalk from 'chalk';

describe('Spinner', () => {
  afterEach(() => {
    vi.restoreAllMocks();
  });

  it('should initialize with default values', () => {
    const spinner = new Spinner();
    expect(spinner.message).toBe('');
    expect(spinner.isSpinning).toBe(false);
  });

  it('should start spinning and write to stdout', () => {
    const writeSpy = vi.spyOn(process.stdout, 'write').mockImplementation(() => true);
    // Mock isTTY to true
    process.stdout.isTTY = true;

    const spinner = new Spinner('Loading...');
    spinner.start();

    expect(spinner.isSpinning).toBe(true);
    // Should hide cursor
    expect(writeSpy).toHaveBeenCalledWith('\u001B[?25l');

    spinner.stop('✔', 'Done');
  });

  it('should not write if not TTY', () => {
    const writeSpy = vi.spyOn(process.stdout, 'write').mockImplementation(() => true);
    const logSpy = vi.spyOn(console, 'log').mockImplementation(() => {});
    // Mock isTTY to false
    process.stdout.isTTY = false;

    const spinner = new Spinner('Loading...');
    spinner.start();

    expect(spinner.isSpinning).toBe(true);
    // Should NOT write to stdout (except for console.log fallback in stop)
    expect(writeSpy).not.toHaveBeenCalled();
    expect(logSpy).toHaveBeenCalledWith(expect.stringContaining('ℹ'), 'Loading...');

    spinner.stop('✔', 'Done');
  });

  it('should update message', () => {
    const spinner = new Spinner('Initial');
    expect(spinner.message).toBe('Initial');

    spinner.start('Updated');
    expect(spinner.message).toBe('Updated');
    spinner.stop('x', 'bye');
  });

  it('should handle succeed', () => {
    const writeSpy = vi.spyOn(process.stdout, 'write').mockImplementation(() => true);
    const logSpy = vi.spyOn(console, 'log').mockImplementation(() => {});
    process.stdout.isTTY = true;

    const spinner = new Spinner('Working');
    spinner.start();
    spinner.succeed('Success!');

    expect(spinner.isSpinning).toBe(false);
    expect(logSpy).toHaveBeenCalledWith(expect.stringContaining('Success!'));
  });

  it('should handle fail', () => {
    const writeSpy = vi.spyOn(process.stdout, 'write').mockImplementation(() => true);
    const logSpy = vi.spyOn(console, 'log').mockImplementation(() => {});
    process.stdout.isTTY = true;

    const spinner = new Spinner('Working');
    spinner.start();
    spinner.fail('Failed!');

    expect(spinner.isSpinning).toBe(false);
    expect(logSpy).toHaveBeenCalledWith(expect.stringContaining('Failed!'));
  });
});
