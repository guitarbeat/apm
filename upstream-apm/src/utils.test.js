import { describe, it, expect, vi, afterEach } from 'vitest';
import { displaySuccess } from './utils.js';
import chalk from 'chalk';

describe('displaySuccess', () => {
  const consoleLogSpy = vi.spyOn(console, 'log').mockImplementation(() => {});

  afterEach(() => {
    consoleLogSpy.mockClear();
  });

  it('should display success message correctly', () => {
    displaySuccess('Operation successful');
    expect(consoleLogSpy).toHaveBeenCalledWith(expect.stringContaining('✔ Operation successful'));
  });

  it('should display info lines', () => {
    displaySuccess('Done', ['Info 1', 'Info 2']);
    expect(consoleLogSpy).toHaveBeenCalledWith(expect.stringContaining('Info 1'));
    expect(consoleLogSpy).toHaveBeenCalledWith(expect.stringContaining('Info 2'));
  });

  it('should display next steps with correct styling', () => {
    displaySuccess('Done', [], ['Step 1']);
    expect(consoleLogSpy).toHaveBeenCalledWith(expect.stringContaining('Next steps:'));
    expect(consoleLogSpy).toHaveBeenCalledWith(expect.stringContaining('Step 1'));
  });
});
