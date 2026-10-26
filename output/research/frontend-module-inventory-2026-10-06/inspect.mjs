import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath, pathToFileURL } from 'node:url';

// Observational research only. No install, vendor patch, application build or browser execution.
const evidence = path.dirname(fileURLToPath(import.meta.url));
const repo = path.resolve(evidence, '../../..');
const candidate = path.join(repo, 'output/research/frontend-three-remedy-evaluation-2026-10-06/candidate');
const workspace = path.join(evidence, 'workspace');
const digest = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const relative = name => path.relative(repo, name).replaceAll('\\', '/');
const writeJson = (name, value) => fs.writeFile(path.join(evidence, name), JSON.stringify(value, null, 2) + '\n');
const finiteInputs = ['index.html', 'package.json', 'package-lock.json', 'vite.config.mjs',
  'tsconfig.json', 'tsconfig.invalid.json', 'tsconfig.loader-control.json',
  'src/fixture.tsx', 'src/fixture.css', 'src/invalid-control.tsx', 'src/loader-declaration-control.ts'];
const sourceFiles = ['node_modules/vite/package.json', 'node_modules/vite/dist/node/index.d.ts',
  'node_modules/vite/dist/node/chunks/node.js', 'node_modules/rolldown/package.json',
  'node_modules/rolldown/dist/shared/define-config-kIZKjX8Q.d.mts',
  'node_modules/gensync/package.json', 'node_modules/gensync/index.js'];
