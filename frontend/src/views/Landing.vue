<template>
  <div class="h-screen w-screen bg-brand-asphalt text-gray-100 relative overflow-hidden font-sans flex flex-col justify-between p-6 md:p-8 select-none">
    
    <!-- Toast Notification (Logout Success) -->
    <transition name="toast">
      <div 
        v-if="showToast" 
        class="fixed top-8 left-1/2 -translate-x-1/2 z-50 bg-brand-asphalt-light border border-status-go/30 px-5 py-3 rounded-2xl shadow-2xl flex items-center gap-3 backdrop-blur-xl"
      >
        <span class="w-2.5 h-2.5 rounded-full bg-status-go animate-pulse"></span>
        <span class="text-xs font-black uppercase tracking-wider text-gray-200">
          System Node: Signed Out Successfully
        </span>
      </div>
    </transition>
    
    <!-- Decorative Grid Background (Midnight starry yellow in dark, sunrise sky blue in light) -->
    <div class="absolute inset-0 opacity-100 pointer-events-none bg-[linear-gradient(to_right,var(--grid-color)_1px,transparent_1px),linear-gradient(to_bottom,var(--grid-color)_1px,transparent_1px)] bg-[size:4rem_4rem]"></div>
    
    <!-- Glowing background anomaly representing the Sunrise of Hope / Telemetry Hotspot -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-brand-highway-yellow/10 rounded-full blur-[140px] pointer-events-none animate-pulse"></div>

    <!-- 1. HEADER -->
    <header class="w-full max-w-7xl mx-auto flex items-center justify-between z-10 relative">
      <div class="flex items-center gap-3">
        <!-- Minimal FMS Badge (Favicon) -->
        <div class="w-9 h-9 flex items-center justify-center">
          <img src="/favicon.svg" alt="FMS Logo" class="w-full h-full object-contain" />
        </div>
        <span class="font-extrabold text-sm tracking-widest text-gray-50 uppercase">
          FLEET MANAGEMENT <span class="text-brand-highway-yellow">SYSTEM</span>
        </span>
      </div>

      <div class="flex items-center gap-3">
        <!-- Reusable User/Preferences Dropdown -->
        <UserMenu />
      </div>
    </header>

    <!-- 2. CENTRAL HERO BLOCK (Single-Frame Focused Overlay) -->
    <main class="w-full max-w-xl mx-auto flex flex-col items-center text-center justify-center flex-grow z-10 relative">
      
      <!-- Minimal Telemetry Badge representing the Community -->
      <div class="inline-flex items-center gap-2 bg-brand-asphalt-light border border-brand-asphalt-lighter rounded-full px-4.5 py-1.5 text-[9px] font-black uppercase tracking-widest text-brand-highway-yellow mb-8 shadow-sm">
        <span>●</span>
        <span>Community Fleet Management</span>
        <span>●</span>
      </div>

      <h1 class="text-4xl md:text-5xl font-black tracking-tighter text-gray-50 uppercase leading-none mb-6">
        SAFE & RELIABLE<br />
        <span class="text-brand-highway-yellow">SCHOOL TRANSIT</span>
      </h1>

      <p class="text-sm text-gray-400 font-medium tracking-wide max-w-md mb-10 leading-relaxed">
        A unified platform connecting fleet managers, school administrators, and families for a secure, eco-friendly daily commute.
      </p>

      <!-- Hopeful CTA Button -->
      <router-link
        :to="auth.isAuthenticated ? '/dashboard' : '/login'"
        class="px-8 py-4 bg-brand-highway-yellow hover:bg-brand-highway-yellow-hover text-brand-asphalt font-black text-xs uppercase tracking-widest rounded-2xl transition duration-200 shadow-xl hover:scale-[1.03] cursor-pointer inline-flex items-center gap-2 active:scale-98"
      >
        <span>ENTER SYSTEM PORTAL</span>
        <span class="text-sm font-semibold">➔</span>
      </router-link>

    </main>

    <!-- 3. FOOTER (Minimalist representation of "The Naked Nature, the Road and Hope") -->
    <footer class="w-full max-w-7xl mx-auto flex flex-col items-center z-10 relative">
      
      <div class="w-full flex flex-col md:flex-row items-center justify-between text-[9px] font-bold text-gray-500 uppercase tracking-widest gap-4 mt-8">
        <span>© 2026 Fleet Management System. All systems nominal.</span>
        <span class="flex items-center gap-2">
          <span class="w-1.5 h-1.5 rounded-full bg-status-go animate-ping"></span>
          <span>Eco-Friendly Community Transit & Family Trust</span>
        </span>
      </div>
    </footer>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import UserMenu from '../components/UserMenu.vue'

const auth = useAuthStore()
const route = useRoute()
const router = useRouter()

const showToast = ref(false)

onMounted(() => {
  if (route.query.logout === 'success') {
    showToast.value = true
    
    // Clear query parameter from URL
    router.replace({ query: {} })
    
    setTimeout(() => {
      showToast.value = false
    }, 3500)
  }
})
</script>

<style scoped>
@keyframes roadTravel {
  0% {
    left: -10%;
    opacity: 0;
  }
  15% {
    opacity: 1;
  }
  85% {
    opacity: 1;
  }
  100% {
    left: 110%;
    opacity: 0;
  }
}

.animate-road-travel {
  animation: roadTravel 5s cubic-bezier(0.4, 0, 0.2, 1) infinite;
}

/* Toast Transition */
.toast-enter-active {
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.toast-leave-active {
  transition: all 0.3s cubic-bezier(0.82, 0, 0.88, 0.1);
}
.toast-enter-from,
.toast-leave-to {
  transform: translate(-50%, -24px) scale(0.95);
  opacity: 0;
}
</style>
