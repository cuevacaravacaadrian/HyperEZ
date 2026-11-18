'use strict';
const path = require('path');
require('esbuild').buildSync({
  entryPoints: [path.join(__dirname, '..', 'extension.js')],
  outfile: path.join(__dirname, '..', 'dist', 'extension.js'),
  bundle: true,
  platform: 'node',
  format: 'cjs',
  target: 'node18',
  external: ['vscode'],
  minify: true,
  sourcemap: false,
  logLevel: 'warning',
});
console.log('dist/extension.js listo');
