<template lang="pug">
ciu-navbar
  template(v-slot:brand)
    h1 Ciu Kune
  router-link(to="/") Home
  template(v-slot:end)
    ciu-dropdown
      template(#header)
        ciu-icon(icon="user-circle")
      ciu-router-link(to="/profile" icon="user-circle") {{ $t('navbar.profile') }}
      logout-button
</template>


<script lang="ts">
import { defineComponent } from 'vue'
import LogoutButton from './logout-button.vue'
import { getLoginResource } from '../api/resources/auth/login'

export default defineComponent({
  components: {
    LogoutButton
  },
  setup() {
    const login = getLoginResource() 
    return {
      logout: async () => await login.logout()
    }
  },
})
</script>
