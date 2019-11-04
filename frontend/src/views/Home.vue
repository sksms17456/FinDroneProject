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
      if(move=='about'){
        this.ableAbout()
      } else {
        this.disableAbout()
      }

      if(move=='system'){
        this.ableSystem();
      } else {
        this.disableSystem();
      }

      if(move=='service'){
        this.ableService();
      } else {
        this.disableService();
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

      var vertical = document.getElementById('vertical_line_system');
      var systemTitle = document.getElementById('systemTitle');
      var computerBackground = document.getElementById('computerBackground');
      var computer = document.getElementById('computer');
      vertical.classList.add('on');
      systemTitle.classList.add('on');
      computerBackground.classList.add('on');
      computer.classList.add('on');
        
      $('#structure').animate({'opacity':'1','margin-left':'0px'},1500);
    },
    disableSystem(){
      var st0 = document.getElementById('sysTitle0');
      st0.classList.remove("systemMTitle");

      var st1 = document.getElementById('sysTitle1');
      st1.classList.remove("systemSTitle1");

      var st2 = document.getElementById('sysTitle2');
      st2.classList.remove("systemSTitle2");

      var vertical = document.getElementById('vertical_line_system');
      var systemTitle = document.getElementById('systemTitle');
      var computerBackground = document.getElementById('computerBackground');
      var computer = document.getElementById('computer');
      vertical.classList.remove('on');
      systemTitle.classList.remove('on');
      computerBackground.classList.remove('on');
      computer.classList.remove('on');

      $('#structure').animate({'opacity':'0','margin-left':'-300px'},1500);
    },
    ableService(){
      var vertical = document.getElementById('vertical_line_service');
      var lightbulb = document.getElementById('icon_service');
      var title = document.getElementById('service_Title');
      var card0 = document.getElementById('Card_0');
      var card1 = document.getElementById('Card_1');
      var card2 = document.getElementById('Card_2');
      var ai_img = document.getElementById('ai_img');
      var ai_text = document.getElementById('ai_text');
      vertical.classList.add('on');
      lightbulb.classList.add('on');
      title.classList.add('on');
      card0.classList.add('on');
      card1.classList.add('on');
      card2.classList.add('on');
      ai_img.classList.add('on');
      ai_text.classList.add('on');
    },
    disableService(){
      var vertical = document.getElementById('vertical_line_service');
      var lightbulb = document.getElementById('icon_service');
      var title = document.getElementById('service_Title');
      var card0 = document.getElementById('Card_0');
      var card1 = document.getElementById('Card_1');
      var card2 = document.getElementById('Card_2');
      var ai_img = document.getElementById('ai_img');
      var ai_text = document.getElementById('ai_text');
      vertical.classList.remove('on');
      lightbulb.classList.remove('on');
      title.classList.remove('on');
      card0.classList.remove('on');
      card1.classList.remove('on');
      card2.classList.remove('on');
      ai_img.classList.remove('on');
      ai_text.classList.remove('on');
    },
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
#applicationBox {
  height:73vh;
}
</style>