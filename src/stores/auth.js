import { defineStore } from 'pinia'
import api from '../api/axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: JSON.parse(localStorage.getItem('user')) || null,
    token: localStorage.getItem('access_token') || null,
    loading: false,
    error: null,
  }),

  getters: {
    isAuthenticated: (state) => !!state.token,
  },

  actions: {
    async login(username, password) {
      this.loading = true
      this.error = null
      try {
        const response = await api.post('token/', { username, password })
        this.token = response.data.access
        localStorage.setItem('access_token', this.token)
        localStorage.setItem('refresh_token', response.data.refresh)
        
        // You could also fetch user details here if needed
        this.user = { username } // Placeholder
        localStorage.setItem('user', JSON.stringify(this.user))
        
        return true
      } catch (err) {
        this.error = err.response?.data?.detail || 'Login failed'
        return false
      } finally {
        this.loading = false
      }
    },

    logout() {
      this.user = null
      this.token = null
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      localStorage.removeItem('user')
    },
  },
})