async function fileIdentity(name) {
  const bytes = await fs.readFile(name);
  return { path: relative(name), bytes: bytes.length, sha256: digest(bytes) };
}
async function walkFiles(directory) {
  const result = [];
  for (const item of await fs.readdir(directory, { withFileTypes: true })) {
    const name = path.join(directory, item.name);
    if (item.isDirectory()) result.push(...await walkFiles(name));
    else if (item.isFile()) result.push(name);
    else throw new Error('Unexpected non-regular fixture output member');
  }
  return result.sort();
}
const originalOutputs = await walkFiles(path.join(candidate, 'fixture-dist'));
const protectedNames = [...finiteInputs, ...sourceFiles].map(p => path.join(candidate, p)).concat(originalOutputs);
const before = await Promise.all(protectedNames.map(fileIdentity));
await writeJson('protected-before.json', before);
await fs.mkdir(workspace); // Fail instead of overwriting an earlier run.
for (const name of finiteInputs) {
  const destination = path.join(workspace, name);
  await fs.mkdir(path.dirname(destination), { recursive: true });
  await fs.copyFile(path.join(candidate, name), destination);
}
await fs.mkdir(path.join(workspace, 'node_modules'));
const junctions = [];
for (const item of await fs.readdir(path.join(candidate, 'node_modules'), { withFileTypes: true })) {
  if (item.name.startsWith('.')) continue;
  const source = path.join(candidate, 'node_modules', item.name);
  const destination = path.join(workspace, 'node_modules', item.name);
  if (item.name.startsWith('@') && item.isDirectory()) {
    await fs.mkdir(destination);
    for (const child of await fs.readdir(source, { withFileTypes: true })) {
      if (!child.isDirectory()) continue;
      const target = path.join(source, child.name);
      const link = path.join(destination, child.name);
      await fs.symlink(target, link, 'junction');
      junctions.push({ link: relative(link), target: relative(target) });
    }
  } else if (item.isDirectory()) {
    await fs.symlink(source, destination, 'junction');
    junctions.push({ link: relative(destination), target: relative(source) });
  }
}
await writeJson('junctions.json', junctions);
const captured = [];
const observer = {
  name: 'hsd-research-module-inventory', enforce: 'post', apply: 'build',
  generateBundle: {
    order: 'post',
    handler(_options, bundle, isWrite) {
      const graph = [...this.getModuleIds()].sort().map(id => {
        const info = this.getModuleInfo(id);
        if (!info) throw new Error('Module disappeared from graph');
        return { id, isEntry: info.isEntry, isExternal: info.isExternal,
          importedIds: info.importedIds, dynamicallyImportedIds: info.dynamicallyImportedIds,
          importers: info.importers, dynamicImporters: info.dynamicImporters };
      });
      captured.push({ isWrite, graph, chunkIds: Object.values(bundle)
        .filter(item => item.type === 'chunk').map(item => ({ fileName: item.fileName,
          moduleIds: [...item.moduleIds], moduleKeys: Object.keys(item.modules) })) });
    }
  }
};
const start = new Date().toISOString();
try {
  const { build } = await import(pathToFileURL(path.join(candidate, 'node_modules/vite/dist/node/index.js')).href);
  const built = await build({ root: workspace, configFile: path.join(workspace, 'vite.config.mjs'),
    plugins: [observer], build: { write: false, outDir: 'observed-not-written-dist' } });
  const results = Array.isArray(built) ? built : [built];
  const inventory = [];
  const packageOwners = new Map();
  async function owner(id) {
    // Preserve raw IDs. Virtual modules are not guessed to belong to packages.
    if (id.includes('\0')) return { kind: 'virtual', package: null };
    const plain = id.split('?')[0];
    if (!path.isAbsolute(plain)) return { kind: 'non-file', package: null };
    let directory = path.dirname(plain);
    while (true) {
      const manifest = path.join(directory, 'package.json');
      try {
        const bytes = await fs.readFile(manifest);
        const json = JSON.parse(bytes);
        if (json.name && json.version) {
          const key = relative(manifest);
          const record = { path: key, name: json.name, version: json.version,
            declaredLicense: json.license ?? null, sha256: digest(bytes) };
          packageOwners.set(key, record);
          return { kind: 'named-manifest', package: key };
        }
      } catch (error) { if (error.code !== 'ENOENT') throw error; }
      const parent = path.dirname(directory);
      if (parent === directory) return { kind: 'unowned-file', package: null };
      directory = parent;
    }
  }
  const artifacts = [];
  for (let index = 0; index < results.length; index++) {
    for (const item of results[index].output) {
      const bytes = item.type === 'chunk' ? Buffer.from(item.code) :
        typeof item.source === 'string' ? Buffer.from(item.source) : Buffer.from(item.source);
      const target = path.resolve(evidence, 'generated-artifacts', item.fileName);
      const outputRoot = path.resolve(evidence, 'generated-artifacts') + path.sep;
      if (!target.startsWith(outputRoot)) throw new Error('Unsafe generated artifact name');
      await fs.mkdir(path.dirname(target), { recursive: true });
      await fs.writeFile(target, bytes, { flag: 'wx' });
      const original = path.join(candidate, 'fixture-dist', item.fileName);
      let sameOriginal = false;
      try { sameOriginal = bytes.equals(await fs.readFile(original)); }
      catch (error) { if (error.code !== 'ENOENT') throw error; }
      artifacts.push({ result: index, type: item.type, fileName: item.fileName,
        bytes: bytes.length, sha256: digest(bytes), matchesOriginalBytes: sameOriginal });
      if (item.type === 'chunk') {
        const modules = [];
        for (const [id, details] of Object.entries(item.modules)) modules.push({ id,
          ...await owner(id), renderedLength: details.renderedLength,
          renderedExports: details.renderedExports,
          renderedCodeSha256: details.code === null ? null : digest(Buffer.from(details.code)) });
        inventory.push({ fileName: item.fileName, isEntry: item.isEntry,
          isDynamicEntry: item.isDynamicEntry, facadeModuleId: item.facadeModuleId,
          imports: item.imports, dynamicImports: item.dynamicImports,
          moduleIds: [...item.moduleIds], modules });
      }
    }
  }
  const matchesGensync = id => /(?:^|[\\/])gensync(?:[\\/]|$)/.test(id);
  const graphIds = captured.flatMap(x => x.graph.map(x => x.id));
  const chunkIds = inventory.flatMap(x => x.moduleIds);
  const moduleKeys = inventory.flatMap(x => x.modules.map(x => x.id));
  const inventoryAgrees = inventory.every(x =>
    JSON.stringify([...x.moduleIds].sort()) === JSON.stringify(x.modules.map(x => x.id).sort()));
  const after = await Promise.all(protectedNames.map(fileIdentity));
  await writeJson('protected-after.json', after);
  await writeJson('module-graph.json', captured);
  await writeJson('output-module-inventory.json', inventory);
  await writeJson('output-package-manifests.json', [...packageOwners.values()].sort((a,b) => a.path.localeCompare(b.path)));
  const observation = { startedAt: start, endedAt: new Date().toISOString(),
    node: process.version, vite: JSON.parse(await fs.readFile(path.join(candidate, 'node_modules/vite/package.json'))).version,
    rolldown: JSON.parse(await fs.readFile(path.join(candidate, 'node_modules/rolldown/package.json'))).version,
    scope: 'Exact synthetic client fixture, existing matched Three184 candidate; not the application or deployed graph.',
    buildWrite: false, capturedGenerateCalls: captured.length, observedWriteFlags: captured.map(x => x.isWrite),
    graphModuleCount: new Set(graphIds).size, outputModuleCount: new Set(chunkIds).size,
    outputManifestCount: packageOwners.size, chunkModuleIdsAgreeWithModuleKeys: inventoryAgrees,
    gensyncGraphMatches: graphIds.filter(matchesGensync), gensyncChunkMatches: chunkIds.filter(matchesGensync),
    gensyncModuleKeyMatches: moduleKeys.filter(matchesGensync),
    externalGraphModules: captured.flatMap(x => x.graph.filter(x => x.isExternal)), artifacts,
    allProtectedInputsUnchanged: JSON.stringify(before) === JSON.stringify(after),
    configuredOutDirExists: await fs.stat(path.join(workspace, 'observed-not-written-dist')).then(() => true, error => {
      if (error.code === 'ENOENT') return false; throw error;
    }),
    limits: ['Module ownership is nearest named manifest, not legal authorship or complete licence clearance.',
      'Bundler module metadata does not inventory opaque embedded code, binaries or other builds/targets.',
      'No universal gensync build-host/deployed exclusion, D072 conformance or D069 stack selection.',
      'Artifact equality binds this observation to previous exact-byte fixture browser evidence only.'] };
  await writeJson('observation.json', observation);
  if (!observation.allProtectedInputsUnchanged || !inventoryAgrees || captured.length !== 1 ||
      observation.configuredOutDirExists || captured.some(x => x.isWrite) ||
      artifacts.length !== originalOutputs.length || artifacts.some(x => !x.matchesOriginalBytes))
    throw new Error('Observation scope/integrity/equality guard failed; retain all records');
  console.log(JSON.stringify(observation, null, 2));
} catch (error) {
  await writeJson('error.json', { endedAt: new Date().toISOString(), message: error.message, stack: error.stack });
  throw error;
}
