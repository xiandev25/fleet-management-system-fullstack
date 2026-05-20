<template>
  <div class="space-y-8">
    
    <!-- Welcome Header -->
    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 bg-brand-asphalt-light p-6 rounded-2xl border border-brand-asphalt-lighter">
      <div>
        <h1 class="text-2xl font-black text-gray-50 uppercase tracking-wide">
          Guardian <span class="text-brand-highway-yellow">Console</span>
        </h1>
        <p class="text-xs font-semibold text-gray-400 uppercase tracking-widest mt-1">
          Monitor your children's transit schedules & billing status
        </p>
      </div>
      
      <!-- Quick Status -->
      <div class="flex items-center gap-2 px-4 py-2 bg-brand-asphalt rounded-xl border border-brand-asphalt-lighter text-xs font-bold uppercase tracking-wider text-gray-400">
        <svg class="w-4 h-4 text-brand-highway-yellow" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
        </svg>
        Assigned Services: <span class="text-status-go font-extrabold">{{ students.length }} Active</span>
      </div>
    </div>

    <!-- Children Transit Cards List -->
    <div class="space-y-5">
      <h3 class="text-xs font-black text-gray-400 uppercase tracking-widest">
        My Children's Transit Registry
      </h3>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        
        <!-- Individual Child Card -->
        <div 
          v-for="student in students" 
          :key="student.id" 
          class="bg-brand-asphalt-light rounded-2xl border border-brand-asphalt-lighter p-6 flex flex-col justify-between hover:border-brand-highway-yellow/20 transition duration-150 relative overflow-hidden"
        >
          <!-- Top section -->
          <div>
            <div class="flex items-start justify-between gap-4 mb-4">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-xl bg-brand-asphalt-lighter flex items-center justify-center border border-brand-highway-yellow/30 font-black text-brand-highway-yellow text-lg">
                  {{ student.first_name.slice(0, 1) }}{{ student.last_name.slice(0, 1) }}
                </div>
                <div>
                  <h4 class="font-extrabold text-gray-50 text-base leading-tight">{{ student.first_name }} {{ student.last_name }}</h4>
                  <span class="text-[10px] text-gray-400 font-bold uppercase tracking-wider block mt-0.5">Student Passenger</span>
                </div>
              </div>
              
              <!-- Route Assignment Status -->
              <span class="px-2.5 py-0.5 rounded-full text-[10px] font-extrabold uppercase tracking-wider border bg-brand-sign-blue-glow text-brand-sign-blue border-brand-sign-blue/20">
                Route Enrolled
              </span>
            </div>

            <!-- Route Stop Details (Resembling a physical highway sign) -->
            <div class="bg-brand-asphalt p-4 rounded-xl border border-brand-asphalt-lighter space-y-3">
              <div class="flex justify-between items-center text-xs">
                <span class="text-gray-400 font-bold uppercase tracking-wider">Boarding Station:</span>
                <span class="text-gray-100 font-extrabold uppercase">{{ student.bus_stop_details?.name || 'Bus Line Stop' }}</span>
              </div>
              <div class="flex justify-between items-center text-xs">
                <span class="text-gray-400 font-bold uppercase tracking-wider">Scheduled Departure:</span>
                <span class="text-brand-highway-yellow font-black font-mono">{{ student.bus_stop_details?.scheduled_time || '07:45 AM' }}</span>
              </div>
            </div>
          </div>

          <!-- Quick Route Overview map link placeholder -->
          <div class="mt-5 pt-4 border-t border-brand-asphalt-lighter flex justify-between items-center">
            <span class="text-[10px] text-gray-500 font-bold uppercase tracking-widest">School Transport Operations</span>
            <button class="text-xs font-bold text-brand-sign-blue hover:text-brand-sign-blue-hover flex items-center gap-1">
              Live Map
              <span class="text-sm">➔</span>
            </button>
          </div>
        </div>

        <div v-if="students.length === 0" class="col-span-full bg-brand-asphalt-light border border-brand-asphalt-lighter rounded-2xl p-8 text-center text-gray-500 font-semibold">
          No children registered under your family account. Contact administrator to update your profile.
        </div>

      </div>
    </div>

    <!-- Family Billing Grid -->
    <div class="bg-brand-asphalt-light rounded-2xl border border-brand-asphalt-lighter overflow-hidden">
      <!-- Billing Header -->
      <div class="px-6 py-5 border-b border-brand-asphalt-lighter bg-brand-asphalt/20">
        <h3 class="text-base font-extrabold text-gray-50 uppercase tracking-wide">
          Family Shared <span class="text-brand-highway-yellow">Accounting</span>
        </h3>
        <p class="text-xs text-gray-400 mt-0.5">Review payments due for your household transport service</p>
      </div>

      <!-- Invoices list -->
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr class="border-b border-brand-asphalt-lighter bg-brand-asphalt/40 text-[10px] font-extrabold text-gray-400 uppercase tracking-wider">
              <th class="px-6 py-4">Invoice ID</th>
              <th class="px-6 py-4">Total Amount</th>
              <th class="px-6 py-4">Due Date</th>
              <th class="px-6 py-4">Payment Status</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-brand-asphalt-lighter text-sm">
            <tr 
              v-for="invoice in invoices" 
              :key="invoice.id" 
              class="hover:bg-brand-asphalt/10 transition duration-150"
            >
              <td class="px-6 py-4 font-mono font-bold text-gray-300">
                #{{ invoice.invoice_number || `INV-${invoice.id}` }}
              </td>
              <td class="px-6 py-4 font-extrabold text-gray-100">
                ${{ Number(invoice.total_amount).toFixed(2) }}
              </td>
              <td class="px-6 py-4 font-medium text-gray-400 font-mono">
                {{ invoice.due_date }}
              </td>
              <td class="px-6 py-4">
                <span 
                  class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold uppercase tracking-wider border"
                  :class="paymentStatusClass(invoice.status)"
                >
                  {{ invoice.status }}
                </span>
              </td>
            </tr>
            <tr v-if="invoices.length === 0">
              <td colspan="4" class="text-center py-8 text-gray-500 font-semibold">
                No active invoices found for your household.
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../api/axios'

const students = ref([])
const invoices = ref([])

const fetchData = async () => {
  try {
    // Fetch students registered under this family
    const studentsRes = await api.get('clients/students/')
    students.value = studentsRes.data

    // Fetch invoices assigned to the guardian's family
    const invoicesRes = await api.get('billing/invoices/')
    invoices.value = invoicesRes.data
  } catch (err) {
    console.error('Error fetching Guardian console telemetry:', err)
  }
}

const paymentStatusClass = (status) => {
  switch (status) {
    case 'PAID':
      return 'bg-status-go/10 text-status-go border-status-go/20'
    case 'PARTIALLY_PAID':
      return 'bg-status-caution/10 text-status-caution border-status-caution/20'
    default:
      return 'bg-status-stop/10 text-status-stop border-status-stop/20'
  }
}

onMounted(() => {
  fetchData()
})
</script>
