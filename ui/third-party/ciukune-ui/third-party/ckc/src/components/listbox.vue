<template lang="pug">
div(class="listbox flex-column")
  div(
        v-for="item in items"
        :key="item.id"
        class="listbox-item"
        @click="selectItem($event.target, item)"
    )
    slot(name="item" v-bind:item="item")
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue'
import { ref } from 'vue'

export default defineComponent({
  props: {
    items: Object as PropType<Object>,
    selectionDisabled: Boolean,
  },
  emits: ['update:selectedItem'],
  setup({ selectionDisabled }, { emit }) {
    let selectedItem = ref(undefined)
    let selectedItemElement: HTMLElement | undefined = undefined
    let selectItem = function (element: EventTarget | null, item: any) {
      if (selectionDisabled) {
        return
      }

      if (selectedItemElement) {
        selectedItemElement.classList.remove('primary')
      }

      if (selectedItem) {
        selectedItem.value = item
        emit('update:selectedItem', item)
      }

      selectedItemElement = element as HTMLElement
      if (selectedItemElement) {
        selectedItemElement.classList.add('primary')
      }
    }

    return {
      selectItem,
      selectedItem,
    }
  },
})
</script>

<style lang="scss">
.listbox {
  margin: var(--spacing);
  overflow: auto;
  height: calc(100% - 4rem);
  .listbox-item {
    user-select: none;
    border-color: var(--context-color);
    border-radius: var(--border-radius);
    border: 1px solid;
    cursor: pointer;
    margin: calc(0.2 * var(--spacing));
    padding: calc(0.2 * var(--spacing));

    &:nth-child(2n):not(.primary) {
      background-color: rgba(black, 0.2);
    }
  }
}
</style>
