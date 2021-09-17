<template lang="pug">
div(class="text-field")
  input(
    placeholder=" "
    :type="password ? 'password' : 'text'"
    :value="modelValue"
    @input="valueChanged($event)"
  )
  div(class="text-field-placeholder")
    div {{placeholder}}

</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    props: {
      'placeholder': String,
      'modelValue': String,
      'password': Boolean
    },
    emits: [
        'update:modelValue',
    ],
    setup(_, {emit}) {
      function valueChanged(event: Event) {
        const input = event.target as HTMLInputElement
        emit('update:modelValue', input.value)
      }
      return {
          valueChanged
      }
    },
})
</script>

<style>
.text-field {
  display: grid;
  padding-top: calc(var(--font-size) * 0.8);
}

.text-field > input {
  color: inherit;
}

.text-field > input {
  background: transparent;
  border-bottom: 1px var(--primary-dark) solid;
  border-left: none;
  border-right: none;
  border-top: none;
  font: var(--font);
  grid-area: 1 / 1;
  transition: border-bottom 0.2s;
}

.text-field > input:focus {
  outline: none;
  border-bottom: 1px var(--primary-light) solid;
}

.text-field-placeholder {
  color: var(--hint-on-surface);
  opacity: 0.5;
  display: flex;
  font-size: 90%;
  grid-area: 1 / 1;
  transition-duration: 0.2s;
  transition-property: transform font-size;
  z-index: -1;
}

.text-field-placeholder > div {
  align-self: center;
}

.text-field > input:focus + .text-field-placeholder {
  font-size: 80%;
  transform: translate(0px, calc(var(--font-size) * -1.1));
}

.text-field > input:not(:placeholder-shown) + .text-field-placeholder {
  font-size: 80%;
  transform: translate(0px, calc(var(--font-size) * -1.1));
}
</style>
