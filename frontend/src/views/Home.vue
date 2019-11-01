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
  },
  methods: {
    getImgUrl(img) {
      return require("../assets/" + img);
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
}
</style>