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
      external: ['vue', '@ciukune/core', '@dontnod/wlh'],
      treeshake: false,
      output: {
        assetFileNames: 'css/ciukune.mailing[extname]',
        chunkFileNames: 'js/[name].js',
        entryFileNames: 'js/ciukune.mailing.js',
        dir: '../ciukune/mailing/static/ui/',
        minifyInternalExports: false,
        paths: {
          '@ciukune/core': './ciukune.core.js'
        }
      }
    }
  },
})
