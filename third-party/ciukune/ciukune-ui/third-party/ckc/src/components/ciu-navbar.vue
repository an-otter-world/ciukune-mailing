<template lang="pug">
div(class="ciu-primary ciu-navbar" v-bind:class="{'ciu-small': !$mq('sm')}")
  div(class="ciu-brand")
    slot(name="brand")
  div(class="ciu-menu" ref="menu")
    a(href="#" v-on:click="toggle()")
      ciu-icon(icon="bars")
    div(class="ciu-links" v-on:mouseup="close()" v-bind:class="{ 'ciu-opened': isOpened }")
      slot
  div(class="ciu-end")
    slot(name="end")
</template>

<script lang="ts">

import { defineComponent } from 'vue'
import { ref } from 'vue'

export default defineComponent({
  setup() {
    const isOpened = ref(false);
    const html = document.documentElement
    const menu = ref<Node | null>(null)

    function open() {
      html.addEventListener('click', onBodyClick);
      isOpened.value = true
    }

    function close() {
      html.removeEventListener('click', onBodyClick);
      isOpened.value = false
    }

    function toggle() {
      if(!isOpened.value) {
        open()
      }
      else {
        close()
      }
    }

    function onBodyClick(e: Event) {
      if(!menu.value!.contains(e.target as Node)) {
        close()
      }
    }

    return {
      close,
      isOpened,
      menu,
      toggle,
    }
  },
})
</script>

<style>
.ciu-navbar {
  display: flex;
  align-items: stretch;
}

.ciu-navbar > div {
  align-items: center;
  display: flex;
}

.ciu-navbar > .ciu-brand {
  flex-grow: 0;
  margin-left: var(--ciu-spacing);
  margin-right: var(--ciu-spacing);
}

.ciu-navbar.ciu-small > .ciu-brand {
  flex-grow: 1;
  order: 1;
}

.ciu-navbar > .ciu-menu {
  display: flex;
  flex-grow: 1;
}

.ciu-navbar.ciu-small > .ciu-menu {
  flex-direction: column;
  flex-grow: 0;
}

.ciu-navbar > .ciu-menu > a {
  display: none;
}

.ciu-navbar.ciu-small > .ciu-menu > a {
  display: inline;
}

.ciu-navbar > .ciu-menu > .ciu-links {
  display: flex;
}

.ciu-navbar.ciu-small > .ciu-menu > .ciu-links {
  background: var(--ciu-primary);
  flex-direction: column;
  left: 0;
  display: none;
  padding: calc(0.5 * var(--ciu-spacing));
  position: absolute;
  top: 3rem;
}

.ciu-navbar.ciu-small > .ciu-menu > .ciu-links.ciu-opened {
  display: flex;
}

.ciu-navbar > .ciu-end {
  flex-grow: 0;
  margin-left: var(--ciu-spacing);
  margin-right: var(--ciu-spacing);
}

.ciu-navbar.ciu-small > .ciu-end {
  order: 2;
}

.ciu-navbar > .ciu-menu a {
  align-items: center;
  padding: var(--ciu-spacing);
  text-transform: uppercase;
}

.ciu-navbar > .ciu-menu a:hover {
  background-color: var(--ciu-primary-light);
  text-decoration: none;
}

.ciu-navbar > .ciu-menu a.router-link-active {
  background-color: var(--ciu-primary-dark);
  text-transform: uppercase;
}
</style>
