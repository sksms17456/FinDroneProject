<template>
  <div>
    <!-- 홈 화면(sector1) --> 
   <ImgBanner>
      <div style="line-height:1.1em; font-weight:bold;" slot="text" class="layout align-center justify-center row fill-height">
               FinDrone
         <br/>
         <br/>FIND YOUR TARGET
      </div>
    </ImgBanner>
    
    <!-- 서비스 단계 표시(sector2) -->
    <v-flex mr-4 xs8 style="height:40px; border-bottom:3px solid black;"></v-flex>
    <h1> 드론을 이용한 서비스 단계 </h1>
     <v-container fluid grid-list-md>
        <v-layout row justify-center>
            <v-flex v-for="(step,index) in steps" :key="index" xs4>
                <v-card class="hidden-sm-and-down; ma-4">
                    <v-img
                    :src="step.src"
                    height="200"
                    ></v-img>

                    <v-card-title primary-title>
                    <div>
                        <h3 class="headline mb-0">{{ step.card_title }}</h3>
                        <div> {{ step.card_text }} </div>
                    </div>
                    </v-card-title>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>

    <!-- 주요 서비스 소개(sector3) -->
    <v-flex mr-4 xs8 style="height:40px; border-bottom:3px solid black;"></v-flex>
    <h1> 플랫폼 주요 기능 </h1>
    <v-container fluid grid-list-md>
      <v-tabs
        color="black"
        dark
        slider-color="white"
        centered
      >
        <v-tab
          v-for="(service,index) in services"
          :key="index"
          ripple
        >
        {{service.card_title}}
        </v-tab>
        <v-tab-item
          v-for="(service,index) in services"
          :key="index"
        >
          <v-layout row wrap mt-4>
            <v-flex xs6>
              <v-card>
                <v-card-title primary-title>
                  {{service.card_title}}
                </v-card-title>
                <v-card-text>{{ service.card_text }}</v-card-text>
              </v-card>
            </v-flex>

            <v-flex xs6>
              <v-card>
                <v-img
                  :src="service.src"
                  height="200px"
                  >
                  </v-img>
              </v-card>
            </v-flex>
          </v-layout>
        </v-tab-item>
      </v-tabs>
    </v-container>
 </div>
</template>

<script>
import ImgBanner from '../components/ImgBanner'

export default {
  name: 'Home',
  components:{
    ImgBanner
  },
  methods:{
    getImgUrl(img){
      return require('../assets/'+img)
    }
  },
  data(){
    return{
      steps:[
        {
          src:this.getImgUrl('launch.png'),
          card_title:'STEP 01 FLY',
          card_text:'자 날아봅시다~'
                    
        },
        {
          src:this.getImgUrl('detect.png'),
          card_title:'STEP 02 DETECT',
          card_text:'타겟을 찾아 봅시다'
        },
        {
          src:this.getImgUrl('stop.png'),
          card_title:'STEP 03 FIND & WAIT',
          card_text:'찾았당!'
                    
        }],
        services:[
        {
          src:this.getImgUrl('monitoring.gif'),
          card_title:'수색 현장 모니터링',
          card_text:'수색하고 있는 드론의 화면을 웹상에서 간편하게 볼 수 있습니다.'
        },
        {
          src:this.getImgUrl('mappin.gif'),
          card_title:'타겟 위치 변화 시각화',
          card_text:'지정한 타겟이 이동하는 위치를 쉽게 파악할 수 있습니다.'
        }]
    }
  }
}
</script>

