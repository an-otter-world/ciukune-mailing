import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000/',
        xfwd: true
      }
    },
  },
  build: {
    sourcemap: true,
    minify: true,
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
          'wlh':['@dontnod/wlh'],
          'vue-router': ['vue-router']
        }
      }
    }
  },
})
