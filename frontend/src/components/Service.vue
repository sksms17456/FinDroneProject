<template>
    <div class="sector" id="serviceBox">
      <!-- Title -->
      <div id="vertical_line_service"></div>
      <svg id="svg" viewBox="0 0 24 24">
        <path id="icon_service" fill="#0005" d="M9.5,8.5L11,10L8,13L11,16L9.5,17.5L5,13L9.5,8.5M14.5,17.5L13,16L16,13L13,10L14.5,8.5L19,13L14.5,17.5M21,2H3A2,2 0 0,0 1,4V20A2,2 0 0,0 3,22H21A2,2 0 0,0 23,20V4A2,2 0 0,0 21,2M21,20H3V6H21V20Z" />
      </svg>
      <p id="service_Title">SERVICE</p>

      <v-flex>
        <v-layout class="px-5">
          <!-- Drone Controll Contents -->
          <v-flex row justify-center xs4 px-5>
            <v-layout v-for="(step,index) in steps" :key="index">
              <v-card :id="getCardId(index)" class="hidden-sm-and-down py-0" style="box-shadow:none">
                <v-img pd-1 :src="step.src" aspect-ratio="1.7" contain style="height:10vh"></v-img>
                <v-card-title primary-title style="text-align:center;" class="py-4">
                  <div style="width:20.8vw; height:70px">
                    <h3 class="headline mb-0">{{ step.card_title }}</h3>
                    <div>{{ step.card_text }}</div>
                  </div>
                </v-card-title>
              </v-card>
            </v-layout>
          </v-flex>

          <!-- AI _ Object Detection Contents -->
          <v-flex xs8>
            <v-img id="ai_img" :src="getImgUrl('AI.png')" contain style="width:90%"></v-img>
            <v-flex id="ai_text">
              <v-layout class="aiText">
                <span class="bold">MobileNet : </span>&nbsp;드론 cpu만으로 작동할 수 있는 가벼운 모델 사용
              </v-layout>
              <v-layout class="aiText">
                <span class="bold">Trace : </span>&nbsp;현재 드론 위치와 타겟 위치를 기반으로 추적 알고리즘 작동
              </v-layout>
            </v-flex>
          </v-flex>
        </v-layout>
      </v-flex>

    </div>
</template>

<script>
export default {
  name:'Service',
  methods: {
    getImgUrl(img) {
      return require("../assets/" + img);
    },
    getCardId(id) {
      return 'Card_' + id;
    }
  },
  data(){
    return{
      steps: [
        {
          src: this.getImgUrl("launch.png"),
          card_title: "STEP 01 LAUNCH",
          card_text: "사람, 동물 등의 목표물을 입력하면 3대의 드론이 입력된 목표물을 찾기위해 이륙합니다."
        },
        {
          src: this.getImgUrl("detect.png"),
          card_title: "STEP 02 DETECT",
          card_text: "Spin Square 알고리즘을 기반으로 지정된 영역을 수색하기 시작합니다."
        },
        {
          src: this.getImgUrl("stop.png"),
          card_title: "STEP 03 TRACE",
          card_text: "목표물을 발견하면 각 드론들이 전체 수색 / 근방 수색 / 타겟 추적으로 전환되어 임무를 수행합니다."
        }
      ]
    }
  },
}
</script>

<style scoped>
#serviceBox {
  padding-top: 0!important;
}

#svg {
  width: 50px;
  height: 50px;
  transform: rotate(180deg);
}

#vertical_line_service {
  position: relative;
  left: 49.9%;
  content: '';
  width: 3px;
  height: 3.5em;
  background-color: rgba(0, 0, 0, 0.3);
  transition: background-color 2s ease;
}

#vertical_line_service.on {
  background-color: #11436a!important;
}

#icon_service {
  transition: fill 2s ease;
}

#icon_service.on {
  fill: #11436a;
}

#service_Title {
  text-transform: uppercase;
  font-size: 50px;
  margin: 0;
  font-family: 'Baloo Paaji', cursive;
  color: rgba(111, 15, 13, 0.7);
  transition: text-shadow 3s ease, color 2s ease;
}

#service_Title.on {
  color: #11436a;
  text-shadow: #d5ad5899 2.7px 4.985px;
}

.aiText {
  font-size: 1.55rem;
  padding-bottom: 0.5rem;
}

.bold {
  font-weight: bold;
}

#Card_0.on {
  animation: fade_in_left 2s;
}
#Card_1.on {
  animation: fade_in_left 2.7s;
}
#Card_2.on {
  animation: fade_in_left 3.4s;
}

#ai_img.on {
  animation: fade_in_bottom 4s;
}

#ai_text {
  margin-top: 35px;
  opacity: 1;
}
#ai_text.on {
  animation: fade_in 4s;
}

@keyframes fade_in_left {
  0% { opacity: 0; margin-left:-100% }
  50% { opacity: 0; margin-left:-100% }
  100% { opacity: 1; margin-left:0 }
}

@keyframes fade_in_bottom {
  0% { opacity: 0; margin-bottom:-50% }
  50% { opacity: 0; margin-bottom:-50% }
  100% { opacity: 1; margin-bottom:0 }
}

@keyframes fade_in {
  0% { opacity: 0 }
  80% { opacity: 0 }
  100% { opacity: 1 }
}
</style>