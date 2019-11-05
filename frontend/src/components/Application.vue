<template>
    <div class="sector" id="applicationBox">
      <h1 id="appTitle">APPLICATION</h1>
      <v-container fluid id="appContainer">
        <v-layout row wrap>
          <v-flex xs6>
            <h1 class="appSubTitle">"FinDrone</h1> <br/>
            <h1 class="appSubTitle">Find All"</h1> <br/>
                <v-tabs fixed-tabs v-model="active">
                  <v-tab v-for="(service,index) in services" :key="index" ripple style="font-weight:bold;">{{service.card_title}}</v-tab>
                  <v-tab-item v-for="(service,index) in services" :key="index" style="padding-top:30px;" >
                    <span class="appSubContents">{{ service.card_text }}</span>
                  </v-tab-item>
                </v-tabs>
          </v-flex>

            <img id="firstImage" class="functionImage" :src='getImgUrl("monitoring.gif")' contain />
            <img id="secondImage" class="functionImage" :src='getImgUrl("mappin.gif")' contain />
            
          <v-flex xs6>
            <!-- <v-img class="functionImage" :src="services[active].src" contain></v-img> -->
            <img :src='getImgUrl("monitor.jpg")' contain style="width:600px;height:400px"/>  
          </v-flex>
          
        </v-layout>
          
        </v-container>
    </div>
</template>

<script>
import $ from 'jquery'

export default {
    data() {
    return {
      active:'0',
      services: [
        {
          src: this.getImgUrl("monitoring.gif"),
          card_title: "수색 현장 모니터링",
          card_text:
            "수색하고 있는 드론의 화면을 웹상에서 간편하게 볼 수 있습니다."
        },
        {
          src: this.getImgUrl("mappin.gif"),
          card_title: "타겟 위치 변화 시각화",
          card_text: "지정한 타겟이 이동하는 위치를 쉽게 파악할 수 있습니다."
        }
      ]
    };
  },
  watch:{
    active:function(){
      switch(this.active){
        case 0:
          $('#secondImage').animate({'opacity':'0','margin-left':'10px'},1000);
          $('#firstImage').animate({'opacity':'1','margin-left':'0px'},1000);
          break;
        case 1:
          $('#firstImage').animate({'opacity':'0','margin-left':'10px'},1000);
          $('#secondImage').animate({'opacity':'1','margin-left':'0px'},1000);
          break;
      }
    }
  },
  methods: {
    getImgUrl(img) {
      return require("../assets/" + img);
    }
  }
}
</script>

<style scoped>
#appTitle{
  font-family: 'Baloo Paaji', cursive;
  font-size: 60px;
  margin-top: 30px;
  margin-bottom:50px;
  color: rgba(111, 15, 13);
  transition: text-shadow 3s ease, color 2s ease;  
}

#appTitle.on{
  color: #11436a;
  text-shadow: #d5ad5899 3.125px 3.98px;
}

.appSubTitle{
  font-family: "LotteMartDream";
  font-size:45px;
}

.v-tabs__item.v-tabs__item--active{
  font-family: "LotteMartDream";
  font-weight: bold;
}

.appSubContents{
  font-family: "LotteMartDream";
  font-size:20px;
}

#appContainer{
  max-width: 1400px;
  width: 1400px;
  height: 570px;
}

.functionImage{
  position: absolute;
  z-index:10; 
  left:825px;
  bottom:290px;
  width:565px;
  height:288px;
}

#firstImage{
  opacity:0;
  margin-left:-10px;
  max-width:100%;
}

#secondImage{
  opacity:0;
  margin-left:-10px;
  max-width:100%;
}


/* #goService:hover{
  margin-left:10px;
  margin-bottom:10px;
  left:10%;
  animation: bounceArrow 0.9s infinite ease-out;
}

@keyframes bounceArrow {
    0%,
    20%,
    100% {
        transform: translateX(-60px);
    }
    30% {
        transform: translateX(-65px);
    }
    50% {
        transform: translateX(-60px);
    }
} */

/* #structure{
  opacity:0;
  margin-left:-300px;
  max-width:100%; */
/* } */

@keyframes fadeInLeft {
    from {
        opacity: 0;
        transform: translateX(20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

</style>