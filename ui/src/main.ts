import {CiukuneApp, AdminMenu, User} from '@ciukune/core'
import Admin from './views/admin/mailing.vue'

AdminMenu.addItem({
  component: Admin,
  path: 'mailing',
  icon: 'question',
  label: 'Mailing'
})
