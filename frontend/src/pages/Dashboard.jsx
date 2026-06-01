import { useEffect, useState } from 'react'
import { ordersAPI } from '../services/api'
import StatCard from "../components/StatCard";

export default function Dashboard() {
  const [stats, setStats] = useState({
    total_products: 0,
    total_customers: 0,
    total_orders: 0,
    total_revenue: 0
  })
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchStats = async () => {
      try {
        setLoading(true)
        const response = await ordersAPI.getDashboardStats()
        setStats(response.data)
      } catch (err) {
        setError('Failed to load dashboard statistics')
        console.error(err)
      } finally {
        setLoading(false)
      }
    }

    fetchStats()
  }, [])

  if (loading) {
    return (
      <div className="flex items-center justify-center h-96">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading dashboard...</p>
        </div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded relative">
        <strong className="font-bold">Error!</strong>
        <span className="block sm:inline ml-2">{error}</span>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold text-gray-800">Dashboard</h1>

      {/* Statistics Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <StatCard
          title="Total Products"
          value={stats.total_products}
          icon="📦"
          color="bg-blue-50 border-blue-200"
          iconBg="bg-blue-100"
        />
        <StatCard
          title="Total Customers"
          value={stats.total_customers}
          icon="👥"
          color="bg-green-50 border-green-200"
          iconBg="bg-green-100"
        />
        <StatCard
          title="Total Orders"
          value={stats.total_orders}
          icon="🛒"
          color="bg-purple-50 border-purple-200"
          iconBg="bg-purple-100"
        />
        <StatCard
          title="Total Revenue"
          value={`$${stats.total_revenue.toFixed(2)}`}
          icon="💰"
          color="bg-orange-50 border-orange-200"
          iconBg="bg-orange-100"
        />
      </div>

      {/* Welcome Section */}
      <div className="bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg shadow-lg p-8 text-white">
        <h2 className="text-2xl font-bold mb-2">Welcome to Inventory Management</h2>
        <p className="text-blue-50">
          Manage your inventory efficiently with our comprehensive system. Track products,
          customer information, and orders all in one place.
        </p>
        <div className="mt-6 flex gap-4">
          <button className="bg-white text-blue-600 px-6 py-2 rounded-lg font-semibold hover:bg-blue-50 transition-colors">
            Get Started
          </button>
          <button className="border-2 border-white text-white px-6 py-2 rounded-lg font-semibold hover:bg-white hover:bg-opacity-10 transition-colors">
            Learn More
          </button>
        </div>
      </div>

      {/* Quick Actions */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white rounded-lg shadow p-6 border-l-4 border-blue-500">
          <h3 className="text-lg font-bold text-gray-800 mb-4">Quick Actions</h3>
          <ul className="space-y-2 text-gray-600">
            <li>✓ Add new products to inventory</li>
            <li>✓ Register new customers</li>
            <li>✓ Create and track orders</li>
            <li>✓ Monitor stock levels</li>
          </ul>
        </div>

        <div className="bg-white rounded-lg shadow p-6 border-l-4 border-green-500">
          <h3 className="text-lg font-bold text-gray-800 mb-4">System Features</h3>
          <ul className="space-y-2 text-gray-600">
            <li>✓ Real-time inventory tracking</li>
            <li>✓ Automatic stock reduction</li>
            <li>✓ Order management</li>
            <li>✓ Comprehensive reporting</li>
          </ul>
        </div>
      </div>
    </div>
  )
}
