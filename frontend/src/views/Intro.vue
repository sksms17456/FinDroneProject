<template>
<v-container style="height:100vh;" >
    <v-layout row wrap style="height:60vh">
    </v-layout>
    
    <v-layout row wrap style="height:30vh">
        <v-layout row wrap style="vertical-align-mid">
            <v-flex mb-4 px-5 xs5>
                <v-img :src="getImgUrl('launch_drone.png')" contain style="height:100px;widht:100px" ></v-img>
            </v-flex>
            <v-flex xs7>
                <h1 style="font-size:2.5em; padding-top:30px">이륙하시겠습니까?</h1>
            </v-flex>
        </v-layout>
        
        <v-layout row wrap>
            <div class="slide-wrap center">
                <label >밀어서 이륙</label>
                <input type="range" min="0" max="100" value="0"/>
            </div>
        </v-layout>
    </v-layout>

    <!-- <v-layout row wrap>
        <v-flex xs4>
            <v-img :src="getImgUrl('control_left.png')" contain style="height:100px;widht:100px"></v-img>
        </v-flex> 
        <v-flex xs4>
        </v-flex>  
        <v-flex xs4>
            <v-img :src="getImgUrl('control_right.png')" contain style="height:100px;widht:100px"></v-img>
        </v-flex>    
    </v-layout> -->

    
</v-container>
</template>

<script>
import $ from 'jquery'

export default {
    name:'Intro',
    data(){
        return{
            launch:'false',
            bgImage:'../assets/samle.png'
        }
    },
    mounted(){
        const curSelf = this
        // $('.application--wrap').css('background-image',self.getImgUrl('sample.png'))
        $("input[type=range]").on("change", function(e) {
            var value = $('').val();
        if(value > 0) {
            transValue = 1 - ((value * 2) / 100);
            transValue = transValue <= 0 ? 0 : transValue;
            $("label", $("label").parent()).css({
                opacity: transValue
            });
        }
        }).on("mouseup", function(e) {
        const self = this;
        var value = $(this).val();

        if(value != 100) {
            for(var i = value; i >= 0; i--) {
            (function changeValue(value) {
                setTimeout(function () { 
                $(self).val(value);
                }, (100 - value) * 3);
            })(i);
            }
            $("label", $(self).parent()).animate({
            opacity:1
            }, 500, "linear");
        }else{
            curSelf.goHome();
        }
        });
    },
    methods:{
        getImgUrl(img){
            return require('../assets/'+img)
        },
        goHome(){
            console.log("goHome")
            this.$emit('goHome','') 
        }
    }
}
</script>
<style scoped>
#introPage{
    background: url('../assets/sample2.png') center !important;
}
 .container {
    width: 780px;
    margin: 0 auto;
}
.slide-wrap {
  width: 650px;
  position:relative;
}
.center {
  margin: 0 auto;
}
@-webkit-keyframes slidetounlock {
  0% {
  	background-position: -400px 0;
	}
	100%{
		background-position: 200px 0;
	}
}
label {
  width: 650px;
  background: -webkit-gradient(linear,left top,right top,color-stop(0, #4d4d4d),color-stop(0.4, #4d4d4d),color-stop(0.5, white),color-stop(0.6, #4d4d4d),color-stop(1, #4d4d4d)); 
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  -webkit-animation: slidetounlock 5s infinite;
  color: #4d4d4d;
  font-size: 60px;
  font-family: "HelveticaNeue-Light";
  line-height: 100px;
  height: 100px;
  position: absolute;
	left: 200px;
}
input[type=range] {
  -webkit-appearance: none !important;
  -webkit-border-radius: 30px;
  border-radius: 23px;
  background: -moz-linear-gradient(top, #010101, #181818);
  background: -webkit-gradient(linear,left top,left bottom,color-stop(0, #010101),color-stop(1, #181818));
  border: 2px solid #454545;
  overflow: hidden;
  -webkit-user-select: none;
  width: 650px;
  height: 100px;
}
input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none !important;
    background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJIAAABiCAYAAAC76YqXAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyJpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMC1jMDYwIDYxLjEzNDc3NywgMjAxMC8wMi8xMi0xNzozMjowMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNSBNYWNpbnRvc2giIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MTc2MEJCMzY5RTdCMTFERjk2MTRDN0NEQzZBQkQzODkiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MTc2MEJCMzc5RTdCMTFERjk2MTRDN0NEQzZBQkQzODkiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDpGRDI4QTM2QjlFNzcxMURGOTYxNEM3Q0RDNkFCRDM4OSIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDpGRDI4QTM2QzlFNzcxMURGOTYxNEM3Q0RDNkFCRDM4OSIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PhpMjk0AAAmgSURBVHja7F17TFNX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');
  background-position: 0 2px;
  width: 146px;
  height: 98px;
  line-height: 1;
  display: inline-block;
}
</style>