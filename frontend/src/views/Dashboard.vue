<template>
  <div class="dashboard-view-wrapper">
    <ManagerDashboard />
  </div>
</template>

<script setup>
import ManagerDashboard from '../components/ManagerDashboard.vue'
</script>

<style scoped>
.dashboard-view-wrapper {
  animation: fadeIn 0.25s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(4px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
