<template lang="pug">
c-navbar
  template(v-slot:brand)
    h1 Ciu Kune
  router-link(to="/") Home
  template(v-slot:end)
    c-dropdown
      template(#header)
        c-icon(icon="user-circle")
      c-router-link(to="/profile" icon="user-circle") {{ $t('navbar.profile') }}
      c-router-link(to="/admin" icon="user-circle") {{ $t('navbar.admin') }}
      logout-button
</template>


<script lang="ts">
import { defineComponent } from 'vue'
import LogoutButton from './logout-button.vue'

export default defineComponent({
  components: {
    LogoutButton
  },
  setup() {
    return {
    }
  },
})
</script>
