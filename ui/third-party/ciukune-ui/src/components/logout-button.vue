<template lang="pug">
a(@click="logout()" href="#" class="logout-button")
  div(class="c-router-link c-flex-row")
    c-icon(icon="sign-out-alt")
    div {{ $t("logout-button.logout") }}
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { getLogin } from '../lib/api/auth/login'

export default defineComponent({
  setup() {
    const login = getLogin()
    const [_, logout ] = login.do(async login => await login.logout())

    return { 
      logout
    }
  },
})
</script>

<style>
.logout-button > svg {
  margin-right: var(--ciu-spacing);
}
</style>

