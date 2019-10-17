<template>
  <div>
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
                style="font-size:15vmin!important; color:white; align-text:center"
                >
                <slot name="text" />
                </span>
        </v-carousel-item>
    </v-carousel>
  </div>
</template>

<script>
export default {
    name:'ImgBanner',
    props: {
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

