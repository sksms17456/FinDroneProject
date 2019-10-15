<template>
   <ImgBanner>
      <div style="line-height:1.1em; font-weight:bold;" slot="text">
               FinDrone
         <br/>
         <br/>FIND YOUR TARGET
      </div>
    </ImgBanner>

</template>

<script>
import ImgBanner from '../components/ImgBanner'

export default {
  name: 'Home',
  components:{
    ImgBanner
  }
}
</script>
