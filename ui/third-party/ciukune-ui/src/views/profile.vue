<template lang="pug">
c-component
  header
    h1 Profile
  c-api-form(:resource="user")
    c-api-errors
    c-api-input(field="email")
      c-text-field(:placeholder="$t('profile.email')" v-model="email")
    c-api-input(field="username" patch)
      c-text-field(:placeholder="$t('profile.username')" v-model="username")
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { getLogin } from '../lib/api'

export default defineComponent({
  setup() {
    let login = getLogin()
    let user = login.nested(r => r.currentUser)
    let email = user.field(r => r.email)
    let username = user.field(r => r.username, (r, value) => r.username = value)

    return {
      user,
      email,
      username,
    }
  }
})
</script>
