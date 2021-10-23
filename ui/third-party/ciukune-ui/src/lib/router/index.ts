import Home from '../../views/home.vue'
import Profile from '../../views/profile.vue'

export const routes = [{
    path: "/",
    name: "Home",
    component: Home,
  }, {
    path: "/profile",
    name: "Profile",
    component: Profile,
  }
];
