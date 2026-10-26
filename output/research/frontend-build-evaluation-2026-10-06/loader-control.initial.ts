// Synthetic public type-entry control; no runtime loader invocation or asset use.
import type { SVGLoader } from 'three-stdlib/loaders/SVGLoader.js'
import type { TGALoader } from 'three-stdlib/loaders/TGALoader.js'

export type LoaderDeclarations = [SVGLoader, TGALoader]
