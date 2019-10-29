<template>
    <div>
        <ImgBanner call="service" height="100vh">
            <div style="line-height:1.1em; font-weight:bold;text-align:center" slot="text" class="layout align-center justify-center row fill-height">
                <br/> WATCH THE DRONES
                <br/> FIND YOUR TARGET
            </div>
        </ImgBanner>

        <v-layout row wrap>
            <h1>시스템 구성도</h1>
        </v-layout>
        
        <v-layout row wrap>
            <h1>수색 알고리즘</h1>    
        </v-layout>

        <v-layout row wrap>
            <h1></h1>
        </v-layout>

    </div>
</template>

<script>
import ImgBanner from '../components/ImgBanner'

export default {
    name:'Service',
    components:{
        ImgBanner
    }
}
</script>