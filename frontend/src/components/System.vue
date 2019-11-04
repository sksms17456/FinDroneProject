<template>
    <div class="sector" id="systemBox">

      <div id="vertical_line_system"></div>
      <svg id="svg" viewBox="0 0 24 24">
        <path id="computer" fill="#000000" d="M6,2C4.89,2 4,2.89 4,4V12C4,13.11 4.89,14 6,14H18C19.11,14 20,13.11 20,12V4C20,2.89 19.11,2 18,2H6M6,4H18V12H6V4M4,15C2.89,15 2,15.89 2,17V20C2,21.11 2.89,22 4,22H20C21.11,22 22,21.11 22,20V17C22,15.89 21.11,15 20,15H4M8,17H20V20H8V17M9,17.75V19.25H13V17.75H9M15,17.75V19.25H19V17.75H15Z" />
      </svg>
      <img id="computerBackground" src="../assets/computer.jpg" alt="computer" />

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

#svg {
  width: 50px;
  height: 50px;
}

#vertical_line_system {
  position: relative;
  left: 49.9%;
  content: '';
  width: 3px;
  height: 3.5em;
  background-color: #d5ad5899;
  transition: background-color 3s ease;
}

#vertical_line_system.on {
  background-color: #11436a!important;
}

#computerBackground {
  position: absolute;
  left: 49.05%;
  margin-top: 6px;
  width:30px;
  opacity: 0;
  transition: opacity 4s cubic-bezier(0.785, 0.135, 0.15, 0.86);
  border-radius: 4px;
}

#computerBackground.on {
  opacity: 1;
}

#systemTitle{
  text-align: center;
  font-family: 'Baloo Paaji', cursive;
  font-size: 60px;
  overflow: hidden;
  height:90px;
  margin-bottom:60px;
  color: rgba(111, 15, 13);
  transition: text-shadow 3s ease, color 2s ease;
}

#systemTitle.on {
  color: #11436a;
  text-shadow: #d5ad5899 3.125px 3.98px;
}

.systemSTitle {
  animation: showup 10s;
}

.systemSTitle1 {
  width:0px;
  animation: reveal 5s;
}

.systemSTitle2 {
  animation: slidein 9s;
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
    0% { margin-left:5px; }
    20% { margin-left:5px; }
    35% { margin-left:0px; }
    100% { margin-left:0px; }
}

@keyframes reveal {
    0% {opacity:1;width:220px;}
    20% {opacity:1;width:220px;}
    30% {width:0px;}
    80% {opacity:0;}
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