<template>
    <v-card>
        <v-card-text style="padding:0">
            <v-img
              :src="getImgUrl(mapImg)"
              height="65vh"
            >
            </v-img>
        </v-card-text>
    </v-card>
</template>

<script>
export default {
  name: 'MapMonitor',
  data () {
    return {
      mapImg: 'mappin.gif'
    }
  },
  methods: {
    getImgUrl(img){
      return require('../assets/'+img)
    },
  }
}
</script>

<style>

</style>
