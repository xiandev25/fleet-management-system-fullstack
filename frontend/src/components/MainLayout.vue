<template>
  <div class="min-h-screen flex bg-brand-asphalt text-gray-100 font-sans">
    
    <!-- Desktop Sidebar -->
    <aside class="w-64 bg-brand-asphalt-light border-r border-brand-asphalt-lighter hidden md:flex flex-col">
      <!-- Brand Logo -->
      <div class="h-16 flex items-center px-6 gap-3 border-b border-brand-asphalt-lighter">
        <!-- SVG Road Logo -->
        <svg class="w-8 h-8 text-brand-highway-yellow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
        </svg>
        <span class="font-extrabold text-sm tracking-widest text-gray-50 uppercase">
          FLEET <span class="text-brand-highway-yellow">SYSTEM</span>
        </span>
      </div>

      <!-- Navigation Links -->
      <nav class="flex-grow p-4 space-y-1">
        <router-link
          v-for="item in navItems"
          :key="item.name"
          :to="item.to"
          class="flex items-center gap-3 px-4 py-3 rounded-lg text-sm font-medium transition-all duration-200 group"
          :class="isActive(item.to) 
            ? 'bg-brand-highway-yellow/10 text-brand-highway-yellow border border-brand-highway-yellow/30 font-semibold shadow-md' 
            : 'text-gray-400 hover:bg-brand-asphalt-lighter hover:text-gray-100 border border-transparent'"
        >
          <component 
            :is="item.icon" 
            class="w-5 h-5 transition-transform duration-200 group-hover:scale-110"
            :class="isActive(item.to) ? 'text-brand-highway-yellow' : 'text-gray-400 group-hover:text-gray-200'"
          />
          {{ item.name }}
        </router-link>
      </nav>
    </aside>

    <!-- Main Workspace -->
    <div class="flex-grow flex flex-col min-h-screen overflow-x-hidden">
      
      <!-- Top Header -->
      <header class="h-16 bg-brand-asphalt-light border-b border-brand-asphalt-lighter flex items-center justify-between px-6 z-10">
        
        <!-- Mobile Sidebar Toggle -->
        <button class="md:hidden p-2 rounded-lg text-gray-400 hover:bg-brand-asphalt-lighter hover:text-gray-100">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>

        <!-- Current View Title / Highway Breadcrumb -->
        <div class="hidden sm:flex items-center gap-2 text-xs font-semibold text-gray-400 uppercase tracking-widest">
          <span>Route</span>
          <span class="text-brand-highway-yellow">➔</span>
          <span class="text-gray-200">{{ currentRouteName }}</span>
        </div>

        <!-- Quick Actions -->
        <div class="flex items-center gap-4">
          <!-- System Status Pill -->
          <div class="flex items-center gap-2 bg-brand-asphalt-lighter border border-brand-asphalt-lighter rounded-full px-3 py-1 text-xs">
            <span class="w-2.5 h-2.5 rounded-full bg-status-go animate-pulse"></span>
            <span class="text-gray-300 font-medium tracking-wide">All Routes Clear</span>
          </div>

          <!-- Reusable User Menu Settings Dropdown -->
          <UserMenu />
        </div>
      </header>

      <!-- Page Content Content -->
      <main class="flex-grow p-6 md:p-8 overflow-y-auto max-w-7xl w-full mx-auto">
        <router-view v-slot="{ Component }">
          <transition 
            name="fade" 
            mode="out-in"
          >
            <component :is="Component" />
          </transition>
        </router-view>
      </main>

    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import UserMenu from './UserMenu.vue'

const route = useRoute()

// Current route name for dashboard header
const currentRouteName = computed(() => {
  return route.name || 'Overview'
})

// Active route class checker
const isActive = (path) => {
  return route.path === path
}

// Navigation SVG components
const DashboardIcon = {
  template: `
    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v4a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v4a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
    </svg>
  `
}

const FleetIcon = {
  template: `
    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" d="M9 17a2 2 0 11-4 0 2 2 0 014 0zM19 17a2 2 0 11-4 0 2 2 0 014 0z" />
      <path stroke-linecap="round" stroke-linejoin="round" d="M13 16V6a1 1 0 00-1-1H4a1 1 0 00-1 1v10M13 16h6.18a2 2 0 001.956-1.578l1.422-5.69A2 2 0 0020.6 6.222H13M13 16V6" />
    </svg>
  `
}

const RoutesIcon = {
  template: `
    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
    </svg>
  `
}

const ClientsIcon = {
  template: `
    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
    </svg>
  `
}

const OperationsIcon = {
  template: `
    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
    </svg>
  `
}

const BillingIcon = {
  template: `
    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
    </svg>
  `
}

// Streamlined Superadmin & Manager specific navigations
const navItems = computed(() => {
  return [
    { name: 'Dashboard', to: '/dashboard', icon: DashboardIcon },
    { name: 'Fleet', to: '/dashboard/fleet', icon: FleetIcon },
    { name: 'Routes', to: '/dashboard/routes', icon: RoutesIcon },
    { name: 'Clients', to: '/dashboard/clients', icon: ClientsIcon },
    { name: 'Operations', to: '/dashboard/operations', icon: OperationsIcon },
    { name: 'Billing', to: '/dashboard/billing', icon: BillingIcon },
  ]
})
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.fade-enter-from {
  opacity: 0;
  transform: translateY(6px);
}

.fade-leave-to {
  opacity: 0;
  transform: translateY(-6px);
}
</style>
