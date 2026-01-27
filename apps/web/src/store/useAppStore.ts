import { create } from 'zustand'

type AppState = {
  theme: 'light' | 'dark'
  toggleTheme: () => void
}

export const useAppStore = create<AppState>((set) => ({
  theme: 'light',
  toggleTheme: () =>
    set((state) => ({
      theme: state.theme === 'light' ? 'dark' : 'light'
    }))
}))
