<template lang="pug">
c-component
  header
    h1 Profile
  c-api-form(:resource="me")
    c-api-errors
    c-api-input(field="email")
      c-text-field(:placeholder="$t('profile.email')" v-model="state.email")
    c-api-input(field="username" patch)
      c-text-field(:placeholder="$t('profile.username')" v-model="state.username")
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { getMeResource } from '../api/resources/user/me'

export default defineComponent({
  async setup() {
    const me = getMeResource()

    await me.load()

    return {
	    me: me,
      state: me.state!
    }
  }
})
</script>
