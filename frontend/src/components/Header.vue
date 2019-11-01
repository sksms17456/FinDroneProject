<template>
  <v-toolbar id="deskToolbar" fixed>
    <v-container id="headerContainer">
      <v-toolbar-items>
        <v-btn v-scroll="onScroll"
               @click="toTop"
               to="/home"
               flat 
               id="headerLogoBox">
          <v-img id="headerLogo" :src="getImgUrl('logoText.png')" contain/>
        </v-btn>
        <div>
          <v-btn v-scroll="onScroll"
                 @click="toAbout"
                 flat>About</v-btn>
        </div>
        <div>
          <v-btn v-scroll="onScroll"
                 @click="toSystem"
                 flat>System</v-btn>
        </div>
        <div>
          <v-btn v-scroll="onScroll"
                 @click="toService"
                 flat>Service</v-btn>
        </div>
        <div>
          <v-btn v-scroll="onScroll"
                 @click="toApplication"
                 flat>Application</v-btn>
        </div>
        <div>
          <v-btn to="/central" flat>Central</v-btn>
        </div>
      </v-toolbar-items>
    </v-container>
  </v-toolbar>
</template>

<script>
import $ from "jquery";
import { eventBus } from '../main'
export default {
  name: 'mainHeader',
  methods:{
    getImgUrl(img){
      return require('../assets/'+img)
    },
    toTop() {
      window.scrollTo({
          top: 0,
          left: 0,
          behavior: "smooth"
      });
    },
    toAbout() {
      window.scrollTo({
          top: $('#aboutBox').offset().top - $('#deskToolbar').height(),
          left: 0,
          behavior: "smooth"
      });
    },
    toSystem() {
      window.scrollTo({
          top: $('#systemBox').offset().top - $('#deskToolbar').height(),
          left: 0,
          behavior: "smooth"
      });
      
      eventBus.$emit("goToMenu",'system');
    },
    toService() {
      window.scrollTo({
          top: $('#serviceBox').offset().top - $('#deskToolbar').height(),
          left: 0,
          behavior: "smooth"
      });
    },
    toApplication() {
      window.scrollTo({
          top: $('#applicationBox').offset().top - $('#deskToolbar').height(),
          left: 0,
          behavior: "smooth"
      });
    },
    onScroll() {
      this.offsetTop = window.scrollY;
    }
  },
  mounted() {
    var curThis = this
    $(document).ready(function() {
      $(window).scroll(function() {
        var deskToolbarElement = document.getElementById("deskToolbar");
        var headerLogoElement = document.getElementById("headerLogo");
        var headerBtn = document.getElementsByClassName("v-btn");

        if(curThis.$route.path === '/central' || curThis.$route.path === '/rootmap'){
          deskToolbarElement.style.display = "none";
        } else {
          if ($(window).scrollTop() < 300) {
            deskToolbarElement.style.background = "transparent";
          }
          else {
            deskToolbarElement.style.background = "#fff";
          }
        }
      }).scroll();
    });
  }
}
</script>

<style scoped>
.v-btn{
  font-size:1.55em;
  font-weight:bold;
}
.v-btn:hover{
  background-color: transparent;
}

.v-btn--active:before, .v-btn:hover:before, .v-btn:focus:before {
  background-color: transparent;
  border-bottom: 2px solid black;
  opacity: 1;
}

#deskToolbar {
  box-shadow: none;
  background-color: transparent;
}

#headerContainer {
  margin: 0;
  padding-left: 0;
}

#headerLogoBox {
  margin-right: 10px;
  border-right: 1.7px solid gray;
}

#headerLogoBox::before {
  border-bottom: none;
}

#headerLogoBox:hover {
  background-color: rgba(0,0,0,0.1);
}

#headerLogo {
  width: 80px;
  padding-right: 50px;
  height: 30px;
}

</style>