<template>
  <v-toolbar id="deskToolbar" style="background:transparent; color:white; z-index:19; box-shadow:none;" fixed>
      <v-container text-md-center>
        <v-toolbar-side-icon class="hidden-sm-and-up"></v-toolbar-side-icon>
        <v-toolbar-items class="hidden-sm-and-down">
          <v-flex xs3 text-md-right><v-btn to="/" flat>Home</v-btn></v-flex>
          <v-flex xs2><v-btn to="/about" flat>About</v-btn></v-flex>
          <v-card style="background:transparent;font-size:1.7em" flat to="/">
              <v-img :src="getImgUrl('dronelogo.png')"/>
              <v-flex xs2><v-btn flat large style="text-transform : none !important">FinDrone</v-btn></v-flex>
          </v-card>
          <v-flex xs2><v-btn to="/service" flat>Service</v-btn></v-flex>
          <v-flex xs3 text-md-left><v-btn to="/central" flat>Central</v-btn></v-flex>
      </v-toolbar-items>
      </v-container>
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
                $(window)
                    .scroll(function() {
                        var deskToolbarElement = document.getElementById(
                            "deskToolbar"
                        );
                        // var mobileToolbarElement = document.getElementById(
                        //     "mobileToolbar"
                        // );
                        if ($(window).scrollTop() < 700) {
                            deskToolbarElement.style.background = "transparent";
                            deskToolbarElement.style.boxShadow = "none";
                            deskToolbarElement.style.color = "white";

                            // mobileToolbarElement.style.background = "transparent";
                            // mobileToolbarElement.style.boxShadow = "none";
                        } else {
                            deskToolbarElement.style.background = "white";
                            deskToolbarElement.style.boxShadow ="0px 1px 10px grey";
                            deskToolbarElement.style.color = "black";

                            // mobileToolbarElement.style.background = "white";
                            // mobileToolbarElement.style.boxShadow ="0px 1px 10px grey";
                        }
                    })
                    .scroll();
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