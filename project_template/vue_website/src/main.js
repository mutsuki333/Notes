import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import i18n from './i18n'
import axios from 'axios'

import 'bulma'

axios.defaults.baseURL = process.env.VUE_APP_API_ROOT
axios.defaults.withCredentials = true
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

if (process.env.NODE_ENV === 'development') {
  axios.defaults.debug = true
  Vue.config.productionTip = false
} else Vue.config.productionTip = true

Vue.prototype.$http = axios

new Vue({
  router,
  store,
  i18n,
  render: h => h(App)
}).$mount('#app')
