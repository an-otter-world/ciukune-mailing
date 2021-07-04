<template lang="pug">
div(class="ciu-dropdown")
  header
    a(href="#" @click="toggle()")
      slot(name="header")
        ciu-icon(icon="chevron-down")
  div(v-if="isOpen" @click="isOpen = false")
    slot
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { ref } from 'vue'

export default defineComponent({
  setup() {
    let isOpen = ref(false);
    let toggle = () => {
      isOpen.value = !isOpen.value;
    }
    return {
      isOpen,
      toggle
    }
  },
})
</script>

<style>
.ciu-dropdown > header {
  position: relative;
}

.ciu-dropdown > header {
  vertical-align: middle;
}

.ciu-dropdown > div {
  background: var(--ciu-primary);
  border-bottom-left-radius: var(--ciu-border-radius);
  border-bottom-right-radius: var(--ciu-border-radius);
  border-top: 1px solid var(--ciu-on-primary);
  padding: var(--ciu-spacing);
  position: absolute;
  right: 0px;
}
</style>
