<template>
  <div class="sector" id="aboutBox">

    <div id="vertical_line"></div>
    <svg id="svg" viewBox="0 0 24 24">
      <path id="lightbulb" fill="#000000" d="M12,2A7,7 0 0,1 19,9C19,11.38 17.81,13.47 16,14.74V17A1,1 0 0,1 15,18H9A1,1 0 0,1 8,17V14.74C6.19,13.47 5,11.38 5,9A7,7 0 0,1 12,2M9,21V20H15V21A1,1 0 0,1 14,22H10A1,1 0 0,1 9,21M12,4A5,5 0 0,0 7,9C7,11.05 8.23,12.81 10,13.58V16H14V13.58C15.77,12.81 17,11.05 17,9A5,5 0 0,0 12,4Z" />
    </svg>

    <p id="about_Title">Hello</p>
    <p id="title_sm">This is Start Drone Team</p>

    <div id="hello_text">
      <p>
        안녕하세요, '
        <span>출발 드론팀</span>' 입니다.&nbsp;
        <br />저희 <b>FinDrone</b> 사이트에 방문해 주셔서 감사합니다.
        <br />FinDrone은
        <b>Find</b>와
        <b>Drone</b>의 합성어로 '드론으로 찾는다'라는 의미를 갖고 있습니다.
        <br />저희는 섬세하고 꼼꼼하게 실종자를 수색하기 위한 뛰어난 수색 알고리즘을 갖추고 있습니다.
        <br />골든타임의 중요성을 인지하고 있으며, 보다 많은 실종자를 찾을 수 있도록 오늘도 궁리 중입니다.
      </p>
      <p>
        작은 단서도 놓치지 않도록 '황하남 알고리즘 전문가'가 전문성을 담아 개발하고 있습니다.
        <br />저희 팀의 도움이 필요하시다면 언제든 연락 주세요 :)
      </p>
    </div>

    <div id="more">
      <span id="more_link_text"><mark>'출발 드론팀'에 대해 더 궁금하신가요?</mark></span>

      <!-- 팀소개 다이얼로그 -->
      <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
        <template v-slot:activator="{ on }">
          <v-btn class="button" fab v-on="on"> <i class="fas fa-users"></i> </v-btn>
        </template>

        <v-img :src="getImgUrl('Team.jpg')" style="height:100vh;">
          <!-- 메인 카드 영역 -->
          <v-card>
            <v-toolbar style="background:transparent; box-shadow:none; position:fixed;">
              <v-btn icon @click="dialog = false">
                <i class="fas fa-times"></i>
              </v-btn>
              <v-toolbar-title style="font-weight:bold;">Introduce Our Team</v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>
          </v-card>

          <!-- 인물별 hover 카드 -->
          <!-- 하남 -->
          <div v-for="elem in members" :key="elem.position">
            <div class="teamMember" :id="elem.target">
              <div class="corner top left"></div>
              <div class="corner top right"></div>
              <div class="corner bottom left"></div>
              <div class="corner bottom right"></div>
            </div>
            <v-card class="memberInfo" :id="elem.info">
              <v-layout>
                <!-- 프로필 사진 -->
                <v-flex xs5>
                  <v-img :src="elem.src" class="memberImage"></v-img>
                </v-flex>

                <!-- 정보 -->
                <v-flex xs7>
                  <v-container>
                    <h1>{{elem.name}}</h1>
                    <h4>{{elem.discription}}</h4><br/>

                    <p>{{elem.position}}</p> <br/>
                    <span>
                      더 알아보기
                    </span>
                      <i class="fas fa-arrow-right moreInfo"></i>
                      <v-btn style="padding-right:150px" icon :link="elem.src"> <v-icon>fab fa-github</v-icon> </v-btn>
                  </v-container>
                </v-flex>
              </v-layout>
            </v-card>
          </div>
        </v-img>
    </v-dialog>
    </div>

  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: "About",
  data(){
    return{
      dialog:false,
      members:[
        {
          position:'CTO',
          name:'King HaNam',
          discription:'모든걸 마스터한 남자',
          github:'https://github.com/diterun',
          src:'https://avatars0.githubusercontent.com/u/27193194?s=460&v=4',
          target: 'HanamTarget',
          info: 'HanamInfo'
        },
        {
          position:'Unreal',
          name:'Kang Hyun',
          discription:'모든 것을 창조하는 조물주',
          github:'https://github.com/mmhyun90',
          src:'https://avatars1.githubusercontent.com/u/18240086?s=460&v=4',
          target: 'HyunTarget',
          info: 'HyunInfo'
        },
        {
          position:'AI',
          name:'Lee GiIn',
          discription:'AI를 뛰어넘는 Human Intelligence',
          github:'https://github.com/marco0332',
          src:'https://avatars2.githubusercontent.com/u/27988544?s=460&v=4',
          target: 'GinTarget',
          info: 'GinInfo'
        },
        {
          position:'FrontEnd',
          name:'Jeong HaeIn',
          discription:'웹마스터',
          github:'https://github.com/jhi93',
          src:'https://avatars1.githubusercontent.com/u/31469550?s=400&v=4',
          target: 'HaeinTarget',
          info: 'HaeinInfo'
        },
        {
          position:'BackEnd',
          name:'Park HyunBin',
          discription:'모든걸 정점찍은 남자',
          github:'https://github.com/sksms17456',
          src:'https://avatars0.githubusercontent.com/u/19828721?s=460&v=4',
          target: 'BinTarget',
          info: 'BinInfo'
        }
      ]
    }
  },
  methods:{
    getImgUrl(img){
      return require('../assets/'+img)
    }
  }
}
</script>

<style scoped>
#svg {
  width: 50px;
  height: 50px;
  transform: rotate(180deg);
}

