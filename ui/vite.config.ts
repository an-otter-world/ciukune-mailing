import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': 'http://localhost:8000/',
    }
  },
  build: {
    sourcemap: true,
    lib: {
      entry: './src/main.ts',
      name: 'ciukune',
      formats: ['es']
    },
    rollupOptions: {
      external: ['vue', '@ciukune/core', '@ciukune/ckc'],
      treeshake: false,
      output: {
        assetFileNames: 'css/ciukune.mailing[extname]',
        chunkFileNames: 'js/[name].js',
        entryFileNames: 'js/ciukune.mailing.js',
        dir: '../ciukune/mailing/static/ui/',
        minifyInternalExports: false,
      }
    }
  },
})
