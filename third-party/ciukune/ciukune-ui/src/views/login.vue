<template lang="pug">
ciu-screen-center
  ciu-component
    header {{ $t('login.title') }}
    ciu-api-form(:resource="login" @submit.prevent="doLogin()")
      ciu-api-errors
      ciu-api-input(field="email")
        ciu-text-field(:placeholder="$t('login.email')" v-model="login.email")
      ciu-api-input(field="password")
        ciu-text-field(password :placeholder="$t('login.password')" v-model="login.password")
      ciu-button(type="submit") {{ $t('login.login') }} 
    hr
    div(class="links-area")
      a(href='#') {{ $t('login.reset-password') }}
      a(href='#') {{ $t('login.register') }}
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { getLoginResource } from '../api/resources/auth/login'

export default defineComponent({
    setup() {
      const login = getLoginResource()

      async function doLogin() {
        await login.login()
      }

      return {
        doLogin: doLogin,
        login: getLoginResource()
      }
    },
})
</script>

<style scoped>
.links-area {
  display: flex;
  flex-direction: row;
  align-items: stretch;
}

.links-area > *:last-child {
  border-left: 1px var(--ciu-muted-on-surface) solid;
  margin-left: var(--ciu-spacing);
  padding-left: var(--ciu-spacing);
}
</style>
