<template>
  <div class="min-h-screen flex items-center justify-center bg-brand-asphalt px-4 relative overflow-hidden">
    
    <!-- Background highway decorative stripes -->
    <div class="absolute inset-0 opacity-5 pointer-events-none">
      <div class="absolute w-[2px] h-full bg-brand-highway-yellow left-1/3 border-dashed border-spacing-y-4"></div>
      <div class="absolute w-[2px] h-full bg-brand-highway-yellow left-2/3 border-dashed border-spacing-y-4"></div>
    </div>

    <!-- Login Card Container -->
    <div class="w-full max-w-md bg-brand-asphalt-light/80 backdrop-blur-xl border border-brand-asphalt-lighter rounded-2xl shadow-2xl p-8 relative z-10 transition-all duration-300 hover:border-brand-highway-yellow/30">
      
      <!-- Top road/fleet icon header -->
      <div class="flex flex-col items-center mb-8">
        <div class="w-16 h-16 rounded-2xl bg-brand-asphalt flex items-center justify-center border-2 border-brand-highway-yellow shadow-lg shadow-brand-highway-yellow-glow mb-4">
          <svg class="w-9 h-9 text-brand-highway-yellow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
          </svg>
        </div>
        <h2 class="text-2xl font-extrabold tracking-wider text-gray-50 uppercase">
          FLEET<span class="text-brand-highway-yellow">FLOW</span>
        </h2>
        <p class="text-xs text-gray-400 font-semibold uppercase tracking-widest mt-2">
          Management Portal
        </p>
      </div>

      <!-- Alert Message Box (if login fails) -->
      <transition name="slide-fade">
        <div 
          v-if="auth.error" 
          class="mb-6 p-4 rounded-xl bg-status-stop/10 border border-status-stop/20 flex items-center gap-3 text-status-stop text-sm font-medium"
        >
          <svg class="w-5 h-5 flex-shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
          </svg>
          <span>{{ auth.error }}</span>
        </div>
      </transition>

      <!-- Form -->
      <form @submit.prevent="handleSubmit" class="space-y-6">
        
        <!-- Username Field -->
        <div>
          <label for="username" class="block text-xs font-bold text-gray-400 uppercase tracking-widest mb-2">
            Username
          </label>
          <div class="relative rounded-lg shadow-sm">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg class="h-5 h-5 text-gray-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
              </svg>
            </div>
            <input
              id="username"
              v-model="username"
              type="text"
              required
              class="block w-full pl-10 pr-4 py-3 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-gray-100 placeholder-gray-500 font-medium text-sm focus:outline-none focus:ring-2 focus:ring-brand-highway-yellow/20 focus:border-brand-highway-yellow transition-all duration-200"
              placeholder="e.g. admin"
              autocomplete="username"
            />
          </div>
        </div>

        <!-- Password Field -->
        <div>
          <label for="password" class="block text-xs font-bold text-gray-400 uppercase tracking-widest mb-2">
            Password
          </label>
          <div class="relative rounded-lg shadow-sm">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg class="h-5 h-5 text-gray-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>
            </div>
            <input
              id="password"
              v-model="password"
              type="password"
              required
              class="block w-full pl-10 pr-4 py-3 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-gray-100 placeholder-gray-500 font-medium text-sm focus:outline-none focus:ring-2 focus:ring-brand-highway-yellow/20 focus:border-brand-highway-yellow transition-all duration-200"
              placeholder="••••••••"
              autocomplete="current-password"
            />
          </div>
        </div>

        <!-- Submit Action -->
        <button
          type="submit"
          :disabled="auth.loading"
          class="w-full flex items-center justify-center py-3.5 px-4 bg-brand-highway-yellow hover:bg-brand-highway-yellow-hover disabled:bg-gray-700 text-brand-asphalt font-bold text-sm rounded-xl transition-all duration-200 focus:outline-none focus:ring-4 focus:ring-brand-highway-yellow/20 cursor-pointer shadow-lg hover:shadow-brand-highway-yellow-glow"
        >
          <!-- Spinning Indicator -->
          <svg 
            v-if="auth.loading" 
            class="animate-spin -ml-1 mr-3 h-5 w-5 text-brand-asphalt" 
            fill="none" 
            viewBox="0 0 24 24"
          >
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          <span>{{ auth.loading ? 'Initializing Routes...' : 'Access Dashboard' }}</span>
        </button>
      </form>
      
      <!-- Footer Copyright info resembling highway markings -->
      <div class="mt-8 text-center border-t border-brand-asphalt-lighter pt-5">
        <span class="text-[10px] font-bold text-gray-500 uppercase tracking-widest flex items-center justify-center gap-1.5">
          <span class="w-1.5 h-1.5 rounded-full bg-brand-highway-yellow"></span>
          Secure Connection Active
          <span class="w-1.5 h-1.5 rounded-full bg-brand-highway-yellow"></span>
        </span>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const auth = useAuthStore()
const router = useRouter()

const username = ref('')
const password = ref('')

const handleSubmit = async () => {
  const success = await auth.login(username.value, password.value)
  if (success) {
    router.push('/')
  }
}
</script>

<style scoped>
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}
.slide-fade-leave-active {
  transition: all 0.2s cubic-gradient(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateY(-8px);
  opacity: 0;
}
</style>
