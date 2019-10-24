<template>
    <!-- Arrow Down Button -->
    <div class="layout align-center justify-center" ma-0>
        <v-btn flat dark @click="goDown" round class="hidden-sm-and-down">
            <v-icon dark class="bounce_ball">mdi mdi-arrow-down</v-icon>
        </v-btn>
    </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'goDownBtn',
  methods: {
    goDown(){
      console.log("goDown")
      this.simulationOffset = $('#simulation').offset();
      $('html, body').animate({scrollTop : this.simulationOffset.top}, 400);
    }
  }
}
</script>

<style scoped>
.bounce_ball {
    /* position: relative; */
    width: 80px;
    height: 35px;
    border-radius: 10rem;
    opacity: 0.9;
    -webkit-animation: bounceball 0.9s infinite ease-out;
}
.bounce_ball:hover {
    background-color: black;
}
@-webkit-keyframes bounceball {
    0%,
    20%,
    100% {
        -webkit-transform: translateY(-60px);
    }
    30% {
        -webkit-transform: translateY(-75px);
    }
    50% {
        -webkit-transform: translateY(-51px);
    }
}
</style>