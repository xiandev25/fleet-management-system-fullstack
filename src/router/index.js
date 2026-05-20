import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue'
import MainLayout from '../components/MainLayout.vue'
import { useAuthStore } from '../stores/auth'

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { guest: true }
  },
  {
    path: '/',
    component: MainLayout,
    meta: { requiresAuth: true },
    children: [
      {
        path: '',
        name: 'Dashboard',
        component: Dashboard
      }
    ]
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// Navigation Guard: Protect secure routes and redirect logged-in users away from guest pages
router.beforeEach((to, from, next) => {
  const auth = useAuthStore()
  
  if (to.matched.some(record => record.meta.requiresAuth) && !auth.isAuthenticated) {
    next('/login')
  } else if (to.matched.some(record => record.meta.guest) && auth.isAuthenticated) {
    next('/')
  } else {
    next()
  }
})

export default router
