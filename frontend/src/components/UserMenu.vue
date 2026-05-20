<template>
  <div class="relative inline-block text-left z-30">
    <!-- Dropdown Trigger Button -->
    <button 
      @click="toggleMenu"
      class="flex items-center justify-center w-9 h-9 rounded-xl transition-all duration-200 border cursor-pointer select-none active:scale-95"
      :class="auth.isAuthenticated 
        ? 'bg-brand-asphalt-light hover:bg-brand-asphalt-lighter border-brand-highway-yellow/20 hover:border-brand-highway-yellow/40 text-brand-highway-yellow font-bold text-xs shadow-md'
        : 'bg-brand-asphalt-light hover:bg-brand-asphalt-lighter border-brand-asphalt-lighter hover:border-gray-500/40 text-gray-400 hover:text-gray-200'"
    >
      <span v-if="auth.isAuthenticated">{{ userInitials }}</span>
      <svg v-else class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
      </svg>
    </button>

    <!-- Invisible Backdrop to close menu on click outside -->
    <div 
      v-if="isOpen" 
      @click="closeMenu"
      class="fixed inset-0 z-40 bg-transparent cursor-default"
    ></div>

    <!-- Dropdown Menu Card -->
    <transition name="wind">
      <div 
        v-if="isOpen" 
        class="absolute right-0 mt-2.5 w-56 rounded-2xl bg-brand-asphalt-light border border-brand-asphalt-lighter shadow-2xl p-3.5 z-50 text-left flex flex-col gap-3 backdrop-blur-xl"
      >
        <!-- A. Header (User Info / Status) -->
        <div class="px-1.5 py-1">
          <h4 class="font-extrabold text-xs uppercase tracking-wider text-gray-50 truncate">
            {{ auth.isAuthenticated ? auth.user?.username : 'Guest Node' }}
          </h4>
          <span 
            class="inline-flex items-center mt-1 px-1.5 py-0.5 rounded text-[8px] font-black uppercase tracking-widest border"
            :class="auth.isAuthenticated
              ? 'bg-brand-sign-blue-glow text-brand-sign-blue border-brand-sign-blue/20'
              : 'bg-brand-asphalt-lighter text-gray-500 border-brand-asphalt-lighter'"
          >
            {{ auth.isAuthenticated ? auth.user?.role : 'Unauthorized' }}
          </span>
        </div>

        <div class="h-[1px] bg-brand-asphalt-lighter"></div>

        <!-- B. Display Theme Preferences -->
        <div class="px-1">
          <span class="text-[8px] font-black text-gray-500 uppercase tracking-widest block mb-2">Display Mode</span>
          <div class="grid grid-cols-2 bg-brand-asphalt/60 border border-brand-asphalt-lighter p-0.5 rounded-xl">
            <button 
              v-for="opt in themes"
              :key="opt.id"
              @click="themeStore.setTheme(opt.id)"
              class="py-1 rounded-lg text-[8px] font-black uppercase tracking-wider text-center transition-all duration-150 cursor-pointer"
              :class="themeStore.theme === opt.id 
                ? 'bg-brand-highway-yellow text-brand-asphalt font-black shadow-sm' 
                : 'text-gray-400 hover:text-gray-200'"
            >
              {{ opt.label }}
            </button>
          </div>
        </div>

        <div class="h-[1px] bg-brand-asphalt-lighter"></div>

        <!-- C. Action Footer -->
        <div class="px-0.5">
          <button 
            v-if="auth.isAuthenticated"
            @click="handleLogout"
            class="w-full flex items-center justify-between px-3 py-2 rounded-xl text-[10px] font-extrabold uppercase tracking-wider text-red-400 hover:bg-red-500/10 transition duration-150 cursor-pointer"
          >
            <span>Sign Out</span>
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M17 16l4-4m0 0l-4-4m4 4H7" />
            </svg>
          </button>
          <router-link
            v-else
            to="/login"
            @click="closeMenu"
            class="w-full flex items-center justify-between px-3 py-2 rounded-xl text-[10px] font-extrabold uppercase tracking-wider bg-brand-highway-yellow hover:bg-brand-highway-yellow-hover text-brand-asphalt transition duration-150 cursor-pointer shadow-sm shadow-brand-highway-yellow-glow"
          >
            <span>Log In</span>
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M11 16l4-4m0 0l-4-4m4 4H3" />
            </svg>
          </router-link>
        </div>

      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { useThemeStore } from '../stores/theme'

const auth = useAuthStore()
const themeStore = useThemeStore()
const router = useRouter()

const isOpen = ref(false)

const themes = [
  { id: 'light', label: 'Light' },
  { id: 'dark', label: 'Dark' }
]

const toggleMenu = () => {
  isOpen.value = !isOpen.value
}

const closeMenu = () => {
  isOpen.value = false
}

// User Initials
const userInitials = computed(() => {
  const name = auth.user?.username || 'G'
  return name.slice(0, 2).toUpperCase()
})

// Logout Logic
const handleLogout = () => {
  isOpen.value = false
  auth.logout()
  router.push({ path: '/', query: { logout: 'success' } })
}
</script>

<style scoped>
/* Wind Down Transition */
.wind-enter-active {
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}
.wind-leave-active {
  transition: all 0.15s cubic-bezier(0.82, 0, 0.88, 0.1);
}
.wind-enter-from,
.wind-leave-to {
  transform: translateY(-8px) scale(0.96);
  opacity: 0;
}
</style>
