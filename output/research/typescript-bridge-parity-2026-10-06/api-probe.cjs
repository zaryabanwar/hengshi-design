const path = require('node:path');
const fs = require('node:fs');
const {createRequire} = require('node:module');
const candidate = path.resolve(process.argv[2]);
const root = __dirname;
const candidateRequire = createRequire(path.join(candidate, 'package.json'));
const ts = candidateRequire('typescript');
const oracle = JSON.parse(fs.readFileSync(path.join(root, 'fixture-oracles.json'), 'utf8'));
const project = diagnostics => diagnostics.map(d => {
  const pos = d.file && d.start !== undefined ? d.file.getLineAndCharacterOfPosition(d.start) : null;
  return {code: d.code, category: d.category,
    file: d.file ? path.relative(root, d.file.fileName).replaceAll('\\', '/') : null,
    line: pos ? pos.line + 1 : null, column: pos ? pos.character + 1 : null,
    message: ts.flattenDiagnosticMessageText(d.messageText, '\n')};
});
const results = oracle.fixtures.map(({name}) => {
  const config = path.join(root, name, 'tsconfig.json');
  const read = ts.readConfigFile(config, ts.sys.readFile);
  const parsed = ts.parseJsonConfigFileContent(read.config, ts.sys, path.dirname(config));
  const program = ts.createProgram(parsed.fileNames, parsed.options);
  const compiler = project([...parsed.errors, ...ts.getPreEmitDiagnostics(program)]);
  const host = {
    getCompilationSettings: () => parsed.options,
    getScriptFileNames: () => parsed.fileNames,
    getScriptVersion: () => '1',
    getScriptSnapshot: file => {
      const text = ts.sys.readFile(file);
      return text === undefined ? undefined : ts.ScriptSnapshot.fromString(text);
    },
    getCurrentDirectory: () => path.dirname(config),
    getDefaultLibFileName: options => ts.getDefaultLibFilePath(options),
    fileExists: ts.sys.fileExists, readFile: ts.sys.readFile,
    readDirectory: ts.sys.readDirectory, directoryExists: ts.sys.directoryExists,
    getDirectories: ts.sys.getDirectories
  };
  const service = ts.createLanguageService(host);
  const languageService = project(parsed.fileNames.flatMap(file => [
    ...service.getSyntacticDiagnostics(file), ...service.getSemanticDiagnostics(file)
  ]));
  service.dispose();
  return {name, compiler, languageService};
});
process.stdout.write(JSON.stringify({
  version: ts.version,
  resolvedEntry: candidateRequire.resolve('typescript'),
  delegatedEntry: candidateRequire.resolve('@typescript/old'),
  scope: 'TypeScript 6 API and in-process language service only; no native/editor LSP or build parity claim',
  results
}, null, 2) + '\n');
