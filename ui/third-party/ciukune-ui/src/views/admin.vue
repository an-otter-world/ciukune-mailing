<template>
  <c-component>
    <ul>
      <li>
        <router-link to="/admin/general">
          General
        </router-link>
      </li>
      <li>
        <router-link to="/admin/mailing">
          Mailing
        </router-link>
      </li>
    </ul>
    <router-view/>
  </c-component>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  setup() {
    return {}  
  },
})
</script>
