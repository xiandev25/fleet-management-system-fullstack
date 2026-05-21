<template>
  <div class="space-y-8">
    
    <!-- Hero Header resembling a modern telemetry dashboard -->
    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 bg-brand-asphalt-light p-6 rounded-2xl border border-brand-asphalt-lighter">
      <div>
        <h1 class="text-2xl font-black text-gray-50 uppercase tracking-wide">
          Operations <span class="text-brand-highway-yellow">Telemetry</span>
        </h1>
        <p class="text-xs font-semibold text-gray-400 uppercase tracking-widest mt-1">
          Real-time fleet & logistics tracking panel
        </p>
      </div>
      
      <!-- Date Display Badge -->
      <div class="flex items-center gap-2 px-4 py-2 bg-brand-asphalt rounded-xl border border-brand-asphalt-lighter text-xs font-bold uppercase tracking-wider text-gray-400">
        <svg class="w-4 h-4 text-brand-highway-yellow" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
        </svg>
        System Status: <span class="text-status-go">Active</span>
      </div>
    </div>

    <!-- Quick Stats Grid (Road Dashboard Metrics) -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
      
      <!-- Stat 1: Vehicles -->
      <div class="bg-brand-asphalt-light p-6 rounded-2xl border border-brand-asphalt-lighter flex items-center justify-between transition-all hover:border-brand-highway-yellow/20">
        <div class="space-y-1">
          <span class="text-xs font-extrabold text-gray-400 uppercase tracking-widest">Fleet Size</span>
          <h2 class="text-3xl font-black text-gray-100">{{ stats.vehicles.total }}</h2>
          <span class="text-xs text-status-go font-semibold">{{ stats.vehicles.active }} Operational</span>
        </div>
        <div class="w-12 h-12 rounded-xl bg-brand-asphalt flex items-center justify-center border border-brand-asphalt-lighter">
          <svg class="w-6 h-6 text-brand-highway-yellow" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 17a2 2 0 11-4 0 2 2 0 014 0zM19 17a2 2 0 11-4 0 2 2 0 014 0z" />
            <path stroke-linecap="round" stroke-linejoin="round" d="M13 16V6a1 1 0 00-1-1H4a1 1 0 00-1 1v10M13 16h6.18a2 2 0 001.956-1.578l1.422-5.69A2 2 0 0020.6 6.222H13M13 16V6" />
          </svg>
        </div>
      </div>

      <!-- Stat 2: Maintenance Alerts -->
      <div class="bg-brand-asphalt-light p-6 rounded-2xl border border-brand-asphalt-lighter flex items-center justify-between transition-all hover:border-brand-highway-yellow/20">
        <div class="space-y-1">
          <span class="text-xs font-extrabold text-gray-400 uppercase tracking-widest">In Workshop</span>
          <h2 class="text-3xl font-black text-gray-100">{{ stats.vehicles.maintenance }}</h2>
          <span class="text-xs text-status-caution font-semibold">Needs Attention</span>
        </div>
        <div class="w-12 h-12 rounded-xl bg-brand-asphalt flex items-center justify-center border border-brand-asphalt-lighter">
          <svg class="w-6 h-6 text-status-caution" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
          </svg>
        </div>
      </div>

      <!-- Stat 3: Lines -->
      <div class="bg-brand-asphalt-light p-6 rounded-2xl border border-brand-asphalt-lighter flex items-center justify-between transition-all hover:border-brand-highway-yellow/20">
        <div class="space-y-1">
          <span class="text-xs font-extrabold text-gray-400 uppercase tracking-widest">Active Lines</span>
          <h2 class="text-3xl font-black text-gray-100">{{ stats.routes.total }}</h2>
          <span class="text-xs text-brand-sign-blue font-semibold">Transit Channels</span>
        </div>
        <div class="w-12 h-12 rounded-xl bg-brand-asphalt flex items-center justify-center border border-brand-asphalt-lighter">
          <svg class="w-6 h-6 text-brand-sign-blue" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
          </svg>
        </div>
      </div>

      <!-- Stat 4: Billing Alerts -->
      <div class="bg-brand-asphalt-light p-6 rounded-2xl border border-brand-asphalt-lighter flex items-center justify-between transition-all hover:border-brand-highway-yellow/20">
        <div class="space-y-1">
          <span class="text-xs font-extrabold text-gray-400 uppercase tracking-widest">Unpaid Bills</span>
          <h2 class="text-3xl font-black text-status-stop">{{ stats.billing.unpaid }}</h2>
          <span class="text-xs text-gray-400 font-semibold">Payment Claims</span>
        </div>
        <div class="w-12 h-12 rounded-xl bg-brand-asphalt flex items-center justify-center border border-brand-asphalt-lighter">
          <svg class="w-6 h-6 text-status-stop" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
          </svg>
        </div>
      </div>

    </div>

    <!-- Active Vehicles Inventory Table -->
    <div class="bg-brand-asphalt-light rounded-2xl border border-brand-asphalt-lighter overflow-hidden">
      
      <!-- Table Header -->
      <div class="px-6 py-5 border-b border-brand-asphalt-lighter flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 bg-brand-asphalt/20">
        <div>
          <h3 class="text-base font-extrabold text-gray-50 uppercase tracking-wide">
            Fleet Dispatch <span class="text-brand-highway-yellow">Inventory</span>
          </h3>
          <p class="text-xs text-gray-400 mt-0.5">List of deployed motor assets in the registry</p>
        </div>
        
        <!-- Action Buttons -->
        <!-- <button 
          @click="showAddVehicleModal = true"
          class="flex items-center gap-2 px-4 py-2 bg-brand-highway-yellow hover:bg-brand-highway-yellow-hover text-brand-asphalt font-bold text-xs rounded-xl uppercase tracking-wider transition duration-150 cursor-pointer shadow-md hover:scale-[1.02]"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
          </svg>
          Register Bus
        </button> -->
      </div>

      <!-- Table Body -->
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr class="border-b border-brand-asphalt-lighter bg-brand-asphalt/40 text-[10px] font-extrabold text-gray-400 uppercase tracking-wider">
              <th class="px-6 py-4">Vehicle Model</th>
              <th class="px-6 py-4">License Number</th>
              <th class="px-6 py-4">Registry ID</th>
              <th class="px-6 py-4">Mileage</th>
              <th class="px-6 py-4">Service Status</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-brand-asphalt-lighter">
            <tr 
              v-for="bus in vehicles" 
              :key="bus.id" 
              class="hover:bg-brand-asphalt/10 transition duration-150 text-sm"
            >
              <td class="px-6 py-4 font-bold text-gray-100">
                {{ bus.brand }} <span class="font-normal text-gray-400 text-xs">{{ bus.model }}</span>
              </td>
              <td class="px-6 py-4 font-mono font-semibold text-brand-highway-yellow">
                {{ bus.license_plate }}
              </td>
              <td class="px-6 py-4 text-xs font-semibold text-gray-400">
                {{ bus.immatriculation_number }}
              </td>
              <td class="px-6 py-4 font-medium text-gray-300">
                {{ bus.current_mileage.toLocaleString() }} KM
              </td>
              <td class="px-6 py-4">
                <span 
                  class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold uppercase tracking-wider border"
                  :class="statusClass(bus.status)"
                >
                  {{ bus.status_display || bus.status }}
                </span>
              </td>
            </tr>
            <tr v-if="vehicles.length === 0">
              <td colspan="5" class="text-center py-8 text-gray-500 font-semibold">
                No vehicles registered. Click "Register Bus" to add one!
              </td>
            </tr>
          </tbody>
        </table>
      </div>

    </div>

    <!-- Modals (Simple overlays for registering resources) -->
    <div 
      v-if="showAddVehicleModal" 
      class="fixed inset-0 bg-brand-asphalt/85 backdrop-blur-md flex items-center justify-center z-50 p-4"
      @click.self="showAddVehicleModal = false"
    >
      <div class="w-full max-w-md bg-brand-asphalt-light rounded-2xl border border-brand-asphalt-lighter shadow-2xl p-6 space-y-6">
        <div>
          <h3 class="text-lg font-black text-gray-50 uppercase tracking-wide">
            Register New <span class="text-brand-highway-yellow">Vehicle</span>
          </h3>
          <p class="text-xs text-gray-400 mt-0.5">Introduce a new bus asset to the transport pool</p>
        </div>

        <form @submit.prevent="addVehicle" class="space-y-4">
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-[10px] font-bold text-gray-400 uppercase tracking-wider mb-2">Brand</label>
              <input v-model="newVehicle.brand" required type="text" placeholder="e.g. Toyota" class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow" />
            </div>
            <div>
              <label class="block text-[10px] font-bold text-gray-400 uppercase tracking-wider mb-2">Model</label>
              <input v-model="newVehicle.model" required type="text" placeholder="e.g. Coaster" class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow" />
            </div>
          </div>
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-[10px] font-bold text-gray-400 uppercase tracking-wider mb-2">Plate Number</label>
              <input v-model="newVehicle.license_plate" required type="text" placeholder="e.g. LT-123-XY" class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow" />
            </div>
            <div>
              <label class="block text-[10px] font-bold text-gray-400 uppercase tracking-wider mb-2">Immatriculation ID</label>
              <input v-model="newVehicle.immatriculation_number" required type="text" placeholder="e.g. IM-987" class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow" />
            </div>
          </div>
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-[10px] font-bold text-gray-400 uppercase tracking-wider mb-2">Build Year</label>
              <input v-model="newVehicle.manufacture_year" required type="number" placeholder="2023" class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow" />
            </div>
            <div>
              <label class="block text-[10px] font-bold text-gray-400 uppercase tracking-wider mb-2">Mileage (KM)</label>
              <input v-model="newVehicle.current_mileage" required type="number" placeholder="0" class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow" />
            </div>
          </div>
          <div>
            <label class="block text-[10px] font-bold text-gray-400 uppercase tracking-wider mb-2">Service Status</label>
            <select v-model="newVehicle.status" class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow">
              <option value="AVAILABLE">Available for Trips</option>
              <option value="MAINTENANCE">Under Maintenance</option>
              <option value="OUT_OF_SERVICE">Out of Service</option>
            </select>
          </div>

          <div class="flex gap-3 justify-end pt-4">
            <button type="button" @click="showAddVehicleModal = false" class="px-4 py-2 border border-brand-asphalt-lighter hover:bg-brand-asphalt-lighter text-xs font-bold rounded-xl uppercase tracking-wider">Cancel</button>
            <button type="submit" class="px-4 py-2 bg-brand-highway-yellow hover:bg-brand-highway-yellow-hover text-brand-asphalt font-bold text-xs rounded-xl uppercase tracking-wider shadow-md">Create Bus</button>
          </div>
        </form>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../api/axios'

