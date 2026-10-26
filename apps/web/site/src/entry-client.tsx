import { hydrateRoot } from 'react-dom/client'
import { Site } from './Site'

const root = document.getElementById('site-root')
if (!root) throw new Error('The semantic site root is missing')
hydrateRoot(root, <Site path={window.location.pathname} />)
