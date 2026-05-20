<template>
  <div class="dashboard-view-wrapper">
    <transition name="fade" mode="out-in">
      <component :is="dashboardComponent" />
    </transition>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useAuthStore } from '../stores/auth'
import ManagerDashboard from '../components/ManagerDashboard.vue'
import GuardianDashboard from '../components/GuardianDashboard.vue'
import DriverDashboard from '../components/DriverDashboard.vue'

const auth = useAuthStore()

// Dynamic component resolver based on current session's RBAC role
const dashboardComponent = computed(() => {
  const role = auth.userRole
  if (role === 'ADMIN' || role === 'MANAGER') {
    return ManagerDashboard
  }
  if (role === 'DRIVER') {
    return DriverDashboard
  }
  if (role === 'GUARDIAN') {
    return GuardianDashboard
  }
  // Fallback fallback dashboard for other roles (Mechanic, Guardian fallback)
  return {
    template: `
      <div class="bg-brand-asphalt-light border border-brand-asphalt-lighter p-8 rounded-2xl text-center max-w-xl mx-auto space-y-4">
        <div class="w-12 h-12 rounded-xl bg-brand-asphalt mx-auto flex items-center justify-center border border-brand-asphalt-lighter text-brand-highway-yellow">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
          </svg>
        </div>
        <h3 class="text-base font-extrabold text-gray-50 uppercase tracking-wide">Account Role Unassigned</h3>
        <p class="text-xs text-gray-400 font-medium">Your profile is registered inside Fleet Flow, but does not have a verified operational access tier mapped to your token. Please contact system dispatch administrators.</p>
      </div>
    `
  }
})
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.15s ease, transform 0.15s ease;
}
.fade-enter-from {
  opacity: 0;
  transform: translateY(4px);
}
.fade-leave-to {
  opacity: 0;
  transform: translateY(-4px);
}
</style>
