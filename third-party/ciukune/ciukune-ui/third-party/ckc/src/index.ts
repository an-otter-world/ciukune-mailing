import './assets/styles/_index.css'
import './font-awesome'
import './ckc.d.ts'
import Vue from 'vue'
import CiuApiErrors from './components/ciu-api-errors.vue'
import CiuApiForm from './components/ciu-api-form.vue'
import CiuApiInput from './components/ciu-api-input.vue'
import CiuButton from './components/ciu-button.vue'
import CiuComponent from './components/ciu-component.vue'
import CiuDropdown from './components/ciu-dropdown.vue'
import CiuIcon from './components/ciu-icon.vue'
import CiuInput from './components/ciu-input.vue'
import CiuLoadingOverlay from './components/ciu-loading-overlay.vue'
import CiuNavbar from './components/ciu-navbar.vue'
import CiuRouterLink from './components/ciu-router-link.vue'
import CiuScreenCenter from './components/ciu-screen-center.vue'
import CiuSpinner from './components/ciu-spinner.vue'
import CiuTextField from './components/ciu-text-field.vue'
import { App } from 'vue';
import { MediaQueryOptions } from './services/media-query'
import { installResourceManager } from './services/resource-manager'
import { installBackend } from './services/backend'
import { mediaQuery } from './services/media-query'

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $mq: (query: string) => boolean
  }
}

export interface CkcOptions {
  mqOptions?: MediaQueryOptions
}

export default function install<T>(app: App<T>, options?: CkcOptions) {
    installBackend(app)
    installResourceManager(app)
    app
      .component('CiuApiErrors', CiuApiErrors)
      .component('CiuApiForm', CiuApiForm)
      .component('CiuApiInput', CiuApiInput)
      .component('CiuButton', CiuButton)
      .component('CiuComponent', CiuComponent)
      .component('CiuDropdown', CiuDropdown)
      .component('CiuIcon', CiuIcon)
      .component('CiuInput', CiuInput)
      .component('CiuLoadingOverlay', CiuLoadingOverlay)
      .component('CiuNavbar', CiuNavbar)
      .component('CiuRouterLink', CiuRouterLink)
      .component('CiuScreenCenter', CiuScreenCenter)
      .component('CiuSpinner', CiuSpinner)
      .component('CiuTextField', CiuTextField)

    app.config.globalProperties.$mq = mediaQuery(options?.mqOptions)
}

export { Backend } from './services/backend'
export { Resource } from './services/resource'
export { ResourceObject } from './services/resource-object'
export { getBackend } from './services/backend'
export { getCurrentResource } from './services/current-resource'
export { getResource } from './services/resource-manager'
