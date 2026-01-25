import { describe, it, expect } from 'vitest';
import { getMemoryRootContent, getImplementationPlanContent } from './utils.js';

describe('utils', () => {
  describe('getMemoryRootContent', () => {
    it('should return a non-empty string', () => {
      const content = getMemoryRootContent();
      expect(content).toBeDefined();
      expect(typeof content).toBe('string');
      expect(content.length).toBeGreaterThan(0);
    });

    it('should contain key sections', () => {
      const content = getMemoryRootContent();
      expect(content).toContain('# 🧠 Project Memory Root');
      expect(content).toContain('## 📂 Structure');
      expect(content).toContain('## 🚀 Usage');
    });
  });

  describe('getImplementationPlanContent', () => {
    it('should return a non-empty string', () => {
      const content = getImplementationPlanContent();
      expect(content).toBeDefined();
      expect(typeof content).toBe('string');
      expect(content.length).toBeGreaterThan(0);
    });

    it('should contain key sections', () => {
      const content = getImplementationPlanContent();
      expect(content).toContain('# 📋 Implementation Plan');
      expect(content).toContain('## 🏗️ Active Task');
      expect(content).toContain('## 📝 Backlog');
    });
  });
});
