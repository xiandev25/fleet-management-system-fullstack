<template>
  <div class="h-full flex flex-col relative">
    
    <!-- Header & Tabs -->
    <header class="flex flex-col md:flex-row md:items-end justify-between mb-6 gap-4">
      <div>
        <h1 class="text-2xl font-extrabold tracking-wider text-gray-50 uppercase">
          Routes <span class="text-brand-accent-amber">Network</span>
        </h1>
        <p class="text-sm font-semibold tracking-widest text-gray-400 uppercase mt-1">
          Manage bus lines, stops, and shuttles
        </p>
      </div>

      <!-- Tab Navigation -->
      <div class="flex p-1 bg-brand-asphalt-lighter rounded-xl">
        <button 
          @click="activeTab = 'lines'"
          class="px-5 py-2 text-sm font-bold uppercase tracking-wider rounded-lg transition-colors"
          :class="activeTab === 'lines' ? 'bg-brand-accent-amber text-brand-asphalt shadow-sm' : 'text-gray-400 hover:text-gray-200'"
        >
          Bus Lines
        </button>
        <button 
          @click="activeTab = 'shuttles'"
          class="px-5 py-2 text-sm font-bold uppercase tracking-wider rounded-lg transition-colors"
          :class="activeTab === 'shuttles' ? 'bg-brand-accent-amber text-brand-asphalt shadow-sm' : 'text-gray-400 hover:text-gray-200'"
        >
          Shuttles
        </button>
      </div>
    </header>

    <!-- Main Container -->
    <div class="bg-brand-asphalt-light border border-brand-asphalt-lighter rounded-2xl flex-grow flex flex-col overflow-hidden shadow-lg">
      
      <!-- Action Bar -->
      <div class="px-6 py-4 border-b border-brand-asphalt-lighter flex justify-between items-center bg-brand-asphalt/40">
        <h2 class="font-extrabold tracking-widest text-gray-200 uppercase text-sm">
          {{ activeTab === 'lines' ? 'Active Bus Lines' : 'Active Shuttles' }}
        </h2>
        <button 
          @click="activeTab === 'lines' ? openLineModal() : openShuttleModal()"
          class="flex items-center gap-2 px-4 py-2 bg-brand-asphalt-lighter hover:bg-brand-accent-amber/20 hover:text-brand-accent-amber text-gray-300 border border-brand-asphalt-lighter hover:border-brand-accent-amber/50 font-bold text-xs uppercase tracking-wider rounded-xl transition-all"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
          </svg>
          Add {{ activeTab === 'lines' ? 'Line' : 'Shuttle' }}
        </button>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="flex-grow flex items-center justify-center">
        <svg class="animate-spin h-8 w-8 text-brand-accent-amber" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
      </div>

      <!-- LINES VIEW -->
      <div v-else-if="activeTab === 'lines'" class="overflow-x-auto flex-grow">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr class="border-b border-brand-asphalt-lighter bg-brand-asphalt/20">
              <th class="px-6 py-4 text-xs font-black tracking-widest text-gray-500 uppercase">Line Name</th>
              <th class="px-6 py-4 text-xs font-black tracking-widest text-gray-500 uppercase">Description</th>
              <th class="px-6 py-4 text-xs font-black tracking-widest text-gray-500 uppercase text-right">Routing & Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="line in lines" :key="line.id" class="border-b border-brand-asphalt-lighter hover:bg-brand-asphalt/10 transition-colors">
              <td class="px-6 py-4 font-bold text-brand-accent-amber">{{ line.name }}</td>
              <td class="px-6 py-4 text-gray-400 font-medium text-sm">{{ line.description || 'No description provided.' }}</td>
              <td class="px-6 py-4 text-right space-x-3">
                <button @click="openStopsManager(line)" class="text-brand-accent-amber hover:text-brand-accent-amber-hover font-bold text-xs uppercase tracking-wider bg-brand-accent-amber/10 px-3 py-1.5 rounded-lg border border-brand-accent-amber/30 transition-colors mr-2">
                  Manage Stops
                </button>
                <button @click="openLineModal(line)" class="text-brand-sign-blue hover:text-brand-sign-blue-hover transition-colors">
                  <svg class="w-5 h-5 inline-block" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" /></svg>
                </button>
                <button @click="deleteLine(line.id)" class="text-status-stop hover:text-red-400 transition-colors">
                  <svg class="w-5 h-5 inline-block" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
                </button>
              </td>
            </tr>
            <tr v-if="lines.length === 0">
              <td colspan="3" class="px-6 py-12 text-center text-gray-500 font-medium italic">No bus lines established yet.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- SHUTTLES VIEW -->
      <div v-else-if="activeTab === 'shuttles'" class="overflow-x-auto flex-grow">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr class="border-b border-brand-asphalt-lighter bg-brand-asphalt/20">
              <th class="px-6 py-4 text-xs font-black tracking-widest text-gray-500 uppercase">Shuttle Name</th>
              <th class="px-6 py-4 text-xs font-black tracking-widest text-gray-500 uppercase">Pickup Point</th>
              <th class="px-6 py-4 text-xs font-black tracking-widest text-gray-500 uppercase">Time</th>
              <th class="px-6 py-4 text-xs font-black tracking-widest text-gray-500 uppercase text-right">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="shuttle in shuttles" :key="shuttle.id" class="border-b border-brand-asphalt-lighter hover:bg-brand-asphalt/10 transition-colors">
              <td class="px-6 py-4 font-bold text-brand-accent-amber">{{ shuttle.name }}</td>
              <td class="px-6 py-4 text-gray-200 font-medium text-sm">{{ shuttle.pickup_point }}</td>
              <td class="px-6 py-4 text-gray-400 font-medium">{{ formatTime(shuttle.scheduled_time) }}</td>
              <td class="px-6 py-4 text-right space-x-3">
                <button @click="openShuttleModal(shuttle)" class="text-brand-sign-blue hover:text-brand-sign-blue-hover transition-colors">
                  <svg class="w-5 h-5 inline-block" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" /></svg>
                </button>
                <button @click="deleteShuttle(shuttle.id)" class="text-status-stop hover:text-red-400 transition-colors">
                  <svg class="w-5 h-5 inline-block" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
                </button>
              </td>
            </tr>
            <tr v-if="shuttles.length === 0">
              <td colspan="4" class="px-6 py-12 text-center text-gray-500 font-medium italic">No shuttles established yet.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- MODAL: LINE / SHUTTLE CRUD -->
    <div v-if="modal.show" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-brand-asphalt/80 backdrop-blur-sm">
      <div class="bg-brand-asphalt-light border border-brand-asphalt-lighter rounded-2xl w-full max-w-lg shadow-2xl overflow-hidden flex flex-col">
        <div class="px-6 py-4 border-b border-brand-asphalt-lighter flex justify-between items-center bg-brand-asphalt/40">
          <h3 class="text-lg font-extrabold uppercase tracking-widest text-gray-50">
            {{ modal.isEditing ? 'Update' : 'Create' }} {{ modal.type === 'line' ? 'Bus Line' : 'Shuttle' }}
          </h3>
        </div>
        <div class="p-6">
          <form id="resourceForm" @submit.prevent="submitModalForm" class="space-y-4">
            <div>
              <label class="block text-xs font-bold text-gray-400 uppercase tracking-widest mb-1.5">Name</label>
              <input v-model="modal.data.name" required class="w-full px-3 py-2 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-gray-100 text-sm focus:outline-none focus:border-brand-accent-amber" placeholder="Name" />
            </div>
            
            <template v-if="modal.type === 'shuttle'">
              <div>
                <label class="block text-xs font-bold text-gray-400 uppercase tracking-widest mb-1.5">Pickup Point</label>
                <input v-model="modal.data.pickup_point" required class="w-full px-3 py-2 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-gray-100 text-sm focus:outline-none focus:border-brand-accent-amber" placeholder="Location Name" />
              </div>
              <div>
                <label class="block text-xs font-bold text-gray-400 uppercase tracking-widest mb-1.5">Scheduled Time</label>
                <input v-model="modal.data.scheduled_time" type="time" required class="w-full px-3 py-2 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-gray-100 text-sm focus:outline-none focus:border-brand-accent-amber" />
              </div>
            </template>

            <div>
              <label class="block text-xs font-bold text-gray-400 uppercase tracking-widest mb-1.5">Description (Optional)</label>
              <textarea v-model="modal.data.description" rows="3" class="w-full px-3 py-2 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-gray-100 text-sm focus:outline-none focus:border-brand-accent-amber"></textarea>
            </div>
          </form>
        </div>
        <div class="px-6 py-4 border-t border-brand-asphalt-lighter bg-brand-asphalt/40 flex justify-end gap-3">
          <button @click="closeModal" class="px-4 py-2 text-sm font-bold tracking-wider uppercase text-gray-400 hover:text-gray-200">Cancel</button>
          <button form="resourceForm" type="submit" class="px-5 py-2 bg-brand-accent-amber hover:bg-brand-accent-amber-hover text-brand-asphalt font-bold text-sm uppercase tracking-wider rounded-xl shadow-md">Save</button>
        </div>
      </div>
    </div>

    <!-- STOPS MANAGER SLIDE-OVER (Takes up full screen overlay on mobile, right side on desktop) -->
    <div v-if="stopsManager.show" class="fixed inset-0 z-[60] flex justify-end bg-brand-asphalt/60 backdrop-blur-sm">
      <div class="w-full max-w-2xl bg-brand-asphalt-light border-l border-brand-asphalt-lighter h-full shadow-2xl flex flex-col transform transition-transform">
        
        <div class="px-6 py-5 border-b border-brand-asphalt-lighter flex justify-between items-center bg-brand-asphalt/80">
          <div>
            <h2 class="text-xl font-extrabold uppercase tracking-widest text-gray-50">Manage Route Stops</h2>
            <p class="text-xs font-bold tracking-widest text-brand-accent-amber uppercase mt-1">Line: {{ stopsManager.lineName }}</p>
          </div>
          <button @click="closeStopsManager" class="text-gray-400 hover:text-gray-200 p-2 rounded-lg bg-brand-asphalt hover:bg-brand-asphalt-lighter border border-brand-asphalt-lighter">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
          </button>
        </div>

        <!-- Add Stop Inline Form -->
        <div class="p-6 border-b border-brand-asphalt-lighter bg-brand-asphalt/40">
          <h4 class="text-xs font-bold text-gray-400 uppercase tracking-widest mb-3">Add New Stop</h4>
          <form @submit.prevent="submitStop" class="grid grid-cols-2 md:grid-cols-4 gap-3 items-end">
            <div class="col-span-2 md:col-span-1">
              <label class="block text-[10px] font-bold text-gray-500 uppercase tracking-widest mb-1">Sequence #</label>
              <input v-model.number="stopForm.sequence_number" type="number" required min="1" class="w-full px-3 py-2 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-gray-100 text-sm focus:border-brand-accent-amber" placeholder="1" />
            </div>
            <div class="col-span-2 md:col-span-1">
              <label class="block text-[10px] font-bold text-gray-500 uppercase tracking-widest mb-1">Time</label>
              <input v-model="stopForm.scheduled_time" type="time" required class="w-full px-3 py-2 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-gray-100 text-sm focus:border-brand-accent-amber" />
            </div>
            <div class="col-span-2 md:col-span-2">
              <label class="block text-[10px] font-bold text-gray-500 uppercase tracking-widest mb-1">Stop Name</label>
              <div class="flex gap-2">
                <input v-model="stopForm.name" required class="flex-grow px-3 py-2 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-gray-100 text-sm focus:border-brand-accent-amber" placeholder="e.g. Main Gate" />
                <button type="submit" class="px-4 py-2 bg-brand-sign-blue hover:bg-brand-sign-blue-hover text-white font-bold text-xs uppercase tracking-wider rounded-xl shadow-md">Add</button>
              </div>
            </div>
          </form>
        </div>

        <!-- Stops Timeline List -->
        <div class="flex-grow overflow-y-auto p-6 bg-brand-asphalt-light">
          <div v-if="stopsLoading" class="text-center py-8 text-brand-accent-amber">
            Loading sequence...
          </div>
          <div v-else-if="stops.length === 0" class="text-center py-12 text-gray-500 italic font-medium">
            No stops defined for this line yet.
          </div>
          <div v-else class="space-y-4">
            <div v-for="stop in sortedStops" :key="stop.id" class="flex items-center gap-4 bg-brand-asphalt p-4 rounded-xl border border-brand-asphalt-lighter relative">
              <!-- Connector line logic can go here in future -->
              <div class="flex flex-col items-center justify-center w-12 h-12 rounded-lg bg-brand-asphalt-lighter border border-brand-asphalt-lighter flex-shrink-0">
                <span class="text-[10px] text-gray-400 font-bold uppercase">Seq</span>
                <span class="text-lg font-black text-brand-accent-amber leading-none">{{ stop.sequence_number }}</span>
              </div>
              <div class="flex-grow">
                <h4 class="text-gray-100 font-bold">{{ stop.name }}</h4>
                <p class="text-xs text-gray-400 font-medium flex items-center gap-1 mt-1">
                  <svg class="w-3 h-3" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                  {{ formatTime(stop.scheduled_time) }}
                </p>
              </div>
              <button @click="deleteStop(stop.id)" class="text-status-stop hover:bg-status-stop/10 p-2 rounded-lg transition-colors">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
              </button>
            </div>
          </div>
        </div>

      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import routesApi from '../api/routes'

