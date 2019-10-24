<template>
  <div>
    <ImgBanner call="central" height="100vh">
      <div style="line-height:1.1em; font-weight:bold;text-align:center" slot="text" class="layout align-center justify-center row fill-height">
               
         <br/> WATCH THE DRONES
         <br/> FIND YOUR TARGET
      </div>
    </ImgBanner>

    <div class="layout align-center justify-center" ma-0>
    <v-btn flat dark @click="goDown" round class="text-xs-center hidden-sm-and-down">
      <v-icon dark class="bounce_ball" style="margin:auto; font-weight:bold; color:white;">mdi mdi-arrow-down</v-icon>
    </v-btn>
    </div>

    <v-container grid-list-xs id="simulation">
        <h1 style="text-align:center">실시간 드론 중계 현황</h1>
        <v-layout row wrap style="margin-top:10px">
            <v-flex xs12 md4>
              <v-card>
                    <v-card-title primary-title class="justify-center">
                        Target Log Information
                    </v-card-title>
                    <v-divider></v-divider>
                    <v-card-text>
                      <template>
                        <v-data-table
                          :headers="headers"
                          :items="target"
                           class="elevation-1"
                        >
                          <template v-slot:items="props">
                            <td class="text-xs-right">{{ props.item.time }}</td>
                            <td class="text-xs-right">{{ props.item.posy }}</td>
                            <td class="text-xs-right">{{ props.item.posx }}</td>
                            <td class="text-xs-right">{{ props.item.posz }}</td>
                          </template>
                        </v-data-table>
                      </template>
                    </v-card-text>
                </v-card>
            </v-flex>

            <v-flex xs12 md8>
                <v-card>
                    <v-card-title primary-title class="justify-center">
                        Map Pin
                    </v-card-title>
                    <v-divider></v-divider>
                    <v-card-text>
                        핀 찍는 이미지 파일 전송하는 거 만들어줘요~ 플리즈~
                        <v-img
                        :src="getImgUrl('mappin.gif')"
                        height="200px"
                        >
                        </v-img>
                    </v-card-text>
                </v-card>
                <v-layout row wrap>
              <v-flex v-for="(drone,index) in drones" :key="index" xs4>
                <v-card >
                    <v-card-title primary-title class="justify-center">
                        Drone - {{index+1}} 화면
                    </v-card-title>
                    <v-divider></v-divider>
                    <v-card-text>
                        드론 {{index+1}}} 화면 보여줘요~
                        <div class="v-responsive v-image droneImg" :id="index">
                            <div class="v-responsive__sizer" style="padding-bottom: 66.6667%;"></div>
                            <img class="v-image__image v-image__image--cover" :id="'drone_img_'+index" :src="require('../../../drone_output/output'+index+'.jpg')"/>
                            <div class="v-responsive__content"></div>
                        </div>
                    </v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
            </v-flex>
        </v-layout>
    </v-container>
  </div>
</template>

<script>
import ImgBanner from '../components/ImgBanner'
import axios from 'axios'
import $ from 'jquery'

  export default {
    name:"Central",
    components:{
      ImgBanner
    },
    data () {
      return {
        simulationOffset:0,
        headers:[
          // {
          //   text: 'Target',
          //   align: 'left',
          //   sortable: false,
          //   value: 'name'
          // },
          { text: '시간', value: 'time' },
          { text: 'Y좌표', value: 'posy' },
          { text: 'X좌표', value: 'posx' },
          { text: 'Z좌표', value: 'posz' }
        ],
        target:[
          {
            name:'Target',
            src:'footerlogo.png',
            time:'',
            posy:'',
            posx:'',
            posz:'',
            state:''
          }],
        drones:[
          {
            name:'Drone1',
            src:'footerlogo.png',
            time:'',
            posy:'',
            posx:'',
            posz:'',
            state:''
          },
          {
            name:'Drone2',
            src:'footerlogo.png',
            time:'',
            posy:'',
            posx:'',
            posz:'',
            state:''
          },
          {
            name:'Drone3',
            src:'footerlogo.png',
            time:'',
            posx:'',
            posy:'',
            posz:'',
            state:''
          }]
      }
    },
    created(){
      this.getImgUrlFromBack();
    },
    methods: {
      getImgUrl(img){
        return require('../assets/'+img)
      },
      getImgUrlFromBack(){
        var curThis = this
        this.polling = setInterval(() => {
          const path = `/api/getImg`
            axios.get(path)
            .then(response => {
              const contain = [response.data.iter0, response.data.iter1, response.data.iter2]

              for(var i=0; i<3; i++){
                curThis.drones[i].src = contain[i]
                const path = '/api/getDroneImg?drone='+i +'&num_img=' + contain[i]
                console.log(curThis.drones[i].src)
                $('#drone_img_'+ i).attr("src", path)
              }
            })
            .catch(error => {
              console.log(error)
            })
          }, 1000)
      },
      goDown(){
        this.simulationOffset = $('#simulation').offset();
        $('html, body').animate({scrollTop : this.simulationOffset.top-100}, 400);
      }
    }
  }
</script>

<style scoped>
.bounce_ball {
    background: transparent;
    width: 80px;
    height: 35px;
    background-size: 100%;
    left: 50%;
    bottom: 10px;
    margin-left: -22px;
    z-index: 4;
    opacity: 0.9;
    -webkit-animation: bounceball 0.9s infinite ease-out;
}
.bounce_ball:hover {
    background-color: black;
    border-radius: 10rem;
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