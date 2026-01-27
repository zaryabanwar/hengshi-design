import React from 'react'
import ReactDOM from 'react-dom/client'

import App from './App'
import './index.css'

const rootElement =
  document.getElementById('root') ??
  document.getElementById('app') ??
  (() => {
    const element = document.createElement('div')
    element.id = 'root'
    document.body.appendChild(element)
    return element
  })()

ReactDOM.createRoot(rootElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)
