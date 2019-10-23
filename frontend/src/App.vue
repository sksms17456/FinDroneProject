<template>
  <v-app>
    <div v-if="first">
      <Intro @intro="goHome"/>
    </div>

    <div v-else>
      <Header/>
      <v-content>
        <router-view/>
      </v-content>
      <Scrolltotop/>
      <Footer/>
    </div>
  </v-app>
</template>

<script>
import Intro from './views/Intro'
import Header from './components/Header'
import Footer from './components/Footer'
import Scrolltotop from './components/ScrollToTop'

export default {
  name: 'App',
  components:{
    Intro,
    Header,
    Scrolltotop,
    Footer
  },
  data () {
    return {
      first:true
    }
  },
  methods:{
    goHome(tile){
    }
  }
}
</script>
