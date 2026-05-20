import { defineStore } from 'pinia'
import api from '../api/axios'

// Helper function to decode JWT payload safely in the browser
function parseJwt(token) {
  try {
    const base64Url = token.split('.')[1]
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
    const jsonPayload = decodeURIComponent(
      window.atob(base64)
        .split('')
        .map((c) => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
        .join('')
    )
    return JSON.parse(jsonPayload)
  } catch (error) {
    return null
  }
}

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: JSON.parse(localStorage.getItem('user')) || null,
    token: localStorage.getItem('access_token') || null,
    loading: false,
    error: null,
  }),

  getters: {
    isAuthenticated: (state) => !!state.token,
    userRole: (state) => state.user?.role || null,
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
        
        // Decode user details and role from custom JWT payload
        const decoded = parseJwt(this.token)
        if (decoded) {
          this.user = {
            username: decoded.username,
            role: decoded.role,
          }
          localStorage.setItem('user', JSON.stringify(this.user))
        } else {
          this.user = { username }
          localStorage.setItem('user', JSON.stringify(this.user))
        }
        
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
