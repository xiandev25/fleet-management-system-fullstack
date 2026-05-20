import api from './axios'

export default {
  /**
   * Vehicle (Bus) API endpoints
   */
  getVehicles(params = {}) {
    return api.get('fleet/vehicles/', { params })
  },
  
  getVehicle(id) {
    return api.get(`fleet/vehicles/${id}/`)
  },
  
  createVehicle(data) {
    return api.post('fleet/vehicles/', data)
  },
  
  updateVehicle(id, data) {
    return api.put(`fleet/vehicles/${id}/`, data)
  },
  
  patchVehicle(id, data) {
    return api.patch(`fleet/vehicles/${id}/`, data)
  },
  
  deleteVehicle(id) {
    return api.delete(`fleet/vehicles/${id}/`)
  },

  /**
   * Maintenance Log API endpoints
   */
  getMaintenanceLogs(vehicleId = null) {
    const params = vehicleId ? { vehicle: vehicleId } : {}
    return api.get('fleet/maintenance/', { params })
  },

  createMaintenanceLog(data) {
    return api.post('fleet/maintenance/', data)
  }
}
