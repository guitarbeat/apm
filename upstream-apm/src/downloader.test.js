
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { downloadAndExtract } from './downloader.js';
import { EventEmitter } from 'events';

// Mock fs
vi.mock('fs', () => {
  return {
    createWriteStream: vi.fn(() => {
      const emitter = new EventEmitter();
      return emitter;
    }),
    unlink: vi.fn((path, cb) => cb && cb(null))
  };
});

// Mock mocks for adm-zip
const mockExtractAllTo = vi.fn();
const mockExtractAllToAsync = vi.fn((dest, overwrite, cb) => cb && cb(null));

vi.mock('adm-zip', () => {
  return {
    default: class AdmZip {
      constructor() {}
      extractAllTo = mockExtractAllTo;
      extractAllToAsync = mockExtractAllToAsync;
    }
  };
});

// Mock axios
vi.mock('axios', () => {
  const mockGet = vi.fn((url) => {
     return Promise.resolve({
        data: {
          tag_name: 'v1.0.0',
          assets: [
            {
              name: 'apm-cursor.zip',
              browser_download_url: 'http://example.com/apm-cursor.zip',
              size: 1024
            }
          ]
        }
      });
  });

  const mockRequest = vi.fn((config) => {
     return Promise.resolve({
         data: {
          pipe: (writer) => {
            process.nextTick(() => writer.emit('finish'));
            return writer;
          }
        }
      });
  });

  return {
    default: Object.assign(mockRequest, { get: mockGet })
  };
});

describe('downloader', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should use extractAllToAsync for non-blocking extraction', async () => {
    await downloadAndExtract('v1.0.0', 'Cursor', '/tmp/dest');

    // Currently, the code uses extractAllTo (sync), so this test expects the CHANGE
    // Failing initially proves we are targeting the right thing.

    // We expect the optimized code to call extractAllToAsync
    // And NOT call extractAllTo

    // For now, let's verify what IS called to confirm baseline.
    // expect(mockExtractAllTo).toHaveBeenCalled();

    // But since I am Bolt, I am writing the test for the OPTIMIZED behavior.
    expect(mockExtractAllToAsync).toHaveBeenCalled();
    expect(mockExtractAllTo).not.toHaveBeenCalled();
  });
});
