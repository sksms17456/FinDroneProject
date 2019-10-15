<template>
    <div>
        <v-img :src="getImgUrl('baekdu.jpg')" aspect-ratio="1.7" :height="height">
            <v-layout align-center justify-center row fill-height>
                <v-flex text-xs-center>
                    <span
                        class="text-shadow display-2 text-weight"
                        style="font-size:15vmin!important; color:white"
                    >
                        <slot name="text" />
                    </span>
                </v-flex>
            </v-layout>
        </v-img>
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
    }

}
</script>