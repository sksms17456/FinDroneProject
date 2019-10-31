<template>
    <!-- Arrow Down Button -->
    <div class="layout align-center justify-center" ma-0>
        <v-btn flat @click="goDown" round class="hidden-sm-and-down bounce_ball" icon>
            <i style="color:white" class="fas fa-arrow-down"></i>
            <!-- <v-icon dark class="bounce_ball" icon ></v-icon> -->
        </v-btn>
    </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'goDownBtn',
  data(){
      return{
          scrollTop:0,
          serviceOffset:0
      }
  },
  methods: {
    goDown(){
      this.serviceOffset = $('#serviceMainTitle').offset();
      $('html, body').animate({scrollTop : this.serviceOffset.top-100}, 400);
    }
  }
}
</script>

<style scoped>
.bounce_ball {
    width: 80px;
    height: 35px;
    border-radius: 10rem;
    opacity: 0.9;
    animation: bounceball 0.9s infinite ease-out;
}
.bounce_ball:hover {
    background-color: black;
}
@keyframes bounceball {
    0%,
    20%,
    100% {
        transform: translateY(-60px);
    }
    30% {
        transform: translateY(-75px);
    }
    50% {
        transform: translateY(-51px);
    }
}
</style>