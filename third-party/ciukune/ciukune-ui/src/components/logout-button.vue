<template lang="pug">
a(@click="logout()" href="#" class="ciu-logout-button")
  div(class="ciu-router-link ciu-flex-row")
    ciu-icon(icon="sign-out-alt")
    div {{ $t("logout-button.logout") }}
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { getLoginResource } from '../api/resources/auth/login'

export default defineComponent({
  setup() {
    const login = getLoginResource()

    async function logout() {
      await login.logout()     
    }

    return { 
      logout
    }
  },
})
</script>

<style>
.ciu-logout-button > svg {
  margin-right: var(--ciu-spacing);
}
</style>

