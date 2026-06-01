import { useEffect, useState } from 'react'
import { ordersAPI, customersAPI, productsAPI } from '../services/api'

export default function Orders() {
  const [orders, setOrders] = useState([])
  const [customers, setCustomers] = useState([])
  const [products, setProducts] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [showForm, setShowForm] = useState(false)
  const [formData, setFormData] = useState({
    customer_id: '',
    items: [{ product_id: '', quantity: '' }]
  })

  useEffect(() => {
    fetchData()
  }, [])

  const fetchData = async () => {
    try {
      setLoading(true)
      const [ordersRes, customersRes, productsRes] = await Promise.all([
        ordersAPI.getAll(),
        customersAPI.getAll(),
        productsAPI.getAll()
      ])
      setOrders(ordersRes.data)
      setCustomers(customersRes.data)
      setProducts(productsRes.data)
    } catch (err) {
      setError('Failed to load data')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  const handleCustomerChange = (e) => {
    setFormData(prev => ({
      ...prev,
      customer_id: parseInt(e.target.value)
    }))
  }

  const handleProductChange = (index, value) => {
    const newItems = [...formData.items]
    newItems[index].product_id = parseInt(value)
    setFormData(prev => ({
      ...prev,
      items: newItems
    }))
  }

  const handleQuantityChange = (index, value) => {
    const newItems = [...formData.items]
    newItems[index].quantity = parseInt(value)
    setFormData(prev => ({
      ...prev,
      items: newItems
    }))
  }

  const handleAddItem = () => {
    setFormData(prev => ({
      ...prev,
      items: [...prev.items, { product_id: '', quantity: '' }]
    }))
  }

  const handleRemoveItem = (index) => {
    setFormData(prev => ({
      ...prev,
      items: prev.items.filter((_, i) => i !== index)
    }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      if (!formData.customer_id || formData.items.some(item => !item.product_id || !item.quantity)) {
        setError('Please fill in all fields')
        return
      }

      await ordersAPI.create({
        customer_id: formData.customer_id,
        items: formData.items.map(item => ({
          product_id: item.product_id,
          quantity: item.quantity
        }))
      })
      
      await fetchData()
      setShowForm(false)
      setFormData({
        customer_id: '',
        items: [{ product_id: '', quantity: '' }]
      })
      setError(null)
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to create order')
      console.error(err)
    }
  }

  const handleCancel = () => {
    setShowForm(false)
    setFormData({
      customer_id: '',
      items: [{ product_id: '', quantity: '' }]
    })
    setError(null)
  }

  const getCustomerName = (id) => {
    return customers.find(c => c.id === id)?.name || 'Unknown'
  }

  const getProductName = (id) => {
    return products.find(p => p.id === id)?.name || 'Unknown'
  }

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold text-gray-800">Orders</h1>
        <button
          onClick={() => setShowForm(!showForm)}
          className="bg-blue-500 text-white px-6 py-2 rounded-lg font-semibold hover:bg-blue-600 transition-colors"
        >
          {showForm ? '✕ Cancel' : '+ Create Order'}
        </button>
      </div>

      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
          {error}
        </div>
      )}

      {/* Create Order Form */}
      {showForm && (
        <div className="bg-white rounded-lg shadow p-6 border-l-4 border-purple-500">
          <h2 className="text-xl font-bold text-gray-800 mb-4">Create New Order</h2>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-gray-700 text-sm font-bold mb-2">Select Customer *</label>
              <select
                value={formData.customer_id}
                onChange={handleCustomerChange}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-purple-500"
                required
              >
                <option value="">Choose a customer...</option>
                {customers.map(customer => (
                  <option key={customer.id} value={customer.id}>
                    {customer.name} ({customer.email})
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-gray-700 text-sm font-bold mb-2">Order Items *</label>
              <div className="space-y-3">
                {formData.items.map((item, index) => (
                  <div key={index} className="flex gap-3">
                    <select
                      value={item.product_id}
                      onChange={(e) => handleProductChange(index, e.target.value)}
                      className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-purple-500"
                      required
                    >
                      <option value="">Choose a product...</option>
                      {products.map(product => (
                        <option key={product.id} value={product.id}>
                          {product.name} (Stock: {product.stock_quantity})
                        </option>
                      ))}
                    </select>
                    <input
                      type="number"
                      min="1"
                      value={item.quantity}
                      onChange={(e) => handleQuantityChange(index, e.target.value)}
                      placeholder="Qty"
                      className="w-24 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-purple-500"
                      required
                    />
                    {formData.items.length > 1 && (
                      <button
                        type="button"
                        onClick={() => handleRemoveItem(index)}
                        className="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition-colors"
                      >
                        Remove
                      </button>
                    )}
                  </div>
                ))}
              </div>
              <button
                type="button"
                onClick={handleAddItem}
                className="mt-3 text-blue-500 hover:text-blue-700 font-semibold text-sm"
              >
                + Add Another Item
              </button>
            </div>

            <div className="flex gap-2 pt-4">
              <button
                type="submit"
                className="flex-1 bg-purple-500 text-white px-4 py-2 rounded-lg font-semibold hover:bg-purple-600 transition-colors"
              >
                Create Order
              </button>
              <button
                type="button"
                onClick={handleCancel}
                className="flex-1 bg-gray-300 text-gray-800 px-4 py-2 rounded-lg font-semibold hover:bg-gray-400 transition-colors"
              >
                Cancel
              </button>
            </div>
          </form>
        </div>
      )}

      {/* Orders List */}
      {loading ? (
        <div className="flex justify-center py-12">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-purple-500"></div>
        </div>
      ) : (
        <div className="bg-white rounded-lg shadow overflow-hidden">
          {orders.length === 0 ? (
            <div className="p-12 text-center text-gray-500">
              <p className="text-lg">No orders found</p>
              <p className="text-sm">Start by creating your first order</p>
            </div>
          ) : (
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead className="bg-gray-100 border-b border-gray-200">
                  <tr>
                    <th className="px-6 py-3 text-left text-sm font-semibold text-gray-700">Order ID</th>
                    <th className="px-6 py-3 text-left text-sm font-semibold text-gray-700">Customer</th>
                    <th className="px-6 py-3 text-right text-sm font-semibold text-gray-700">Total Amount</th>
                    <th className="px-6 py-3 text-left text-sm font-semibold text-gray-700">Items</th>
                    <th className="px-6 py-3 text-left text-sm font-semibold text-gray-700">Created</th>
                  </tr>
                </thead>
                <tbody>
                  {orders.map(order => (
                    <tr key={order.id} className="border-b border-gray-200 hover:bg-gray-50">
                      <td className="px-6 py-4 text-sm text-gray-800 font-semibold">#{order.id}</td>
                      <td className="px-6 py-4 text-sm text-gray-600">{getCustomerName(order.customer_id)}</td>
                      <td className="px-6 py-4 text-sm text-gray-800 text-right font-semibold">
                        ${order.total_amount.toFixed(2)}
                      </td>
                      <td className="px-6 py-4 text-sm text-gray-600">
                        {order.order_items?.length || 0} item(s)
                      </td>
                      <td className="px-6 py-4 text-sm text-gray-600">
                        {new Date(order.created_at).toLocaleDateString()}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}
    </div>
  )
}
