import 'babel-polyfill'

import Vue from 'vue'
import App from './App.vue'

import ElementUI from 'element-ui'
import local from 'element-ui/lib/locale/lang/zh-TW'
import './theme.scss'

Vue.use(ElementUI, {local});

import axios from 'axios'

//axios.defaults.baseURL = "ENTER HERE/";
Vue.prototype.$http = axios;


Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
}).$mount('#app');
