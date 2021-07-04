<template lang="pug">
ciu-component
  header
    h1 Profile
  ciu-api-form(:resource="me")
    ciu-api-errors
    ciu-api-input(field="email")
      ciu-text-field(:placeholder="$t('profile.email')" v-model="state.email")
    ciu-api-input(field="username" patch)
      ciu-text-field(:placeholder="$t('profile.username')" v-model="state.username")
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
