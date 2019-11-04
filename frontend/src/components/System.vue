<template>
    <div class="sector" id="systemBox">
      <div id="systemTitle"> 
        <p id="sysTitle0">SYSTEM</p>
        <p id="sysTitle1"><span id="sysTitle2">/ 구성도</span></p>
      </div>
      <v-container id="systemContainer">
        <v-layout>
          <v-flex xs7 id="structure">
            <v-img :src="getImgUrl('System.png')"></v-img>
          </v-flex>
          <v-flex xs5 id="describe" style="text-align:left;">
            <h1 class="desTitle">1. Unreal Engine</h1><span class="desContent"> -> 실제 상황을 가정한 가상 현실로 실종자를 찾는 드론 시뮬레이션 환경</span><br/><br/>
            <h1 class="desTitle">2. Controller</h1><span class="desContent">-> 드론의 Mobile AP에 해당하며 수색알고리즘과 AI 이미치 처리기술 탑재</span><br/><br/>
            <h1 class="desTitle">3. Server</h1><span class="desContent">-> 드론들의 정보를 수집하여 모든 드론에게 정보를 BroadCast 및 사용자에게 드론 정보 시각화</span><br/><br/>
          </v-flex>
        </v-layout>
      </v-container>
    </div>
</template>

<script>
import $ from 'jquery'

export default {
    methods: {
        getImgUrl(img) {
            return require("../assets/" + img);
        }
    }
}
</script>

<style scoped>
@import 'https://fonts.googleapis.com/css?family=Baloo+Paaji';

#systemBox{
  padding-top:80px;
}

#systemTitle{
  text-align: center;
  font-family: 'Baloo Paaji', cursive;
  font-size: 60px;
  overflow: hidden;
  height:90px;
  margin-bottom:60px;
}
.systemSTitle {
  animation: showup 7s;
}

.systemSTitle1 {
  width:0px;
  animation: reveal 7s;
}

.systemSTitle2 {
  margin-left:-200px;
  animation: slidein 7s;
}

p {
  display:inline-block;
  overflow:hidden;
  white-space:nowrap;
  margin-bottom: 0px;
}

#systemContainer {
  max-width: 1400px;
  width: 1400px;
  height: 570px;
  padding:0;
}

#structure{
  opacity:0;
  margin-left:-300px;
  max-width:100%;
}

#describe{
  margin-top:30px;
  font-family: "LotteMartDream";
  color:#555;
}

.desTitle{
  font-size:3.0em;
  margin-bottom: 20px;
}

.desContent{
  font-size:1.4em;
}


@keyframes showup {
    0% {opacity:0;}
    20% {opacity:1;}
    80% {opacity:1;}
    100% {opacity:0;}
}

@keyframes slidein {
    0% { margin-left:-10px; }
    20% { margin-left:-10px; }
    35% { margin-left:0px; }
    100% { margin-left:0px; }
}

@keyframes reveal {
    0% {opacity:0;width:0px;}
    20% {opacity:1;width:0px;}
    30% {width:200px;}
    80% {opacity:1;}
    100% {opacity:0;width:200x;}
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