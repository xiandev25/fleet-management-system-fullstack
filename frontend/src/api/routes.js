import api from './axios'

export default {
  /**
   * Bus Lines API endpoints
   */
  getLines(params = {}) {
    return api.get('routes/lines/', { params })
  },
  getLine(id) {
    return api.get(`routes/lines/${id}/`)
  },
  createLine(data) {
    return api.post('routes/lines/', data)
  },
  updateLine(id, data) {
    return api.put(`routes/lines/${id}/`, data)
  },
  deleteLine(id) {
    return api.delete(`routes/lines/${id}/`)
  },

  /**
   * Bus Stops API endpoints
   */
  getStops(params = {}) {
    return api.get('routes/stops/', { params })
  },
  getStop(id) {
    return api.get(`routes/stops/${id}/`)
  },
  createStop(data) {
    return api.post('routes/stops/', data)
  },
  updateStop(id, data) {
    return api.put(`routes/stops/${id}/`, data)
  },
  deleteStop(id) {
    return api.delete(`routes/stops/${id}/`)
  },

  /**
   * Shuttles API endpoints
   */
  getShuttles(params = {}) {
    return api.get('routes/shuttles/', { params })
  },
  getShuttle(id) {
    return api.get(`routes/shuttles/${id}/`)
  },
  createShuttle(data) {
    return api.post('routes/shuttles/', data)
  },
  updateShuttle(id, data) {
    return api.put(`routes/shuttles/${id}/`, data)
  },
  deleteShuttle(id) {
    return api.delete(`routes/shuttles/${id}/`)
  }
}
