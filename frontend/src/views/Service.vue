<template>
    <div>
        <ImgBanner call="service" height="100vh" id="banner">
            <div style="line-height:1.1em; font-weight:bold;text-align:center" slot="text" class="layout align-center justify-center row fill-height">
                <br/> WATCH THE DRONES
                <br/> FIND YOUR TARGET
            </div>
        </ImgBanner>
        
        <h1 id="serviceMainTitle">Our Services</h1>

        <v-container fluid grid-list-xs>
            <v-layout row wrap id="section1">
                <v-flex xs7>
                    <v-img :src="getImgUrl('baekdu.jpg')"> </v-img>
                </v-flex>
                <v-flex xs5>
                <h1 class="serviceTitle">시스템 구성도</h1>
                <span  class="fadeinleft">
                    Client : Unreal Engine<br/>
                    Server : Python Flask<br/>
                    AI : CNN기반의 ~~ 모델<br/>
                    WEB : Vue.js                        
                </span>
                    </v-flex>
            </v-layout>

            <v-layout row wrap id="section2">
                <v-flex xs5>
                    <h1 class="serviceTitle">수색 알고리즘</h1>
                    <span>
                        3대의 드론이 수색을 시작하게 되는데...<br/>
                        다음 이시간에 계속!
                    </span>
                </v-flex>
                <v-flex xs7>
                    <v-img :src="getImgUrl('baekdu.jpg')"> </v-img>
                </v-flex>
            </v-layout>

            <v-layout row wrap id="section3">
                <v-flex xs7>
                    <v-img :src="getImgUrl('baekdu.jpg')"> </v-img>
                </v-flex>
                <v-flex xs5>
                    <h1 class="serviceTitle">주요 서비스</h1>
                    <span>
                        수색현장 모니터링<br/>
                        타겟 위치 변화 시각화                      
                    </span>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
import ImgBanner from '../components/ImgBanner'
import $ from 'jquery'

export default {
    name:'Service',
    components:{
        ImgBanner
    },
    data(){
        return{
            bottom_of_section1:-20,
            bottom_of_section2:-20,
            bottom_of_section3:-20
        }
    },
    mounted(){
        window.addEventListener('scroll', this.handleScroll);
        this.bottom_of_section1 = $('#section1').offset().top + $('#section1').outerHeight();
        this.bottom_of_section2 = $('#section2').offset().top + $('#section2').outerHeight();
        this.bottom_of_section3 = $('#section3').offset().top + $('#section3').outerHeight();
    },
    methods:{
        getImgUrl(img){
            return require('../assets/'+img)
        },
        handleScroll (event) {
            var bottom_of_window = $(window).scrollTop() + $(window).height();
            
            if( bottom_of_window > this.bottom_of_section3-250 ){
                $('#section3').animate({'opacity':'1','margin-left':'0px'},500);
            }else if( bottom_of_window > this.bottom_of_section2-250 ){
                $('#section2').animate({'opacity':'1','margin-left':'0px'},500);
            }else if( bottom_of_window > this.bottom_of_section1-250 ){
                $('#section1').animate({'opacity':'1','margin-left':'0px'},500);
            }
        }
    }
}
</script>

<style scoped>
.container{
    width: 90%;
}
.layout.row.wrap{
    height:100vh;
}
#section1{
    opacity:0;
    margin-left:300px;    
    max-width:100%;
}
#section2{
    opacity:0;
    margin-left:-300px;    
    max-width:100%;
}
#section3{
    opacity:0;
    margin-left:300px;    
    max-width:100%;
}

#serviceMainTitle{
    text-align:center;
    font-size:72px;
    margin-top:35px;
    /* animation: fadeIn ease 5s; */
}
.serviceTitle{
    font-size: 60px;
    text-align:center;
}

@keyframes fadeIn {
    from {
        opacity:0;
    }
    to {
        opacity:1;
    }
}

@keyframes fadeInRight {
    from {
        opacity: 0;
        transform: translateX(-20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes fadeInLeft {
    from {
        opacity: 0;
        transform: translateX(20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

</style>