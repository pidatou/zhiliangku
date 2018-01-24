import Vue from 'vue'
import App from './App'
import router from '../../router/personalCenterRouter'
Vue.config.productionTip = false
//引入脚本
import fn from '../../utils/index'
Vue.prototype.$fn = fn;
import Obj from '../../assets/js/const'
Vue.prototype.$myConst = Obj;
//引入选择的插件
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
// import Echarts from 'echarts'
Vue.use(ElementUI)
// Vue.prototype.$echarts = Echarts;
import '../../utils/axios'
Vue.prototype.getSelf=function(){
  return  this
}
Vue.prototype.deepCopy = function (obj) {
  return JSON.parse(JSON.stringify(obj))
}
Vue.prototype.initForm=function(vue, obj, keys1, keys2) {
  for (var i = 0; i < keys1.length; i++) {
    vue[keys2[i]] = obj[keys1[i]];
  }
}

var indexvue = new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: {
    App
  }
})
