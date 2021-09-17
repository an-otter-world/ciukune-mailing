<template lang="pug">
div(class="component")
  div(class='component-background')
    slot
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  setup() {},
})
</script>

<style>
.component {
  color: var(--on-surface);
  display: grid;
  margin: var(--spacing);
}

.component > * {
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow);
  grid-area: 1 / 1;
  padding: var(--spacing);
}

.component > .component-background {
  background-color: var(--surface);
}

.component > header {
  margin-bottom: var(--spacing);
  padding-bottom: var(--spacing);
}

.component > hr {
  border-bottom: 1px var(--on-surface) solid;
  border-left: none;
  border-right: none;
  border-top: none;
  margin-bottom: var(--spacing);
  margin-top: var(--spacing);
  width: 80%;
}
</style>
