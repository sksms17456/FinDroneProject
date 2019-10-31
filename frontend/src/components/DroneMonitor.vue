<template>
    <v-layout row wrap>
        <v-flex v-for="(drone,index) in drones" :key="index" xs4>
            <v-card>
                <v-card-title primary-title class="justify-center py-2">
                    Drone - {{index+1}} 화면
                </v-card-title>
                <v-divider></v-divider>

                <v-card-text>
                    <div class="v-responsive v-image droneImg" :id="index">
                        <div class="v-responsive__sizer" style="padding-bottom: 66.6667%;"></div>
                        <img class="v-image__image v-image__image--cover" style="height:25vh" :id="'drone_img_'+index" :src="require('../../../drone_output/output'+index+'.jpg')"/>
                        <div class="v-responsive__content"></div>
                    </div>
                </v-card-text>
            </v-card>
        </v-flex>
    </v-layout>
</template>

<script>
import axios from 'axios'
import $ from 'jquery'

export default {
  name: 'DroneMonitor',
  data () {
    return {
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
    }
  },
  beforeDestroy() {
    clearInterval(this.polling)
  },
}
</script>

<style>

</style>
