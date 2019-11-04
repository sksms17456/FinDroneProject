<template>
    <div class="sector" id="applicationBox">
      <h1 id="appTitle">APPLICATION</h1>
      <v-container fluid id="appContainer">
        <v-layout row wrap>
          
          <v-flex xs6>
            <h1>드론 이제 FinDrone으로 쉬워집니다.</h1>
                <v-tabs fixed-tabs>
                  <v-tab v-for="(service,index) in services" :key="index" ripple>{{service.card_title}}</v-tab>

                  <v-tab-item v-for="(service,index) in services" :key="index">
                    <h1>{{ service.card_text }}</h1>
                  </v-tab-item>
                </v-tabs>            
          </v-flex>

          <v-flex xs6>
            <img src="../assets/monitor.jpg" contain style="width:700px;height:500px"/>  
          </v-flex>
          
        </v-layout>
          
        </v-container>
    </div>
</template>

<script>
export default {
    data() {
    return {
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
  margin-top:20px;
  margin-bottom:20px;
}

#appContainer{
  max-width: 1400px;
  width: 1400px;
  height: 570px;
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
</style>