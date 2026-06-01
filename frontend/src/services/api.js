/**
 * API Service Module
 * Handles all HTTP requests to the backend API
 */

import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'https://inventory-management-system-production-760b.up.railway.app';
const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Error handling interceptor
apiClient.interceptors.response.use(
  response => response,
  error => {
    console.error('API Error:', error);
    return Promise.reject(error);
  }
);

/**
 * Products API
 */
export const productsAPI = {
  getAll: (skip = 0, limit = 100) => 
    apiClient.get(`/products?skip=${skip}&limit=${limit}`),
  
  getById: (id) => 
    apiClient.get(`/products/${id}`),
  
  create: (data) => 
    apiClient.post('/products', data),
  
  update: (id, data) => 
    apiClient.put(`/products/${id}`, data),
  
  delete: (id) => 
    apiClient.delete(`/products/${id}`)
};

/**
 * Customers API
 */
export const customersAPI = {
  getAll: (skip = 0, limit = 100) => 
    apiClient.get(`/customers?skip=${skip}&limit=${limit}`),
  
  getById: (id) => 
    apiClient.get(`/customers/${id}`),
  
  create: (data) => 
    apiClient.post('/customers', data),
  
  update: (id, data) => 
    apiClient.put(`/customers/${id}`, data),
  
  delete: (id) => 
    apiClient.delete(`/customers/${id}`)
};

/**
 * Orders API
 */
export const ordersAPI = {
  getAll: (skip = 0, limit = 100) => 
    apiClient.get(`/orders?skip=${skip}&limit=${limit}`),
  
  getById: (id) => 
    apiClient.get(`/orders/${id}`),
  
  create: (data) => 
    apiClient.post('/orders', data),
  
  getDashboardStats: () => 
    apiClient.get('/orders/stats/dashboard')
};

export default apiClient;
