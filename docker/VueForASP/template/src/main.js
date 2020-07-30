//import 'babel-polyfill'

import Vue from 'vue'
import App from './App.vue'

import lang from 'element-ui/lib/locale/lang/en'
import locale from 'element-ui/lib/locale'
import './theme.scss'

// configure language
locale.use(lang)

import { Button, Select, Option } from 'element-ui';
Vue.use(Button);Vue.use(Select);Vue.use(Option)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
