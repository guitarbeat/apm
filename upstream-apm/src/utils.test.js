import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { displaySuccess } from './utils.js';
import chalk from 'chalk';

describe('displaySuccess', () => {
  let consoleSpy;

  beforeEach(() => {
    consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {});
  });

  afterEach(() => {
    consoleSpy.mockRestore();
  });

  it('should display title correctly', () => {
    displaySuccess('Task Complete');

    const calls = consoleSpy.mock.calls.flat().join('\n');
    expect(calls).toContain('Task Complete');
  });

  it('should display info key-value pairs', () => {
    displaySuccess('Done', { 'Version': '1.0.0' });

    const calls = consoleSpy.mock.calls.flat().join('\n');
    expect(calls).toContain('Version:');
    expect(calls).toContain('1.0.0');
  });

  it('should display next steps with numbering', () => {
    displaySuccess('Done', {}, ['Step 1', 'Step 2']);

    const calls = consoleSpy.mock.calls.flat().join('\n');
    expect(calls).toContain('Next steps:');
    expect(calls).toContain('1.');
    expect(calls).toContain('Step 1');
    expect(calls).toContain('2.');
    expect(calls).toContain('Step 2');
  });
});
