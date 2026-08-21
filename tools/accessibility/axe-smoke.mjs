import { spawnSync } from 'node:child_process'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..', '..')

const result =
  process.platform === 'win32'
    ? spawnSync('cmd.exe', ['/d', '/s', '/c', 'npm --prefix apps/web run qa:axe'], {
        cwd: repoRoot,
        stdio: 'inherit'
      })
    : spawnSync('npm', ['--prefix', 'apps/web', 'run', 'qa:axe'], {
        cwd: repoRoot,
        stdio: 'inherit'
      })

process.exit(result.status ?? 1)
