<template lang="pug">
//- This components injects a resource for child components (inputs, error feedback, loading feedback...) to access it.
div(v-bind:class="{'loading-overlay': true, 'loading': loading}")
  div(id='background')
  c-screen-center
    c-spinner(id='spinner')
  div
    slot
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    'loading': Boolean,
  }
})
</script>

<style>
.loading-overlay {
  display: grid;
}

.loading-overlay > * {
  grid-area: 1 / 1
}

.loading-overlay #background, #spinner {
  opacity: 0;
  transition: opacity var(--transition-duration) ease var(--transition-duration);
  z-index: -1;
}

.loading-overlay.loading #background {
  background: var(--surface);
  opacity: 0.5;
  z-index: 1;
}

.loading-overlay.loading #spinner {
  opacity: 1;
  z-index: 1;
}

</style>
