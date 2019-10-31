<template>
    <div class="sector">
      <p class="mainTitle">APPLICATION</p>
      <v-tabs color="black" dark slider-color="white" centered>
        <v-tab v-for="(service,index) in services" :key="index" ripple>{{service.card_title}}</v-tab>
        <v-tab-item v-for="(service,index) in services" :key="index">
          <v-layout row wrap mt-4>
            <v-flex xs6>
              <v-card style="text-align:center;">
                
                <v-card-text>
                  <h1>{{service.card_title}}</h1><br/>
                  {{ service.card_text }}</v-card-text>
                <v-divider></v-divider>
                <v-card-text> 기능 더 알아보기 
                    <v-btn icon id="goService">
                      <i class="fas fa-arrow-right"></i>
                    </v-btn>
                </v-card-text>
              </v-card>
            </v-flex>

            <v-flex xs6>
              <v-card>
                <v-img :src="service.src" aspect-ratio="1.7" contain></v-img>
              </v-card>
            </v-flex>
          </v-layout>
        </v-tab-item>
      </v-tabs>
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
#goService:hover{
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
}
</style>