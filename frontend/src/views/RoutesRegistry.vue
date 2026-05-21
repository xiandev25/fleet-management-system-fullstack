<template>
  <div class="h-full flex flex-col relative">

    <!-- Page Header & Tabs -->
    <header class="flex flex-col md:flex-row md:items-end justify-between mb-6 gap-4">
      <div>
        <h1 class="text-2xl font-extrabold tracking-wider text-gray-50 uppercase">
          Routes <span class="text-brand-highway-yellow">Network</span>
        </h1>
        <p class="text-xs font-semibold tracking-widest text-gray-400 uppercase mt-1">
          Manage bus lines, stops &amp; shuttles
        </p>
      </div>

      <!-- Tab Navigation -->
      <div class="flex p-1 bg-brand-asphalt-lighter rounded-xl self-start md:self-auto">
        <button
          @click="activeTab = 'lines'"
          class="px-5 py-2 text-xs font-bold uppercase tracking-wider rounded-lg transition-colors"
          :class="activeTab === 'lines' ? 'bg-brand-highway-yellow text-brand-asphalt shadow-sm' : 'text-gray-400 hover:text-gray-200'"
        >
          Bus Lines
        </button>
        <button
          @click="activeTab = 'shuttles'"
          class="px-5 py-2 text-xs font-bold uppercase tracking-wider rounded-lg transition-colors"
          :class="activeTab === 'shuttles' ? 'bg-brand-highway-yellow text-brand-asphalt shadow-sm' : 'text-gray-400 hover:text-gray-200'"
        >
          Shuttles
        </button>
      </div>
    </header>

    <!-- Main Container -->
    <div class="bg-brand-asphalt-light border border-brand-asphalt-lighter rounded-2xl flex-grow flex flex-col overflow-hidden shadow-lg">

      <!-- Action Bar -->
      <div class="px-6 py-4 border-b border-brand-asphalt-lighter flex justify-between items-center bg-brand-asphalt/40">
        <h2 class="font-extrabold tracking-widest text-brand-highway-yellow uppercase text-xs">
          {{ activeTab === 'lines' ? 'Active Bus Lines' : 'Active Shuttles' }}
        </h2>
        <button
          :id="activeTab === 'lines' ? 'btn-add-line' : 'btn-add-shuttle'"
          @click="activeTab === 'lines' ? openLineModal() : openShuttleModal()"
          class="flex items-center gap-2 px-4 py-2 bg-brand-highway-yellow hover:bg-brand-highway-yellow-hover text-brand-asphalt font-bold text-xs uppercase tracking-wider rounded-xl transition-all shadow-md"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
          </svg>
          Add {{ activeTab === 'lines' ? 'Line' : 'Shuttle' }}
        </button>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="flex-grow flex items-center justify-center">
        <svg class="animate-spin h-8 w-8 text-brand-highway-yellow" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
      </div>

      <!-- BUS LINES TABLE -->
      <div v-else-if="activeTab === 'lines'" class="overflow-x-auto flex-grow">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr class="border-b border-brand-asphalt-lighter bg-brand-asphalt/40">
              <th class="px-5 py-3.5 text-xs font-black tracking-widest text-brand-highway-yellow uppercase">Line Name</th>
              <th class="px-5 py-3.5 text-xs font-black tracking-widest text-brand-highway-yellow uppercase">Description</th>
              <th class="px-5 py-3.5 text-xs font-black tracking-widest text-brand-highway-yellow uppercase text-right">Routing &amp; Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="line in lines" :key="line.id" class="border-b border-brand-asphalt-lighter hover:bg-brand-asphalt/30 transition-colors">
              <td class="px-5 py-4 font-bold text-sm text-brand-highway-yellow">{{ line.name }}</td>
              <td class="px-5 py-4 text-sm text-gray-400 font-medium">{{ line.description || 'No description provided.' }}</td>
              <td class="px-5 py-4 text-right space-x-2 flex items-center justify-end gap-2">
                <button
                  @click="openStopsManager(line)"
                  class="inline-flex items-center gap-1.5 font-bold text-[10px] uppercase tracking-wider bg-brand-highway-yellow/10 text-brand-highway-yellow px-3 py-1.5 rounded-lg border border-brand-highway-yellow/30 hover:bg-brand-highway-yellow/20 transition-colors"
                >
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
                  </svg>
                  Manage Stops
                </button>
                <button @click="openLineModal(line)" class="text-brand-sign-blue hover:text-brand-sign-blue-hover transition-colors">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" /></svg>
                </button>
                <button @click="deleteLine(line.id)" class="text-status-stop hover:text-red-400 transition-colors">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
                </button>
              </td>
            </tr>
            <tr v-if="lines.length === 0">
              <td colspan="3" class="px-6 py-14 text-center text-sm text-gray-500 font-medium italic">No bus lines established yet.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- SHUTTLES TABLE -->
      <div v-else-if="activeTab === 'shuttles'" class="overflow-x-auto flex-grow">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr class="border-b border-brand-asphalt-lighter bg-brand-asphalt/40">
              <th class="px-5 py-3.5 text-xs font-black tracking-widest text-brand-highway-yellow uppercase">Shuttle Name</th>
              <th class="px-5 py-3.5 text-xs font-black tracking-widest text-brand-highway-yellow uppercase">Pickup Point</th>
              <th class="px-5 py-3.5 text-xs font-black tracking-widest text-brand-highway-yellow uppercase">Scheduled Time</th>
              <th class="px-5 py-3.5 text-xs font-black tracking-widest text-brand-highway-yellow uppercase text-right">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="shuttle in shuttles" :key="shuttle.id" class="border-b border-brand-asphalt-lighter hover:bg-brand-asphalt/30 transition-colors">
              <td class="px-5 py-4 font-bold text-sm text-brand-highway-yellow">{{ shuttle.name }}</td>
              <td class="px-5 py-4 text-sm text-gray-200 font-medium">{{ shuttle.pickup_point }}</td>
              <td class="px-5 py-4 text-sm text-gray-400 font-medium">{{ formatTime(shuttle.scheduled_time) }}</td>
              <td class="px-5 py-4 text-right space-x-3">
                <button @click="openShuttleModal(shuttle)" class="text-brand-sign-blue hover:text-brand-sign-blue-hover transition-colors">
                  <svg class="w-5 h-5 inline-block" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" /></svg>
                </button>
                <button @click="deleteShuttle(shuttle.id)" class="text-status-stop hover:text-red-400 transition-colors">
                  <svg class="w-5 h-5 inline-block" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
                </button>
              </td>
            </tr>
            <tr v-if="shuttles.length === 0">
              <td colspan="4" class="px-6 py-14 text-center text-sm text-gray-500 font-medium italic">No shuttles established yet.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- MODAL: Line / Shuttle CRUD -->
    <div v-if="modal.show" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-brand-asphalt/80 backdrop-blur-sm">
      <div class="bg-brand-asphalt-light border border-brand-asphalt-lighter rounded-2xl w-full max-w-lg shadow-2xl overflow-hidden flex flex-col">
        <div class="px-6 py-4 border-b border-brand-asphalt-lighter flex justify-between items-center bg-brand-asphalt/40">
          <h3 class="text-base font-extrabold uppercase tracking-widest text-gray-50">
            {{ modal.isEditing ? 'Update' : 'Create' }} {{ modal.type === 'line' ? 'Bus Line' : 'Shuttle' }}
          </h3>
          <button @click="closeModal" class="text-gray-400 hover:text-gray-200 transition-colors">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
          </button>
        </div>
        <div class="p-6">
          <form id="resourceForm" @submit.prevent="submitModalForm" class="space-y-4">
            <div>
              <label class="block text-xs font-bold text-gray-400 uppercase tracking-widest mb-1.5">Name</label>
              <input v-model="modal.data.name" required class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow" placeholder="e.g. Line A — North Circuit" />
            </div>
            <template v-if="modal.type === 'shuttle'">
              <div>
                <label class="block text-xs font-bold text-gray-400 uppercase tracking-widest mb-1.5">Pickup Point</label>
                <input v-model="modal.data.pickup_point" required class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow" placeholder="Location name" />
              </div>
              <div>
                <label class="block text-xs font-bold text-gray-400 uppercase tracking-widest mb-1.5">Scheduled Time</label>
                <input v-model="modal.data.scheduled_time" type="time" required class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow" />
              </div>
            </template>
            <div>
              <label class="block text-xs font-bold text-gray-400 uppercase tracking-widest mb-1.5">Description (optional)</label>
              <textarea v-model="modal.data.description" rows="3" class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow"></textarea>
            </div>
          </form>
        </div>
        <div class="px-6 py-4 border-t border-brand-asphalt-lighter bg-brand-asphalt/40 flex justify-end gap-3">
          <button @click="closeModal" class="px-4 py-2 text-sm font-bold tracking-wider uppercase text-gray-400 hover:text-gray-200 transition-colors">Cancel</button>
          <button form="resourceForm" type="submit" class="px-5 py-2.5 bg-brand-highway-yellow hover:bg-brand-highway-yellow-hover text-brand-asphalt font-bold text-xs uppercase tracking-wider rounded-xl shadow-md transition-all">Save</button>
        </div>
      </div>
    </div>

    <!-- STOPS MANAGER SLIDE-OVER -->
    <div v-if="stopsManager.show" class="fixed inset-0 z-[60] flex justify-end bg-brand-asphalt/60 backdrop-blur-sm">
      <div class="w-full max-w-2xl bg-brand-asphalt-light border-l border-brand-asphalt-lighter h-full shadow-2xl flex flex-col">

        <!-- Panel Header -->
        <div class="px-6 py-5 border-b border-brand-asphalt-lighter flex justify-between items-center bg-brand-asphalt/80">
          <div>
            <h2 class="text-base font-extrabold uppercase tracking-widest text-gray-50">Route Stop Sequence</h2>
            <p class="text-xs font-bold tracking-widest text-brand-highway-yellow uppercase mt-1">
              Line: {{ stopsManager.lineName }}
            </p>
          </div>
          <button @click="closeStopsManager" class="text-gray-400 hover:text-gray-200 p-2 rounded-lg bg-brand-asphalt hover:bg-brand-asphalt-lighter border border-brand-asphalt-lighter transition-colors">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
          </button>
        </div>

        <!-- Quick-Add Stop Form -->
        <div class="p-5 border-b border-brand-asphalt-lighter bg-brand-asphalt/40">
          <p class="text-[10px] font-black text-gray-400 uppercase tracking-widest mb-3">Add New Stop</p>
          <form @submit.prevent="submitStop" class="grid grid-cols-2 md:grid-cols-4 gap-3 items-end">
            <div>
              <label class="block text-[10px] font-bold text-gray-500 uppercase tracking-widest mb-1">Seq #</label>
              <input v-model.number="stopForm.sequence_number" type="number" min="1" required class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow text-sm" />
            </div>
            <div>
              <label class="block text-[10px] font-bold text-gray-500 uppercase tracking-widest mb-1">Time</label>
              <input v-model="stopForm.scheduled_time" type="time" required class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow text-sm" />
            </div>
            <div class="col-span-2">
              <label class="block text-[10px] font-bold text-gray-500 uppercase tracking-widest mb-1">Stop Name</label>
              <div class="flex gap-2">
                <input v-model="stopForm.name" required class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow text-sm flex-grow" placeholder="e.g. Main Gate" />
                <button type="submit" class="px-4 py-2 bg-brand-highway-yellow hover:bg-brand-highway-yellow-hover text-brand-asphalt font-bold text-xs uppercase tracking-wider rounded-xl shadow-md transition-all flex-shrink-0">Add</button>
              </div>
            </div>
          </form>
        </div>

        <!-- Stops Timeline -->
        <div class="flex-grow overflow-y-auto p-5">
          <div v-if="stopsLoading" class="text-center py-8 text-sm text-brand-highway-yellow">Loading sequence...</div>
          <div v-else-if="stops.length === 0" class="text-center py-12 text-sm text-gray-500 italic font-medium">
            No stops defined for this line yet.
          </div>
          <div v-else class="space-y-3">
            <div
              v-for="stop in sortedStops"
              :key="stop.id"
              class="flex items-center gap-4 bg-brand-asphalt p-4 rounded-xl border border-brand-asphalt-lighter"
            >
              <!-- Sequence Badge -->
              <div class="flex flex-col items-center justify-center w-11 h-11 rounded-lg bg-brand-asphalt-lighter border border-brand-asphalt-lighter flex-shrink-0">
                <span class="text-[9px] text-gray-400 font-bold uppercase leading-none">Stop</span>
                <span class="text-base font-black text-brand-highway-yellow leading-tight">{{ stop.sequence_number }}</span>
              </div>
              <!-- Stop Info -->
              <div class="flex-grow">
                <p class="text-sm font-bold text-gray-100">{{ stop.name }}</p>
                <p class="text-xs text-gray-400 font-medium flex items-center gap-1 mt-0.5">
                  <svg class="w-3 h-3" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                  {{ formatTime(stop.scheduled_time) }}
                </p>
              </div>
              <!-- Delete -->
              <button @click="deleteStop(stop.id)" class="text-status-stop hover:bg-status-stop/10 p-2 rounded-lg transition-colors flex-shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
              </button>
            </div>
          </div>
        </div>

      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import routesApi from '../api/routes'

