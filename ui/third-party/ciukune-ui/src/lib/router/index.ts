import Home from '../../views/home.vue'
import Profile from '../../views/profile.vue'
import Admin from '../../views/admin.vue'

export const routes = [{
    path: "/",
    name: "Home",
    component: Home,
  }, {
    path: "/profile",
    name: "Profile",
    component: Profile,
  }, {
    path: "/admin",
    name: "Admin",
    component: Admin,
  }
];
