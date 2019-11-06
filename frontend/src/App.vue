<template>
  <v-app id="mainDisplay">
    <div id="introPage">
      <Intro v-if="introPage" @goHome="goHome"/>
    </div>
    <div>
      <v-content v-if="!introPage">
        <Header/>
         <v-img id="floatingLogo" :src="getImgUrl('FinDrone_Logo.png')" contain></v-img>
        <router-view/>
        <Footer/>
      </v-content>
    </div>
  </v-app>
</template>

<script>
import Intro from './views/Intro'
import Header from './components/Header'
import Footer from './components/Footer'

export default {
  name: 'App',
  components:{
    Intro,
    Header,
    Footer
  },
  data () {
    return {
      introPage:true
    }
  },
  watch: {
    '$route' (to, from) {
      // 경로 변경에 반응하여...
      var deskToolbarElement = document.getElementById("deskToolbar");
      var deskFooterElement = document.getElementById('footer');

      if(to.path === '/central' || to.path === '/rootmap'){
        deskToolbarElement.style.display = "none";
        deskFooterElement.style.display = "none";
      }
      else{
        deskToolbarElement.style.display = "block";
        deskFooterElement.style.display = "block";
        deskToolbarElement.style.background = "transparent";
      }
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

    document.getElementById('mainDisplay').onwheel = function(){ return false; }
  },
  methods:{
    goHome(){
      this.introPage=false;
      this.$router.push('/home').catch(err => {})
    },
    getImgUrl(img){
      return require('./assets/'+img);
    }
  }

}
</script>

<style scoped>
#mainDisplay {
  background-color: white;
}
#floatingLogo{
  position:fixed; 
  height:100px;
  width:100px;
  z-index:1; 
  right:20px; 
  bottom:0;
}
</style>
