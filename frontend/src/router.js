import Vue from 'vue'
import Router from 'vue-router'
import Intro from './views/Intro.vue'
import Home from './views/Home.vue'
import About from './views/About.vue'
import Service from './views/Service.vue'
import ErrorPage from './views/Error.vue'
import RootMap from './views/RootMap.vue'
import MultiMonitor from './components/MultiMonitor.vue'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [{
            path: '/',
            name: 'intro',
            component: Intro
        },
        {
            path: '/home',
            name: 'home',
            component: Home
        },
        {
            path: '/about',
            name: 'about',
            component: About
        },
        {
            path: '/service',
            name: 'serive',
            component: Service
        },
        {
            path: '/central',
            name: 'central',
            component: MultiMonitor
        },
        {
            path: '/rootmap',
            name: 'rootmap',
            component: RootMap
        },
        {
            path: '*',
            name: 'error',
            component: ErrorPage
        }
    ],
    scrollBehavior (to, from, savedPosition) {
        if(to.path != from.path){
            return { x: 0, y: 0 }
        }
    }
})