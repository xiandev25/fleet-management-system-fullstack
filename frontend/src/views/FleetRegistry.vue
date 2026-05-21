<template>
  <div class="h-full flex flex-col">

    <!-- Page Header -->
    <header class="flex items-center justify-between mb-6">
      <div>
        <h1 class="text-2xl font-extrabold tracking-wider text-gray-50 uppercase">
          Fleet <span class="text-brand-highway-yellow">Registry</span>
        </h1>
        <p class="text-xs font-semibold tracking-widest text-gray-400 uppercase mt-1">
          Motor assets &amp; lifecycle management
        </p>
      </div>
      <button
        id="btn-register-bus"
        @click="openCreateModal"
        class="flex items-center gap-2 px-5 py-2.5 bg-brand-highway-yellow hover:bg-brand-highway-yellow-hover text-brand-asphalt font-bold text-xs uppercase tracking-wider rounded-xl transition-all shadow-md"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
        </svg>
        Register Bus
      </button>
    </header>

    <!-- Table Container -->
    <div class="bg-brand-asphalt-light border border-brand-asphalt-lighter rounded-2xl flex-grow flex flex-col overflow-hidden shadow-lg">

      <!-- Loading State -->
      <div v-if="loading" class="flex-grow flex items-center justify-center">
        <svg class="animate-spin h-8 w-8 text-brand-highway-yellow" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
      </div>

      <!-- Data Table -->
      <div v-else class="overflow-x-auto flex-grow">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr class="border-b border-brand-asphalt-lighter bg-brand-asphalt/40">
              <th class="px-5 py-3.5 text-xs font-black tracking-widest text-brand-highway-yellow uppercase">License Plate</th>
              <th class="px-5 py-3.5 text-xs font-black tracking-widest text-brand-highway-yellow uppercase">Make &amp; Model</th>
              <th class="px-5 py-3.5 text-xs font-black tracking-widest text-brand-highway-yellow uppercase">Year</th>
              <th class="px-5 py-3.5 text-xs font-black tracking-widest text-brand-highway-yellow uppercase">Mileage</th>
              <th class="px-5 py-3.5 text-xs font-black tracking-widest text-brand-highway-yellow uppercase">Status</th>
              <th class="px-5 py-3.5 text-xs font-black tracking-widest text-brand-highway-yellow uppercase text-right">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="vehicle in vehicles"
              :key="vehicle.id"
              class="border-b border-brand-asphalt-lighter hover:bg-brand-asphalt/30 transition-colors"
            >
              <td class="px-5 py-4 font-bold text-sm text-brand-highway-yellow">{{ vehicle.license_plate }}</td>
              <td class="px-5 py-4 font-semibold text-sm text-gray-200">{{ vehicle.brand }} {{ vehicle.model }}</td>
              <td class="px-5 py-4 text-sm text-gray-400 font-medium">{{ vehicle.manufacture_year }}</td>
              <td class="px-5 py-4 text-sm text-gray-400 font-medium">{{ vehicle.current_mileage.toLocaleString() }} KM</td>
              <td class="px-5 py-4">
                <span
                  class="px-2 py-1 text-[10px] font-black uppercase tracking-widest rounded-md"
                  :class="getStatusClass(vehicle.status)"
                >
                  {{ vehicle.status.replace(/_/g, ' ') }}
                </span>
              </td>
              <td class="px-5 py-4 text-right space-x-3">
                <button @click="openEditModal(vehicle)" title="Edit vehicle" class="text-brand-sign-blue hover:text-brand-sign-blue-hover transition-colors">
                  <svg class="w-5 h-5 inline-block" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
                  </svg>
                </button>
                <button @click="handleDelete(vehicle.id)" title="Delete vehicle" class="text-status-stop hover:text-red-400 transition-colors">
                  <svg class="w-5 h-5 inline-block" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                  </svg>
                </button>
              </td>
            </tr>
            <tr v-if="!loading && vehicles.length === 0">
              <td colspan="6" class="px-6 py-14 text-center text-sm text-gray-500 font-medium italic">
                No vehicles found in the registry.
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Pagination Footer -->
      <div v-if="totalCount > 0" class="px-6 py-4 border-t border-brand-asphalt-lighter bg-brand-asphalt/40 flex items-center justify-between">
        <span class="text-xs font-bold text-gray-500 tracking-wider">
          Total Fleet: <span class="text-gray-200">{{ totalCount }}</span>
        </span>
        <div class="flex items-center gap-2">
          <button
            @click="fetchVehicles(currentPage - 1)"
            :disabled="!hasPrevious"
            class="p-1.5 rounded-lg border border-brand-asphalt-lighter text-gray-400 disabled:opacity-30 hover:bg-brand-asphalt-lighter transition-colors"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
            </svg>
          </button>
          <span class="text-xs font-bold text-gray-300 mx-2">Page {{ currentPage }}</span>
          <button
            @click="fetchVehicles(currentPage + 1)"
            :disabled="!hasNext"
            class="p-1.5 rounded-lg border border-brand-asphalt-lighter text-gray-400 disabled:opacity-30 hover:bg-brand-asphalt-lighter transition-colors"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Create / Edit Modal -->
    <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-brand-asphalt/80 backdrop-blur-sm">
      <div class="bg-brand-asphalt-light border border-brand-asphalt-lighter rounded-2xl w-full max-w-2xl shadow-2xl overflow-hidden flex flex-col max-h-[90vh]">

        <!-- Modal Header -->
        <div class="px-6 py-4 border-b border-brand-asphalt-lighter flex justify-between items-center bg-brand-asphalt/40">
          <h3 class="text-base font-extrabold uppercase tracking-widest text-gray-50">
            {{ isEditing ? 'Update Vehicle Details' : 'Register New Vehicle' }}
          </h3>
          <button @click="closeModal" class="text-gray-400 hover:text-gray-200 transition-colors">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <!-- Modal Form -->
        <div class="p-6 overflow-y-auto">
          <form id="vehicleForm" @submit.prevent="submitForm" class="grid grid-cols-1 md:grid-cols-2 gap-5">
            <div>
              <label class="block text-xs font-bold text-gray-400 uppercase tracking-widest mb-1.5">License Plate</label>
              <input v-model="formData.license_plate" required class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow" placeholder="e.g. LT-123-XY" />
            </div>
            <div>
              <label class="block text-xs font-bold text-gray-400 uppercase tracking-widest mb-1.5">Immatriculation No.</label>
              <input v-model="formData.immatriculation_number" class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow" placeholder="Optional" />
            </div>
            <div>
              <label class="block text-xs font-bold text-gray-400 uppercase tracking-widest mb-1.5">Brand</label>
              <input v-model="formData.brand" required class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow" placeholder="e.g. Toyota" />
            </div>
            <div>
              <label class="block text-xs font-bold text-gray-400 uppercase tracking-widest mb-1.5">Model</label>
              <input v-model="formData.model" required class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow" placeholder="e.g. Coaster" />
            </div>
            <div>
              <label class="block text-xs font-bold text-gray-400 uppercase tracking-widest mb-1.5">Manufacture Year</label>
              <input v-model.number="formData.manufacture_year" type="number" required class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow" placeholder="2018" />
            </div>
            <div>
              <label class="block text-xs font-bold text-gray-400 uppercase tracking-widest mb-1.5">Current Mileage (KM)</label>
              <input v-model.number="formData.current_mileage" type="number" required class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow" placeholder="0" />
            </div>
            <div class="md:col-span-2">
              <label class="block text-xs font-bold text-gray-400 uppercase tracking-widest mb-1.5">Operational Status</label>
              <select v-model="formData.status" required class="w-full px-3 py-2.5 bg-brand-asphalt border border-brand-asphalt-lighter rounded-xl text-sm focus:outline-none focus:border-brand-highway-yellow">
                <option value="AVAILABLE">Available</option>
                <option value="IN_USE">In Use</option>
                <option value="IN_MAINTENANCE">In Maintenance</option>
                <option value="IN_REPAIR">In Repair</option>
                <option value="REFUELLING">Refuelling</option>
                <option value="SPECIAL_ASSIGNMENT">Special Assignment</option>
                <option value="RETIRED">Retired</option>
              </select>
            </div>
          </form>
        </div>

        <!-- Modal Footer -->
        <div class="px-6 py-4 border-t border-brand-asphalt-lighter bg-brand-asphalt/40 flex justify-end gap-3">
          <button @click="closeModal" class="px-4 py-2 text-sm font-bold tracking-wider uppercase text-gray-400 hover:text-gray-200 transition-colors">
            Cancel
          </button>
          <button form="vehicleForm" type="submit" class="px-5 py-2.5 bg-brand-highway-yellow hover:bg-brand-highway-yellow-hover text-brand-asphalt font-bold text-xs uppercase tracking-wider rounded-xl transition-all shadow-md">
            {{ isEditing ? 'Save Changes' : 'Register Vehicle' }}
          </button>
        </div>

      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import fleetApi from '../api/fleet'

