<template>
<div>
  <c-component>
    <plugin-menu :menu="menu"/>
  </c-component>
  <c-component>
    <router-view/>
  </c-component>
</div>
</template>

<script lang="ts">
import { defineComponent, reactive } from 'vue'
import PluginMenu, { Menu } from '../components/common/plugin-menu.vue'
import General from './admin/general.vue'

const AdminMenu = new Menu('/admin')
export { AdminMenu }

export default defineComponent({
  components: { PluginMenu },
  setup() {
    AdminMenu.addItem({
      component: General,
      path: '/general',
      icon: 'user',
      label: 'General'
    })

    return {
      menu: reactive(AdminMenu)
    }  
  },
})
</script>
