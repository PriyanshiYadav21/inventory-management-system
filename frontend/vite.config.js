import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    allowedHosts: [
      "graceful-abundance-production-9b3e.up.railway.app"
    ]
  },
  preview: {
    allowedHosts: [
      "graceful-abundance-production-9b3e.up.railway.app"
    ]
  }
});