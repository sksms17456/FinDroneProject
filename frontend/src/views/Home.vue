<template>
  <div>
    <!-- 홈 화면(sector1) -->
    <birdBackground/>
    <!-- 간단소개 (sector2) -->
    <About/>
    <!-- 시스템 소개 (sector3) -->
    <System/>
    <!-- 서비스 소개 (sector4) -->
    <Service/>
    <!-- 어플리케이션 소개 (sector5) -->
    <Application/>
  </div>
</template>

<script>
import birdBackground from '../components/birdBackground'
import About from '../components/About'
import System from '../components/System'
import Service from '../components/Service'
import Application from '../components/Application'
import $ from "jquery";
import { eventBus } from '../main'

export default {
  name: "Home",
  components: {
    birdBackground,
    About,
    System,
    Service,
    Application
  },
  mounted() {
    window.onpopstate = event => {
      if (this.$route.path == "/") {
        this.$router.push("/home");
      }
    };
    eventBus.$on("goToMenu", move => {
        this.animationSetting(move);
    });
  },
  methods: {
    getImgUrl(img) {
      return require("../assets/" + img);
    },
    animationSetting(move){
      if(move=='system'){
        this.ableSystem();
      } else{
        this.disableSystem();
      }

      if(move=='about'){
        this.ableAbout()
      } else {
        this.disableAbout()
      }
    },
    ableAbout(){
      var vertical = document.getElementById('vertical_line');
      var lightbulb = document.getElementById('lightbulb');
      var title = document.getElementById('about_Title');
      var about = document.getElementById('hello_text');
      vertical.classList.add('on');
      lightbulb.classList.add('on');
      title.classList.add('on');
      about.classList.add('on');
    },
    disableAbout(){
      var vertical = document.getElementById('vertical_line');
      var lightbulb = document.getElementById('lightbulb');
      var title = document.getElementById('about_Title');
      var about = document.getElementById('hello_text');
      vertical.classList.remove('on');
      lightbulb.classList.remove('on');
      title.classList.remove('on');
      about.classList.remove('on');
    },
    ableSystem(){
      var st0 = document.getElementById('sysTitle0');
      st0.classList.add("systemMTitle");

      var st1 = document.getElementById('sysTitle1');
      st1.classList.add("systemSTitle1");

      var st2 = document.getElementById('sysTitle2');
      st2.classList.add("systemSTitle2");
        
      $('#structure').animate({'opacity':'1','margin-left':'0px'},1500);
    },
    disableSystem(){
      var st0 = document.getElementById('sysTitle0');
      st0.classList.remove("systemMTitle");

      var st1 = document.getElementById('sysTitle1');
      st1.classList.remove("systemSTitle1");

      var st2 = document.getElementById('sysTitle2');
      st2.classList.remove("systemSTitle2");
      $('#structure').animate({'opacity':'0','margin-left':'-300px'},1500);
    }
  },
  
};
</script>

<style scoped>
@font-face {
  font-family: "LotteMartDream";
  src: url("//cdn.jsdelivr.net/korean-webfonts/1/corps/lottemart/LotteMartDream/LotteMartDreamMedium.woff2")
      format("woff2")
}
.container {
  width: 100%;
}
.sector{
  text-align:center;
  height:100vh;
}
</style>