const vehicles = ref([])
const showAddVehicleModal = ref(false)

const stats = ref({
  vehicles: { total: 0, active: 0, maintenance: 0 },
  routes: { total: 0 },
  billing: { unpaid: 0 }
})

const newVehicle = ref({
  brand: '',
  model: '',
  license_plate: '',
  immatriculation_number: '',
  manufacture_year: new Date().getFullYear(),
  current_mileage: 0,
  status: 'AVAILABLE'
})

// Fetch summary metrics & data lists
const fetchData = async () => {
  try {
    const res = await api.get('fleet/vehicles/')
    vehicles.value = res.data

    // Compile active vs workshop statistics dynamically
    stats.value.vehicles.total = vehicles.value.length
    stats.value.vehicles.active = vehicles.value.filter(v => v.status === 'AVAILABLE').length
    stats.value.vehicles.maintenance = vehicles.value.filter(v => v.status === 'MAINTENANCE').length
  } catch (err) {
    console.error('Error fetching dashboard telemetry:', err)
  }
}

// Add Vehicle
const addVehicle = async () => {
  try {
    await api.post('fleet/vehicles/', newVehicle.value)
    
    // Clear and reload
    newVehicle.value = {
      brand: '',
      model: '',
      license_plate: '',
      immatriculation_number: '',
      manufacture_year: new Date().getFullYear(),
      current_mileage: 0,
      status: 'AVAILABLE'
    }
    showAddVehicleModal.value = false
    await fetchData()
  } catch (err) {
    alert(err.response?.data?.detail || 'Failed to add vehicle.')
  }
}

// Status utility class mapper
const statusClass = (status) => {
  switch (status) {
    case 'AVAILABLE':
      return 'bg-status-go/10 text-status-go border-status-go/20'
    case 'MAINTENANCE':
      return 'bg-status-caution/10 text-status-caution border-status-caution/20'
    default:
      return 'bg-status-stop/10 text-status-stop border-status-stop/20'
  }
}

onMounted(() => {
  fetchData()
})
</script>