#lightbulb {
  transition: fill 2s ease;
}

#lightbulb.on {
  fill: #ffc83b;
}

#about_Title {
  text-transform: uppercase;
  font-size: 72px;
  font-family: "Verdana";
  padding: 30px 30px 0px 30px;
  transition: text-shadow 3s ease, color 2s ease;
}

#about_Title.on {
  color: #ffc83b;
  text-shadow: rgba(227, 6, 19, 0.8) 3.3px 5.985px, rgb(255, 237, 0) 4.125px 7.98px;
}

#title_sm {
  display: block;
  font-size: 11px;
  letter-spacing: 1px;
  color: #aaa;
  text-transform: uppercase;
}

#vertical_line {
  position: relative;
  left: 49.9%;
  content: '';
  width: 3px;
  height: 3.5em;
  background-color: black;
  transition: background-color 2s ease;
}

#vertical_line.on {
  background-color: #ffc83b99!important;
}

#hello_text {
  position: relative;
  margin: 2.5em 0 1em;
  padding: 0 3.5em;
  font-family: "LotteMartDream", sans-serif;
  color: #3f3f3f;
  font-size: 1.5em;
  transition: color 3s ease;
}

#hello_text.on {
  animation: fade_in 3.2s;
  /* animation: fade_in 2s cubic-bezier(0.075, 0.62, 0.305, 1); */
}

#more {
  position: relative;
  margin-top: 5em;
  margin-bottom:6em;
}

#more:before {
  display: block;
  position: absolute;
  top: -20px;
  left: 50%;
  width: 10em;
  height: 1px;
  transform: translateX(-50%);
  background-color: #888;
  content: "";
}

#more_link_text {
  position: relative;
  top:20px;
  padding: 0 20px;
  border-radius:0;
  letter-spacing: 0.12rem;
  text-decoration: underline;
}

mark {
  display: inline-block;
  line-height: 0em;
  background-color: #ffc83b99;
  padding-bottom: 0.5em;
  font-family: "LotteMartDream", sans-serif;
  font-size: 14px;
  color:#464653;
}

.button {
  margin-top:25px;
  font-size: 22px;
  background: rgba(0, 159, 227, 0.7);
  background: linear-gradient(140deg, #ffc83b99 40%,  rgba(227, 6, 19, 0.7) 100%);
  }

.button:hover {
  transform: translateY(-5px);
}

.v-btn::before {
  opacity: 0!important;
}

.button::after {
  content: '';
  width: 30px; height: 30px;
  border-radius: 100%;
  border: 6px solid rgba(227, 6, 19, 0.3);
  position: absolute;
  z-index: -1;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  animation: ring 1.5s infinite;
}

#goMoreInfo{
  margin-left:120px;
  animation: bounceArrow 0.9s infinite ease-out;
}

.teamMember {
  position: fixed;
  display: block;
  background-color: transparent;
  box-shadow: none;
  height: 90px;
  width: 90px;
}

.teamMember > div.corner {
  display: block;
  position: absolute;
  width: 25px;
  height: 25px;
  border-color: #ffc83b;
}

.teamMember:hover > div.corner {
  animation: targeting 1.5s infinite;
}

.top {
    top: 0px;
    border-top-style: solid;
    border-top-width: 6px;
}

.bottom {
    bottom: 0px;
    border-bottom-style: solid;
    border-bottom-width: 6px;
}

.left {
    left: 0px;
    border-left-style: solid;
    border-left-width: 6px;
}

.right {
    right: 0px;
    border-right-style: solid;
    border-right-width: 6px;
}

.memberInfo {
  height: 300px;
  width: 500px;
  z-index: 15;
  display: none;
}

.memberImage {
  height: 300px;
}

.teamMember:hover ~ .memberInfo {
  background-color: #ffc83b;
  position: absolute;
}

#HanamTarget {
  left: 15.3vw;
  top: 29vh;
}

#HanamTarget:hover ~ #HanamInfo{
  display: block;
  top: 45vh;
  left: 8vw;
}

#HyunTarget {
  left: 80vw;
  top: 28vh;
}

#HyunTarget:hover ~ #HyunInfo{
  display: block;
  top: 45vh;
  left: 60vw;
}

#BinTarget {
  left: 49.2vw;
  top: 38vh;
}

#BinTarget:hover ~ #BinInfo{
  display: block;
  top: 55vh;
  left: 36vw;
}

#HaeinTarget {
  left: 30.5vw;
  top: 29.5vh;
}

#HaeinTarget:hover ~ #HaeinInfo{
  display: block;
  top: 5vh;
  left: 40vw;
}

#GinTarget {
  left: 63.2vw;
  top: 32vh;
}

#GinTarget:hover ~ #GinInfo{
  display: block;
  top: 4vh;
  left: 25vw;
}

.moreInfo{
  margin-left:90px;
  margin-top:20px;
  animation: bounceArrow 0.9s infinite ease-out;
}

@keyframes bounceArrow {
    0%,
    20%,
    100% {
        transform: translateX(-60px);
    }
    30% {
        transform: translateX(-65px);
    }
    50% {
        transform: translateX(-60px);
    }
}

@keyframes fade_in {
  0% { bottom: -50px; opacity: 0 }
  50% { bottom: -50px; opacity: 0 }
  100% {bottom: 0px; opacity: 1 }
}

@keyframes ring {
  0% {
    width: 60px;
    height: 60px;
    opacity: 1;
  }
  100% {
    width: 100px;
    height: 100px;
    opacity: 0;
  }
}

@keyframes targeting {
  0% {
    width: 30px;
    height: 30px;
  }
  50% {
    width: 38px;
    height: 38px;
    border-color: #fc9a41;
    border-width: 8px;
  }
  100% {
    width: 30px;
    height: 30px;
  }
}
</style>