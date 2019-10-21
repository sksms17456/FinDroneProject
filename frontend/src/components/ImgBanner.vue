<template>
  <div>
    <div v-if="call==='home'">
    <v-carousel 
    aspect-ratio="1.7" 
    :height="height">

        <v-carousel-item
         v-for="(item,i) in items"
         :key="i"
         :src="item.src"
        >
               <span
                class="text-shadow display-2 text-weight"
                style="font-size:15vmin!important; color:white"
                >
                <slot name="text" />
                </span>
        </v-carousel-item>
    </v-carousel>
    </div>
    <div v-else-if="call==='central'">
        <v-img :src="getImgUrl('baekdu.jpg')" :height="height">
            <span
                class="text-shadow display-2 text-weight"
                style="font-size:15vmin!important; color:white"
                >
                <slot name="text" />
                </span>
        </v-img>
    </div>
  </div>
</template>

<script>
export default {
    name:'ImgBanner',
    props: {
        call:{type:String, default:"home"},
        text: { type: String },
        height: { type: String, default: "100vh" }
    },
    methods:{
        getImgUrl(img){
            return require('../assets/'+img)
        }
    },
    data(){
        return {
            items:[
                {
                    src:this.getImgUrl('valley.gif')
                },
                {
                    src:this.getImgUrl('mabig.gif')
                },
                {
                    src:this.getImgUrl('beach.gif')
                }
            ]
        }
    }

}
</script>

