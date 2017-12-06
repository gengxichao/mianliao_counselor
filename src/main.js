import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import VueResource from 'vue-resource'
import App from './App.vue'

Vue.use(ElementUI)
Vue.use(VueResource)

new Vue({
  el: '#app',
  render: h => h(App)
})
