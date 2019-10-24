<template>
    <div>
        <!-- Central Image Banner -->
        <ImgBanner call="central" height="100vh">
            <div style="line-height:1.1em; font-weight:bold;text-align:center" slot="text" class="layout align-center justify-center row fill-height">
                <br/> WATCH THE DRONES
                <br/> FIND YOUR TARGET
            </div>
        </ImgBanner>        

        <!-- Simulation Part -->
        <v-flex id="simulation">
            <v-layout row wrap>
                <v-flex xs12 md3>
                    <LogsMonitor />
                </v-flex>

                <v-flex xs12 md9>
                    <MapMonitor />
                    <DroneMonitor ref="droneMonitor" />
                </v-flex>
            </v-layout>
        </v-flex>
    </div>
</template>

<script>
import ImgBanner from '../components/ImgBanner'
import DroneMonitor from '../components/DroneMonitor'
import MapMonitor from '../components/MapMonitor'
import LogsMonitor from '../components/LogsMonitor'
import axios from 'axios'
import $ from 'jquery'

  export default {
    name:"Central",
    components:{
      ImgBanner,
      DroneMonitor,
      MapMonitor,
      LogsMonitor
    },
    data () {
      return {
        simulationOffset:0
      }
    }
  }
</script>

<style scoped>
#simulation {
  height: 100vh;
  margin: 0;
  padding: 0;
}

</style>