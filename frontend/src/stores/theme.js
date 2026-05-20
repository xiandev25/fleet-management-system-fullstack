import { defineStore } from 'pinia'

export const useThemeStore = defineStore('theme', {
  state: () => ({
    theme: localStorage.getItem('theme_mode') || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark'),
  }),

  actions: {
    setTheme(newTheme) {
      this.theme = newTheme
      localStorage.setItem('theme_mode', newTheme)
      this.applyTheme()
    },

    applyTheme() {
      const html = document.documentElement
      
      if (this.theme === 'light') {
        html.classList.add('light')
        html.classList.remove('dark')
      } else {
        html.classList.add('dark')
        html.classList.remove('light')
      }
    }
  }
})