const activeTab = ref('lines')
const loading = ref(false)

const lines = ref([])
const shuttles = ref([])

// Shared Modal State for Line / Shuttle
const modal = ref({
  show: false,
  type: 'line', // 'line' or 'shuttle'
  isEditing: false,
  data: {}
})

// Stops Manager State
const stopsManager = ref({
  show: false,
  lineId: null,
  lineName: ''
})
const stops = ref([])
const stopsLoading = ref(false)

const stopForm = ref({
  sequence_number: 1,
  scheduled_time: '07:00',
  name: '',
  location_name: ''
})

const sortedStops = computed(() => {
  return [...stops.value].sort((a, b) => a.sequence_number - b.sequence_number)
})

// Fetch Data
const fetchData = async () => {
  loading.value = true
  try {
    const [linesRes, shuttlesRes] = await Promise.all([
      routesApi.getLines(),
      routesApi.getShuttles()
    ])
    lines.value = linesRes.data.results || linesRes.data
    shuttles.value = shuttlesRes.data.results || shuttlesRes.data
  } catch (err) {
    console.error("Failed to fetch routes data", err)
  } finally {
    loading.value = false
  }
}

const formatTime = (timeString) => {
  if (!timeString) return '--:--'
  // Remove seconds if present (HH:MM:SS -> HH:MM)
  return timeString.substring(0, 5)
}

