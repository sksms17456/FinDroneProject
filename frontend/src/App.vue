<template>
  <v-app>
    <Intro v-if="first" @goHome="goHome"/>
    <Header v-if="!first"/>
      <v-content>
        <router-view/>
      </v-content>
      <Scrolltotop/>
    <Footer v-if="!first"/>
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
      first:false
    }
  },
  methods:{
    goHome(tile){
      this.first=false
    }
  }
}
</script>
