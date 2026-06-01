export default function StatCard({ title, value, icon, color, iconBg }) {
  return (
    <div className={`${color} rounded-lg shadow p-6 border`}>
      <div className="flex items-center justify-between">
        <div>
          <p className="text-gray-600 text-sm font-medium">{title}</p>
          <p className="text-3xl font-bold text-gray-800 mt-2">{value}</p>
        </div>
        <div className={`${iconBg} rounded-full p-3 text-2xl`}>
          {icon}
        </div>
      </div>
    </div>
  )
}
