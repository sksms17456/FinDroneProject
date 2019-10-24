import Vue from 'vue'
import Router from 'vue-router'
import Intro from './views/Intro.vue'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'intro',
      component: Intro
    },
    {
      path:'/home',
      name:'home',
      component:Home
    },
    {
      path:'/about',
      name:'about',
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path:'/service',
      name:'serive',
      component: () => import(/* webpackChunkName: "about" */ './views/Service.vue')
    },
    {
      path:'/central',
      name:'central',
      component: () => import(/* webpackChunkName: "about" */ './views/Central.vue')
    },
    {
      path:'*',
      name:'error',
      component: () => import(/* webpackChunkName: "about" */ './views/Error.vue')
    }
    
  ]
})
