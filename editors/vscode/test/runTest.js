'use strict';
const path = require('path');
const fs = require('fs');
const os = require('os');
const { runTests } = require('@vscode/test-electron');

function findCode() {
  const p = process.argv[2] || process.env.HZ_VSCODE_EXE;
  return p && fs.existsSync(p) ? p : undefined;
}

(async () => {
  for (const k of Object.keys(process.env)) if (k === 'ELECTRON_RUN_AS_NODE' || k.startsWith('VSCODE_')) delete process.env[k];
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'hz-vscode-profile-'));
  const results = path.join(tmp, 'resultados.json');
  process.env.HZ_TEST_RESULTS = results;
  let code = 0;
  try {
    await runTests({
      vscodeExecutablePath: findCode(),
      version: process.env.HZ_VSCODE_VERSION || 'insiders',
      extensionDevelopmentPath: path.join(__dirname, '..'),
      extensionTestsPath: path.join(__dirname, 'suite', 'index.js'),
      launchArgs: ['--user-data-dir', path.join(tmp, 'datos'), '--extensions-dir', path.join(tmp, 'ext'), '--disable-workspace-trust', '--skip-welcome', '--skip-release-notes'],
      extensionTestsEnv: { HZ_TEST_RESULTS: results, HYPEREZ_NO_WELCOME: '1' },
    });
  } catch (e) {
    console.error('Las pruebas de integración fallaron:', e.message || e);
    code = 1;
  }
  if (fs.existsSync(results)) {
    for (const r of JSON.parse(fs.readFileSync(results, 'utf8'))) console.log((r.ok ? '✓ ' : '✗ ') + r.name + (r.detail ? '  — ' + r.detail : ''));
  }
  process.exit(code);
})();
