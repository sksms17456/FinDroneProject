import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

export const eventBus = new Vue({
  // 메소드로 만들어 형제 컴포넌트에서 선언한 userWasEdited를 메소드화 
  methods:{
    goToMenu(data){
      this.$emit('goToMenu', data)
    }
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
