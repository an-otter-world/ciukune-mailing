<template lang="pug">
router-link(:to="to" class="ciu-router-link")
  div(class="ciu-router-link ciu-flex-row")
    ciu-icon(:icon="icon")
    slot
</template>

<script lang="ts">
import { PropType } from 'vue'
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    'to': {
      type: String,
      required: true,
    },
    'icon': {
      type: String,
      required: true,
    }
  },
  setup({ to, icon }) {
    return { to, icon } 
  },
})
</script>

<style>
.ciu-router-link > svg {
  margin-right: var(--ciu-spacing);
}
</style>