const vehicles = ref([])
const loading = ref(false)
const totalCount = ref(0)
const currentPage = ref(1)
const hasNext = ref(false)
const hasPrevious = ref(false)

const showModal = ref(false)
const isEditing = ref(false)
const editingId = ref(null)

const defaultForm = {
  license_plate: '',
  immatriculation_number: '',
  brand: '',
  model: '',
  manufacture_year: new Date().getFullYear(),
  status: 'AVAILABLE',
  current_mileage: 0
}
const formData = ref({ ...defaultForm })

const fetchVehicles = async (page = 1) => {
  loading.value = true
  try {
    const res = await fleetApi.getVehicles({ page })
    if (res.data && res.data.results !== undefined) {
      vehicles.value = res.data.results
      totalCount.value = res.data.count
      hasNext.value = !!res.data.next
      hasPrevious.value = !!res.data.previous
    } else {
      vehicles.value = res.data
      totalCount.value = res.data.length
    }
    currentPage.value = page
  } catch (err) {
    console.error('Failed to fetch vehicles:', err)
  } finally {
    loading.value = false
  }
}

const getStatusClass = (status) => {
  switch (status) {
    case 'AVAILABLE':          return 'bg-status-go/20 text-status-go border border-status-go/30'
    case 'IN_USE':             return 'bg-brand-sign-blue/20 text-brand-sign-blue border border-brand-sign-blue/30'
    case 'IN_MAINTENANCE':
    case 'REFUELLING':         return 'bg-brand-highway-yellow/20 text-brand-highway-yellow border border-brand-highway-yellow/30'
    case 'IN_REPAIR':          return 'bg-status-stop/20 text-status-stop border border-status-stop/30'
    default:                   return 'bg-gray-500/20 text-gray-400 border border-gray-500/30'
  }
}

const openCreateModal = () => {
  isEditing.value = false
  editingId.value = null
  formData.value = { ...defaultForm }
  showModal.value = true
}

const openEditModal = (vehicle) => {
  isEditing.value = true
  editingId.value = vehicle.id
  formData.value = { ...vehicle }
  showModal.value = true
}

const closeModal = () => { showModal.value = false }

const submitForm = async () => {
  try {
    if (isEditing.value) {
      await fleetApi.updateVehicle(editingId.value, formData.value)
    } else {
      await fleetApi.createVehicle(formData.value)
    }
    closeModal()
    fetchVehicles(currentPage.value)
  } catch (err) {
    console.error('Form submission failed', err)
    alert('Failed to save vehicle. Please check the inputs.')
  }
}

const handleDelete = async (id) => {
  if (confirm('Remove this vehicle from the registry?')) {
    try {
      await fleetApi.deleteVehicle(id)
      fetchVehicles(currentPage.value)
    } catch (err) {
      console.error('Deletion failed', err)
    }
  }
}

onMounted(() => fetchVehicles())
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
