<template>
    <div class="sector">
      <p class="mainTitle">SYSTEM.</p>
      <h1>시스템을 소개합니다.</h1>
      <v-layout row justify-center>
        <v-flex v-for="(step,index) in steps" :key="index" xs4>
          <v-card class="hidden-sm-and-down; ma-4">
            <v-img pd-4 :src="step.src" aspect-ratio="1.7" contain></v-img>
            <v-card-title primary-title style="text-align:center">
              <div style="width:100%">
                <h3 class="headline mb-0">{{ step.card_title }}</h3>
                <div>{{ step.card_text }}</div>
              </div>
            </v-card-title>
          </v-card>
        </v-flex>
      </v-layout>
    </div>
</template>

<script>
export default {
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
    methods: {
        getImgUrl(img) {
            return require("../assets/" + img);
        }
    }
}
</script>