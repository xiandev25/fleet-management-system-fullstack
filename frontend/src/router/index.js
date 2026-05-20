import { createRouter, createWebHistory } from 'vue-router'
import Landing from '../views/Landing.vue'
import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue'
import MainLayout from '../components/MainLayout.vue'
import { useAuthStore } from '../stores/auth'

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: Landing
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { guest: true }
  },
  {
    path: '/dashboard',
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

// Navigation Guard: Protect FMS secure routes and restrict access strictly to ADMIN / MANAGER
router.beforeEach((to, from, next) => {
  const auth = useAuthStore()
  
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!auth.isAuthenticated) {
      next('/login')
    } else {
      const role = auth.userRole
      if (role === 'ADMIN' || role === 'MANAGER') {
        next()
      } else {
        // Log out unauthorized roles and send to login
        auth.logout()
        next('/login')
      }
    }
  } else if (to.matched.some(record => record.meta.guest) && auth.isAuthenticated) {
    next('/dashboard')
  } else {
    next()
  }
})

export default router
