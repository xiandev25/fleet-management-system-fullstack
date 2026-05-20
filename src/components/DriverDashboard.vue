<template>
  <div class="space-y-8">
    
    <!-- Welcome Header -->
    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 bg-brand-asphalt-light p-6 rounded-2xl border border-brand-asphalt-lighter">
      <div>
        <h1 class="text-2xl font-black text-gray-50 uppercase tracking-wide">
          Driver <span class="text-brand-highway-yellow">Console</span>
        </h1>
        <p class="text-xs font-semibold text-gray-400 uppercase tracking-widest mt-1">
          Access assigned transit manifests & vehicle dispatch orders
        </p>
      </div>
      
      <!-- Quick Status -->
      <div class="flex items-center gap-2 px-4 py-2 bg-brand-asphalt rounded-xl border border-brand-asphalt-lighter text-xs font-bold uppercase tracking-wider text-gray-400">
        <svg class="w-4 h-4 text-brand-highway-yellow animate-pulse" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        Trips Today: <span class="text-brand-highway-yellow font-extrabold">{{ assignments.length }} Assigned</span>
      </div>
    </div>

    <!-- Active Trips List -->
    <div class="space-y-5">
      <h3 class="text-xs font-black text-gray-400 uppercase tracking-widest">
        My Shift Dispatch Assignments
      </h3>

      <div class="grid grid-cols-1 gap-6">
        
        <!-- Individual Trip Card -->
        <div 
          v-for="trip in assignments" 
          :key="trip.id" 
          class="bg-brand-asphalt-light rounded-2xl border border-brand-asphalt-lighter p-6 hover:border-brand-highway-yellow/20 transition duration-150 relative overflow-hidden"
        >
          <!-- Top bar with Route & Vehicle info -->
          <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-6 pb-5 border-b border-brand-asphalt-lighter">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-xl bg-brand-sign-blue-glow border border-brand-sign-blue/20 flex items-center justify-center text-brand-sign-blue">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
                </svg>
              </div>
              <div>
                <h4 class="font-extrabold text-gray-50 text-base leading-tight">{{ trip.route_name || 'Assigned Transit Line' }}</h4>
                <span class="text-[10px] text-gray-400 font-bold uppercase tracking-wider block mt-0.5">Route Code #{{ trip.route }}</span>
              </div>
            </div>

            <!-- Vehicle Stats Info Box -->
            <div class="flex items-center gap-4 bg-brand-asphalt px-4 py-2 rounded-xl border border-brand-asphalt-lighter">
              <div class="text-xs">
                <span class="text-gray-500 font-bold uppercase tracking-wider block text-[9px]">Vehicle</span>
                <span class="text-gray-200 font-extrabold">{{ trip.vehicle_details?.brand || 'Toyota' }} {{ trip.vehicle_details?.model || 'Bus' }}</span>
              </div>
              <div class="text-xs border-l border-brand-asphalt-lighter pl-4">
                <span class="text-gray-500 font-bold uppercase tracking-wider block text-[9px]">Plate</span>
                <span class="text-brand-highway-yellow font-black font-mono">{{ trip.vehicle_details?.license_plate || 'LT-555-XY' }}</span>
              </div>
            </div>
          </div>

          <!-- Digital Manifest Stop-by-Stop List -->
          <div>
            <h5 class="text-xs font-black text-gray-400 uppercase tracking-widest mb-4">Route Stop Sequence & Manifest</h5>
            
            <div class="relative pl-6 border-l-2 border-brand-asphalt-lighter space-y-6">
              
              <!-- Stop Indicator (Faked sequence for demo visual) -->
              <div class="relative">
                <!-- Stop bullet -->
                <div class="absolute -left-[31px] top-1 w-4 h-4 rounded-full border-2 border-brand-highway-yellow bg-brand-asphalt flex items-center justify-center">
                  <div class="w-1.5 h-1.5 rounded-full bg-brand-highway-yellow"></div>
                </div>
                <div>
                  <div class="flex justify-between items-center">
                    <h6 class="text-sm font-extrabold text-gray-100">Main Street Stop A</h6>
                    <span class="text-xs font-mono font-bold text-brand-highway-yellow">07:30 AM</span>
                  </div>
                  <p class="text-xs text-gray-400 mt-1">Expected Passengers: <span class="text-gray-300 font-semibold">David Smith, Mary Jones</span></p>
                </div>
              </div>

              <!-- Stop 2 -->
              <div class="relative">
                <div class="absolute -left-[31px] top-1 w-4 h-4 rounded-full border-2 border-brand-asphalt-lighter bg-brand-asphalt flex items-center justify-center">
                  <div class="w-1.5 h-1.5 rounded-full bg-brand-asphalt-lighter"></div>
                </div>
                <div>
                  <div class="flex justify-between items-center">
                    <h6 class="text-sm font-extrabold text-gray-100">Central Avenue Stop B</h6>
                    <span class="text-xs font-mono font-bold text-brand-highway-yellow">07:45 AM</span>
                  </div>
                  <p class="text-xs text-gray-400 mt-1">Expected Passengers: <span class="text-gray-300 font-semibold">Lucas Miller</span></p>
                </div>
              </div>

            </div>
          </div>

        </div>

        <div v-if="assignments.length === 0" class="bg-brand-asphalt-light border border-brand-asphalt-lighter rounded-2xl p-8 text-center text-gray-500 font-semibold">
          No dispatch assignments found for your account on this shift.
        </div>

      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../api/axios'

const assignments = ref([])

const fetchData = async () => {
  try {
    const res = await api.get('operations/trips/')
    assignments.value = res.data
  } catch (err) {
    console.error('Error fetching driver assignments:', err)
  }
}

onMounted(() => {
  fetchData()
})
</script>
