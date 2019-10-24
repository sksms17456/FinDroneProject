<template>
  <v-app>
    <div id="introPage">
    <Intro v-if="first" @goHome="goHome"/>
    </div>
    <div>
    <v-content v-if="!first">
    <Header/>
        <router-view/>
      <Scrolltotop/>
    <Footer/>
    </v-content>
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
    goHome(){
      this.first=false;
      this.$router.push('/home').catch(err => {})
    }
  }
}
</script>
