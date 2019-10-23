<template>
  <v-toolbar id="deskToolbar" style="z-index:19; box-shadow:none;" fixed>
    <v-spacer></v-spacer>
      <v-container text-md-center>
        <v-toolbar-side-icon class="hidden-sm-and-up"></v-toolbar-side-icon>
        <v-toolbar-items class="hidden-sm-and-down" >
          <v-flex xs3 text-md-right><v-btn to="/home" flat>Home</v-btn></v-flex>
          <v-flex xs2><v-btn to="/about" flat>About</v-btn></v-flex>
          <v-card style="background:transparent;font-size:1.7em" flat to="/">
              <v-img id="headerLogo" :src="getImgUrl('dronelogo.png')" contain/>
              <v-flex xs2><v-btn id="headerTitle" flat large style="text-transform : none !important" to="/">FinDrone</v-btn></v-flex>
          </v-card>
          <v-flex xs2><v-btn to="/service" flat>Service</v-btn></v-flex>
          <v-flex xs3 text-md-left><v-btn to="/central" flat>Central</v-btn></v-flex>
      </v-toolbar-items>
      </v-container>
      <v-spacer></v-spacer>
     <!-- <v-toolbar-items>
        <v-btn flat>Log In - Sign Up</v-btn>
        <v-btn flat>Log Out</v-btn>
     </v-toolbar-items> -->
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
    $(document).ready(function() {
      $(window).scroll(function() {
        var deskToolbarElement = document.getElementById("deskToolbar");
        // var mobileToolbarElement = document.getElementById( "mobileToolbar"); 
        var headerLogoElement = document.getElementById("headerLogo");
        var headerTitelElement = document.getElementById("headerTitle");
        var headerBtn = document.getElementsByClassName("v-btn");
        if ($(window).scrollTop() < 300) {
          deskToolbarElement.style.background = "transparent";
          deskToolbarElement.style.boxShadow = "none";
          deskToolbarElement.style.height="25vh";
          $('.v-btn').css('color','white');
          headerLogoElement.style.height="auto";
          headerTitelElement.style.fontSize="1.7em";
          // mobileToolbarElement.style.background = "transparent";
          // mobileToolbarElement.style.boxShadow = "none";
          } else {
            deskToolbarElement.style.background = "#f1f0f0f2";
            deskToolbarElement.style.boxShadow ="0px 1px 10px grey";
            $('.v-btn').css('color','black');
            deskToolbarElement.style.height="16vh"
            headerLogoElement.style.height="7vh";
            headerTitelElement.style.fontSize="1.1em";
            // mobileToolbarElement.style.background = "white";
            // mobileToolbarElement.style.boxShadow ="0px 1px 10px grey";
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

</style>