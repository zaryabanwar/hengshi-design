import type { CSSProperties } from 'react'
import tokens from '../../../../docs/phase-1-brand-identity/semantic-tokens.json'

// Accepted D-035 tokens. Figma's Inter fallback is intentionally not shipped.
export const brandStyle = {
  '--ink': tokens.color.ink.value,
  '--slate': tokens.color.slate.value,
  '--stone': tokens.color.stone.value,
  '--mist': tokens.color.mist.value,
  '--paper': tokens.color.paper.value,
  '--cyan': tokens.color.signal.cyan.onDark,
  '--cyan-light': tokens.color.signal.cyan.onLight,
  '--font-text': tokens.typography.text.stack,
  '--font-mono': tokens.typography.evidence.stack,
} as CSSProperties
