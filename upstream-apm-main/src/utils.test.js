import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { detectLikelyAssistant } from './utils.js';
import { existsSync, mkdirSync, rmSync, mkdtempSync } from 'fs';
import { join } from 'path';
import { tmpdir } from 'os';

describe('detectLikelyAssistant', () => {
  let tempDir;

  beforeEach(() => {
    // Create a safe temp directory
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