const activeTab = ref('lines')
const loading = ref(false)
const lines = ref([])
const shuttles = ref([])

const modal = ref({ show: false, type: 'line', isEditing: false, data: {} })

const stopsManager = ref({ show: false, lineId: null, lineName: '' })
const stops = ref([])
const stopsLoading = ref(false)

const stopForm = ref({ sequence_number: 1, scheduled_time: '07:00', name: '' })

const sortedStops = computed(() =>
  [...stops.value].sort((a, b) => a.sequence_number - b.sequence_number)
)

const formatTime = (t) => (t ? t.substring(0, 5) : '--:--')

const fetchData = async () => {
  loading.value = true
  try {
    const [linesRes, shuttlesRes] = await Promise.all([
      routesApi.getLines(),
      routesApi.getShuttles()
    ])
    lines.value = linesRes.data.results ?? linesRes.data
    shuttles.value = shuttlesRes.data.results ?? shuttlesRes.data
  } catch (err) {
    console.error('Failed to fetch routes data', err)
  } finally {
    loading.value = false
  }
}

const openLineModal = (line = null) => {
  modal.value = { show: true, type: 'line', isEditing: !!line, data: line ? { ...line } : { name: '', description: '' } }
}
const openShuttleModal = (shuttle = null) => {
  modal.value = { show: true, type: 'shuttle', isEditing: !!shuttle, data: shuttle ? { ...shuttle } : { name: '', pickup_point: '', scheduled_time: '07:00', description: '' } }
}
const closeModal = () => { modal.value.show = false }

