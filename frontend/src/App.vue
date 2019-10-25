<template>
  <v-app>
    <v-content>
    <!-- <Header/> -->
    <Index/>
      
    </v-content>
    <!-- <div id="introPage">
    <Intro v-if="introPage" @goHome="goHome"/>
    </div>
    <div>
    <v-content v-if="!introPage">
    <Header/>
        <router-view/>
      <Scrolltotop/>
    <Footer/>
    </v-content> -->
    <!-- </div> -->
  </v-app>
</template>

<script>
import Intro from './views/Intro'
import Header from './components/Header'
import Footer from './components/Footer'
import Scrolltotop from './components/ScrollToTop'
import Index from './components/index'

export default {
  name: 'App',
  components:{
    Index,
    Intro,
    Header,
    Scrolltotop,
    Footer
  },
  data () {
    return {
      introPage:true
    }
  },

  mounted(){
    var path = this.$route.path;

    // 새로고침 방지용 현재 path에 따라 구분
    if(path!="/"){
      this.introPage = false;
    }else {
      this.introPage = true;
    }
  },
  methods:{
    goHome(){
      this.introPage=false;
      this.$router.push('/home').catch(err => {})
    }
  }

}
</script>
