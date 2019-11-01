<template>
    <div class="sector" id="systemBox">
      <div id="systemTitle"> <p id="systemMTitle">SYSTEM</p> <p><span id="systemSTitle">/ 구성도</span></p></div>
      <v-container id="systemContainer">
        <v-img :src="getImgUrl('System.png')"></v-img>
        <h3>1. Unreal Engine : 실제 상황을 가정한 가상 현실로 실종자를 찾는 드론 시뮬레이션 환경</h3>
        <h3>2. Controller : 드론의 Mobile AP에 해당하며 수색알고리즘과 AI 이미치 처리기술 탑재 </h3>
        <h3>3. Server : 드론들의 정보를 수집하여 모든 드론에게 정보를 BroadCast 및 사용자에게 드론 정보 시각화</h3>
      </v-container>
    </div>
</template>

<script>
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

#systemContainer {
  width: 900px!important;
  padding:0;
}

#systemTitle{
  text-align: center;
  color:#555;
  font-family: 'Baloo Paaji', cursive;
  font-size: 60px;
  overflow: hidden;
  height:90px;
}

p {
  display:inline-block;
  overflow:hidden;
  white-space:nowrap;
  margin-bottom: 0px;
}

p:first-of-type {
  animation: showup 7s;
}

p:last-of-type {
  width:0px;
  animation: reveal 7s;
}

p:last-of-type span {
  margin-left:-200px;
  animation: slidein 7s;
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
</style>