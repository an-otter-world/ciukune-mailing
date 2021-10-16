import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': 'http://localhost:8000/',
    },
  },
  build: {
    sourcemap: true,
    lib: {
      entry: './src/main.ts',
      name: 'ciukune',
      formats: ['es']
    },
    rollupOptions: {
      treeshake: false,
      output: {
        assetFileNames: 'css/ciukune.core[extname]',
        chunkFileNames: 'js/[name].js',
        entryFileNames: 'js/ciukune.core.js',
        minifyInternalExports: false,
        manualChunks: {
          'vue': ['vue'],
          'ckc':['@ciukune/ckc'],
          'vue-router': ['vue-router']
        }
      }
    }
  },
})
