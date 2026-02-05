import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { displaySuccess, displayError } from './utils.js';

describe('Utils', () => {
  let consoleLogSpy;
  let consoleErrorSpy;

  beforeEach(() => {
    consoleLogSpy = vi.spyOn(console, 'log').mockImplementation(() => {});
    consoleErrorSpy = vi.spyOn(console, 'error').mockImplementation(() => {});
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe('displaySuccess', () => {
    it('should display success message', () => {
      displaySuccess('Operation successful');
      expect(consoleLogSpy).toHaveBeenCalled();
    });
  });

  describe('displayError', () => {
    it('should be exported', () => {
      expect(displayError).toBeDefined();
    });

    it('should display error message using console.error', () => {
       if (displayError) {
          displayError('Operation failed');
          expect(consoleErrorSpy).toHaveBeenCalled();
          expect(consoleLogSpy).not.toHaveBeenCalled();
       }
    });

    it('should include details in error output', () => {
       if (displayError) {
          displayError('Failed', 'Some detailed error');
          // Since console.error is called multiple times with styled strings,
          // we check if any of the calls contained the string.
          const calls = consoleErrorSpy.mock.calls.flat();
          const hasDetails = calls.some(arg => typeof arg === 'string' && arg.includes('Some detailed error'));
          expect(hasDetails).toBe(true);
       }
    });
  });
});