// Line / Shuttle Modals
const openLineModal = (line = null) => {
  modal.value = {
    show: true,
    type: 'line',
    isEditing: !!line,
    data: line ? { ...line } : { name: '', description: '' }
  }
}

const openShuttleModal = (shuttle = null) => {
  modal.value = {
    show: true,
    type: 'shuttle',
    isEditing: !!shuttle,
    data: shuttle ? { ...shuttle } : { name: '', pickup_point: '', scheduled_time: '07:00', description: '' }
  }
}

const closeModal = () => {
  modal.value.show = false
}

const submitModalForm = async () => {
  try {
    const apiCall = modal.value.type === 'line' 
      ? (modal.value.isEditing ? routesApi.updateLine(modal.value.data.id, modal.value.data) : routesApi.createLine(modal.value.data))
      : (modal.value.isEditing ? routesApi.updateShuttle(modal.value.data.id, modal.value.data) : routesApi.createShuttle(modal.value.data))
    
    await apiCall
    closeModal()
    fetchData()
  } catch (err) {
    console.error("Failed to save", err)
    alert("Failed to save changes.")
  }
}

const deleteLine = async (id) => {
  if(confirm("Delete this entire Bus Line? All stops will also be removed.")) {
    await routesApi.deleteLine(id)
    fetchData()
  }
}

