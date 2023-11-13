import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.scss'
import { BrowserRouter } from 'react-router-dom'
import { Container } from '@components/Container'
import { PersistentStoreProvider } from './store'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <PersistentStoreProvider>
      <BrowserRouter>
        <Container>
          <App />
        </Container>
      </BrowserRouter>
    </PersistentStoreProvider>
  </React.StrictMode>,
)
