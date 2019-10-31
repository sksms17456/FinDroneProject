<template>
  <v-toolbar id="deskToolbar" fixed>
    <v-container id="headerContainer">
      <v-toolbar-items>
        <v-btn to="/home" flat id="headerLogoBox">
          <!-- <v-img id="headerLogo" :src="getImgUrl('dronelogo.png')" contain/> -->
          <v-img id="headerLogo" :src="getImgUrl('logoText.png')" contain/>
        </v-btn>
        <div><v-btn to="/about" flat>About</v-btn></div>
        <div><v-btn to="/system" flat>System</v-btn></div>
        <div><v-btn to="/service" flat>Service</v-btn></div>
        <div><v-btn to="/application" flat>Application</v-btn></div>
        <div><v-btn to="/central" flat>Central</v-btn></div>
      </v-toolbar-items>
    </v-container>
  </v-toolbar>
</template>

<script>
import $ from "jquery";

export default {
  methods:{
    getImgUrl(img){
      return require('../assets/'+img)
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
  },
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
}

#headerContainer {
  margin: 0;
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