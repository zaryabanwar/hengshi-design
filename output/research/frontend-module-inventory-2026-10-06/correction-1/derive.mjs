import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

// Correct one unsupported classification by reading retained output metadata.
// No build, package execution, install, browser operation or network request.
const here = path.dirname(fileURLToPath(import.meta.url));
const original = path.dirname(here);
const hash = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const observationBytes = await fs.readFile(path.join(original, 'observation.json'));
const inventoryBytes = await fs.readFile(path.join(original, 'output-module-inventory.json'));
const graphBytes = await fs.readFile(path.join(original, 'module-graph.json'));
const observation = JSON.parse(observationBytes);
const inventory = JSON.parse(inventoryBytes);
const graph = JSON.parse(graphBytes);
if (Object.keys(observation).filter(k => k === 'externalGraphModules').length !== 1)
  throw new Error('Expected original unsupported classification field');
const missingFlag = graph.flatMap(x => x.graph).filter(x => !Object.hasOwn(x, 'isExternal')).length;
if (missingFlag !== observation.graphModuleCount)
  throw new Error('Original graph field-presence observation changed');
const references = inventory.map(chunk => {
  if (!Array.isArray(chunk.imports) || !Array.isArray(chunk.dynamicImports))
    throw new Error('Actual output reference arrays missing');
  return { fileName: chunk.fileName, imports: chunk.imports, dynamicImports: chunk.dynamicImports };
});
delete observation.externalGraphModules;
observation.inputGraphExternalClassification = 'UNPROVEN: original collector read unsupported ModuleInfo.isExternal; serialized records omit it.';
observation.outputChunkReferences = references;
observation.correction = {
  number: 1, atUtc: new Date().toISOString(), rebuilt: false,
  originalObservationSha256: hash(observationBytes),
  originalOutputInventorySha256: hash(inventoryBytes), originalGraphSha256: hash(graphBytes),
  graphRecordsMissingUnsupportedFlag: missingFlag,
  scope: 'Empty returned chunk import/reference arrays only; not all runtime fetches, module classification or deployed external resources.'
};
await fs.writeFile(path.join(here, 'observation.corrected.json'), JSON.stringify(observation, null, 2) + '\n', { flag: 'wx' });
console.log(JSON.stringify({ corrected: true, graphRecordsMissingUnsupportedFlag: missingFlag,
  outputChunkReferences: references, rebuilt: false }, null, 2));
