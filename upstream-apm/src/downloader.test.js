import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { downloadAndExtract } from './downloader.js';
import axios from 'axios';
import fs from 'fs';
import path from 'path';
import os from 'os';
import { PassThrough } from 'stream';
import AdmZip from 'adm-zip';

vi.mock('axios');
vi.mock('adm-zip');

describe('downloadAndExtract', () => {
  let tempDir;

  beforeEach(() => {
    vi.resetAllMocks();
    tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'apm-test-'));
  });

  afterEach(() => {
      fs.rmSync(tempDir, { recursive: true, force: true });
  });

  it('should show progress bar when content-length is present', async () => {
    AdmZip.mockImplementation(() => ({
      extractAllTo: vi.fn(),
    }));

    const mockDataStream = new PassThrough();
    const mockDownloadResponse = {
      headers: { 'content-length': '100' },
      data: mockDataStream,
    };

    const mockReleaseData = {
        tag_name: 'v1.0.0',
        assets: [
            { name: 'apm-cursor.zip', size: 100, browser_download_url: 'http://example.com/apm-cursor.zip' }
        ]
    };

    axios.mockImplementation(() => Promise.resolve(mockDownloadResponse));
    axios.get = vi.fn().mockResolvedValue({ data: mockReleaseData });

    const stdoutSpy = vi.spyOn(process.stdout, 'write').mockImplementation(() => true);

    const promise = downloadAndExtract('v1.0.0', 'Cursor', tempDir);

    // Wait for setup
    await new Promise(r => setTimeout(r, 50));

    mockDataStream.write(Buffer.alloc(50));
    await new Promise(r => setTimeout(r, 50));

    mockDataStream.write(Buffer.alloc(50));
    await new Promise(r => setTimeout(r, 50));

    mockDataStream.end();

    await promise;

    const calls = stdoutSpy.mock.calls.map(c => c[0]);
    const output = calls.join('');

    expect(output).toContain('50%');
    expect(output).toContain('100%');
    expect(stdoutSpy).toHaveBeenCalledWith('\n');
  });
});