const submitModalForm = async () => {
  try {
    const { type, isEditing, data } = modal.value
    if (type === 'line') {
      isEditing ? await routesApi.updateLine(data.id, data) : await routesApi.createLine(data)
    } else {
      isEditing ? await routesApi.updateShuttle(data.id, data) : await routesApi.createShuttle(data)
    }
    closeModal()
    fetchData()
  } catch (err) {
    console.error('Failed to save', err)
    alert('Failed to save changes.')
  }
}

const deleteLine = async (id) => {
  if (confirm('Delete this Bus Line? All stops will be removed.')) {
    await routesApi.deleteLine(id)
    fetchData()
  }
}
const deleteShuttle = async (id) => {
  if (confirm('Delete this Shuttle route?')) {
    await routesApi.deleteShuttle(id)
    fetchData()
  }
}

const openStopsManager = (line) => {
  stopsManager.value = { show: true, lineId: line.id, lineName: line.name }
  fetchStops(line.id)
}
const closeStopsManager = () => { stopsManager.value.show = false }

const fetchStops = async (lineId) => {
  stopsLoading.value = true
  try {
    const res = await routesApi.getStops({ line: lineId })
    const all = res.data.results ?? res.data
    stops.value = all.filter(s => s.line === lineId)
    stopForm.value.sequence_number = stops.value.length + 1
  } catch (err) {
    console.error('Failed to fetch stops', err)
  } finally {
    stopsLoading.value = false
  }
}

const submitStop = async () => {
  try {
    await routesApi.createStop({ ...stopForm.value, line: stopsManager.value.lineId })
    stopForm.value.name = ''
    stopForm.value.sequence_number++
    fetchStops(stopsManager.value.lineId)
  } catch (err) {
    console.error('Failed to add stop', err)
    alert('Failed to add stop.')
  }
}

const deleteStop = async (id) => {
  if (confirm('Remove this stop from the sequence?')) {
    await routesApi.deleteStop(id)
    fetchStops(stopsManager.value.lineId)
  }
}

onMounted(fetchData)
</script>

<style scoped>
.form-input {
  width: 100%;
  padding: 0.5rem 0.75rem;
  background-color: var(--brand-asphalt);
  border: 1px solid var(--brand-asphalt-lighter);
  border-radius: 0.75rem;
  color: #f0fdf4;
  font-size: 0.875rem;
  font-weight: 500;
  outline: none;
  transition: border-color 0.2s;
}
.form-input:focus {
  border-color: var(--brand-accent-amber);
}
.form-input::placeholder {
  color: #6b7280;
}
</style>
