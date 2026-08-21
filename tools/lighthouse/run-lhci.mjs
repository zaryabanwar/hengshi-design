import { existsSync, mkdirSync } from 'node:fs'
import { spawnSync } from 'node:child_process'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..', '..')
const tempDir = resolve(repoRoot, '.lighthouseci', 'tmp')
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
const lhciCli = resolve(repoRoot, 'node_modules', '@lhci', 'cli', 'src', 'cli.js')
const node22Path = process.env.NVM_HOME
  ? resolve(process.env.NVM_HOME, 'v22.15.0', 'node.exe')
  : ''
const node22Dir = node22Path ? dirname(node22Path) : ''
const currentNodeMajor = Number.parseInt(process.versions.node.split('.')[0] ?? '0', 10)
const nodeBinary =
  process.platform === 'win32' && currentNodeMajor > 22 && existsSync(node22Path)
    ? node22Path
    : process.execPath

mkdirSync(tempDir, { recursive: true })

const env = {
  ...process.env,
  TEMP: tempDir,
  TMP: tempDir,
  TMPDIR: tempDir,
  CHROME_PATH: process.env.CHROME_PATH || chromePath
}

if (nodeBinary === node22Path && node22Dir) {
  const pathKey = Object.keys(env).find((key) => key.toLowerCase() === 'path') ?? 'PATH'
  env[pathKey] = `${node22Dir};${env[pathKey] ?? ''}`
}

const result = spawnSync(nodeBinary, [lhciCli, 'autorun'], {
  cwd: repoRoot,
  env,
  stdio: 'inherit'
})

process.exit(result.status ?? 1)
