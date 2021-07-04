<template lang="pug">
button(class="ciu-control ciu-ripple" :type="type")
  slot
</template>

<script lang="ts">
import { PropType } from 'vue'
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    'type': Object as PropType<'submit' | 'reset' | 'button'>,
  },
  setup() {
    
  },
})
</script>
