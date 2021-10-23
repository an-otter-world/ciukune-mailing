<template>
<c-screen-center v-if="loading">
  <c-loading-overlay :loading="loading"/>
</c-screen-center>
<div v-else-if="loggedIn">
  <navbar/>
  <router-view/>
</div>
<login-view v-else/>
</template>

<script lang="ts">
import { defineComponent, watch, reactive } from 'vue'
import LoginView from './views/login.vue'
import Navbar from './components/navbar.vue'
import { getLogin } from './lib/api'


export default defineComponent({
  name: 'App',
  components: {
    LoginView,
    Navbar
  },
  setup() {
    const login = getLogin()
    const loading = login.loading
    const currentUser = login.nested(o => o.currentUser)
    const loggedIn = currentUser.available
    const username = currentUser.field(o => o.username)

    return {
      loading,
      loggedIn,
      username
    }
  },
})
</script>

<style>

#app {
  height: 100vh;
}
</style>