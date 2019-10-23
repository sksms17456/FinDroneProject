<template>
    <v-container grid-list-xs background-color="black">
        <v-layout row wrap>
            <v-flex xs12 fluid>
                <div class="wrapper">
                    <img id="slide" src="http://lorempixel.com/output/cats-q-c-100-100-4.jpg" />
                </div>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
export default {
    name:'Intro',
    data(){
        return{
            show:true
        }
    },
    methods:{
        goHome(){
            this.$emit('intro',this.tile)
        }
    }
}
</script>

<style scoped>
.wrapper {
    position: relative;
    overflow: hidden;
    width: 100px;
    height: 100px; 
    border: 1px solid black;
}

#slide {
    position: absolute;
    left: -100px;
    width: 100px;
    height: 100px;
    background: blue;
    transition: 1s;
}

.wrapper:hover #slide {
    transition: 1s;
    left: 0;
}
</style>