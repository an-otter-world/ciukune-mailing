<template lang="pug">
c-screen-center(v-if="!me.state")
  c-loading-overlay(:loading="me.loading")
    login-view
div(v-else)
  navbar
  router-view
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { ref } from 'vue'
import { onMounted } from 'vue'
import LoginView from './views/login.vue'
import Navbar from './components/navbar.vue'
import { getMeResource } from './api/resources/user/me'


export default defineComponent({
  name: 'App',
  components: {
    LoginView,
    Navbar
  },
  setup() {
    const me = getMeResource()
    const loading = ref(false)

    onMounted(async () => {
      await me.load()
    })

    return {
      loading,
      me,
    }
  },
})
</script>

<style>

#app {
  height: 100vh;
}
</style>