const deleteShuttle = async (id) => {
  if(confirm("Delete this Shuttle route?")) {
    await routesApi.deleteShuttle(id)
    fetchData()
  }
}

// Stops Manager
const openStopsManager = (line) => {
  stopsManager.value = {
    show: true,
    lineId: line.id,
    lineName: line.name
  }
  fetchStops(line.id)
  
  // Predict next sequence
  const maxSeq = stops.value.reduce((max, s) => Math.max(max, s.sequence_number), 0)
  stopForm.value.sequence_number = maxSeq + 1
}

const closeStopsManager = () => {
  stopsManager.value.show = false
}

const fetchStops = async (lineId) => {
  stopsLoading.value = true
  try {
    const res = await routesApi.getStops({ line: lineId }) // Backend must support filtering by line
    let allStops = res.data.results || res.data
    // Filter client-side just in case backend query param isn't configured strictly
    stops.value = allStops.filter(s => s.line === lineId)
    
    const maxSeq = stops.value.reduce((max, s) => Math.max(max, s.sequence_number), 0)
    stopForm.value.sequence_number = maxSeq + 1
  } catch (err) {
    console.error("Failed to fetch stops", err)
  } finally {
    stopsLoading.value = false
  }
}

const submitStop = async () => {
  try {
    await routesApi.createStop({
      ...stopForm.value,
      line: stopsManager.value.lineId
    })
    // Reset form partially
    stopForm.value.name = ''
    stopForm.value.sequence_number++
    // Refresh stops
    fetchStops(stopsManager.value.lineId)
  } catch (err) {
    console.error("Failed to add stop", err)
    alert("Failed to add stop. Check required fields.")
  }
}

const deleteStop = async (id) => {
  if(confirm("Remove this stop from the sequence?")) {
    await routesApi.deleteStop(id)
    fetchStops(stopsManager.value.lineId)
  }
}

onMounted(() => {
  fetchData()
})
</script>
