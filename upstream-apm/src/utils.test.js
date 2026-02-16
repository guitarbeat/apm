import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { detectLikelyAssistant, displayError, displaySuccess } from './utils.js';
import { existsSync, mkdirSync, rmSync, mkdtempSync } from 'fs';
import { join } from 'path';
import { tmpdir } from 'os';

describe('Utils', () => {
  describe('detectLikelyAssistant', () => {
    let tempDir;

    // Create a safe temp directory
    beforeEach(() => {
      tempDir = mkdtempSync(join(tmpdir(), 'apm-test-'));
    });

    afterEach(() => {
      if (existsSync(tempDir)) {
        rmSync(tempDir, { recursive: true, force: true });
      }
    });

    it('should return null when no indicators found', () => {
      expect(detectLikelyAssistant(tempDir)).toBe(null);
    });

    it('should detect Cursor', () => {
      mkdirSync(join(tempDir, '.cursor'));
      expect(detectLikelyAssistant(tempDir)).toBe('Cursor');
    });

    it('should detect Windsurf', () => {
      mkdirSync(join(tempDir, '.windsurf'));
      expect(detectLikelyAssistant(tempDir)).toBe('Windsurf');
    });

    it('should detect Roo Code', () => {
      mkdirSync(join(tempDir, '.roo'));
      expect(detectLikelyAssistant(tempDir)).toBe('Roo Code');
    });

    it('should detect Claude Code', () => {
      mkdirSync(join(tempDir, '.claude'));
      expect(detectLikelyAssistant(tempDir)).toBe('Claude Code');
    });
  });

  describe('displaySuccess', () => {
    let consoleLogSpy;

    beforeEach(() => {
      consoleLogSpy = vi.spyOn(console, 'log').mockImplementation(() => {});
    });

    afterEach(() => {
      vi.restoreAllMocks();
    });

    it('should display success message', () => {
      displaySuccess('Operation successful');
      expect(consoleLogSpy).toHaveBeenCalled();
    });
  });

  describe('displayError', () => {
    let consoleErrorSpy;

    beforeEach(() => {
      vi.spyOn(console, 'log').mockImplementation(() => {});
      consoleErrorSpy = vi.spyOn(console, 'error').mockImplementation(() => {});
    });

    afterEach(() => {
      vi.restoreAllMocks();
    });

    it('should be exported', () => {
      expect(displayError).toBeDefined();
    });

    it('should display error message using console.error', () => {
      if (displayError) {
        displayError('Operation failed');
        expect(consoleErrorSpy).toHaveBeenCalled();
        // displayError uses console.error, so console.log might not be called,
        // or at least error should be called.
      }
    });

    it('should include details in error output', () => {
      if (displayError) {
        displayError('Failed', 'Some detailed error');
        // Since console.error is called multiple times with styled strings,
        // we check if any of the calls contained the string.
        const calls = consoleErrorSpy.mock.calls.flat();
        const hasDetails = calls.some(
          (arg) => typeof arg === 'string' && arg.includes('Some detailed error')
        );
        expect(hasDetails).toBe(true);
      }
    });
  });
});
