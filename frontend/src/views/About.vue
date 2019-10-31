<template>
    <div class="sector">
      <p id="about_Title">Hello.</p>
      <p id="title_sm">This is Start Drone Team.</p>

      <div class="hello_text">
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

        <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
          <template v-slot:activator="{ on }">
            <v-btn class="button" fab v-on="on"> <i class="fas fa-users"></i> </v-btn>
          </template>

          <v-card>
            <v-toolbar dark color="rgba(0, 159, 227, 0.7)">
              <v-btn icon dark @click="dialog = false">
                <i class="fas fa-times"></i>
              </v-btn>
              <v-toolbar-title>Introduce Our Team</v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>

            <v-tabs color="rgba(0, 159, 227, 0.7)" dark slider-color="yellow" centered>
              <v-tab v-for="(member,index) in members" :key="index" ripple>{{member.position}}</v-tab>
              
              <v-tab-item v-for="(member,index) in members" :key="index">
                <v-layout row wrap mt-4>
                  <v-flex xs6>
                    <v-card style="text-align:center;">
                      <v-card-text>
                        <h1>{{member.name}}</h1><br/>
                        {{ member.discription }}</v-card-text>
                      <v-divider></v-divider>
                      <v-card-text>
                        <span>더 알아보기</span>
                        <i id="goMoreInfo" class="fas fa-arrow-right"></i>
                         <v-btn icon :href="member.github">
                              <i class='fab fa-github'></i>
                         </v-btn>
                      </v-card-text>
                    </v-card>
                  </v-flex>

                  <v-flex xs6>
                    <v-card>
                      <v-img :src="member.src" aspect-ratio="1.7" contain></v-img>
                    </v-card>
                  </v-flex>
                </v-layout>
              </v-tab-item>
            </v-tabs>
          </v-card>
      </v-dialog>
      </div>

    </div>
</template>

<script>
import $ from 'jquery'

export default {
  name:'About',
  data(){
    return{
      dialog:false,
      members:[
        {
          position:'CTO',
          name:'King HaNam',
          discription:'모든걸 마스터한 남자',
          github:'https://github.com/diterun',
          src:'https://avatars0.githubusercontent.com/u/27193194?s=460&v=4'
        },
        {
          position:'Unreal',
          name:'Kang Hyun',
          discription:'모든걸 마스터한 남자',
          github:'https://github.com/mmhyun90',
          src:'https://avatars1.githubusercontent.com/u/18240086?s=460&v=4'
        },
        {
          position:'AI',
          name:'Lee GiIn',
          discription:'AI를 뛰어넘는 Human Intelligence',
          github:'https://github.com/marco0332',
          src:'https://avatars2.githubusercontent.com/u/27988544?s=460&v=4'
        },
        {
          position:'FrontEnd',
          name:'Jeong HaeIn',
          discription:'버스승객',
          github:'https://github.com/jhi93',
          src:'https://avatars0.githubusercontent.com/u/31469550?s=460&v=4'
        },
        {
          position:'BackEnd',
          name:'Park HyunBin',
          discription:'모든걸 정점찍은 남자',
          github:'https://github.com/sksms17456',
          src:'https://avatars0.githubusercontent.com/u/19828721?s=460&v=4'
        }
      ]
    }
  },
  mounted(){
    $("#about_Title").mousemove(function(e) {
      var rXP = e.pageX - this.offsetLeft - $(this).width() / 2;
      var rYP = e.pageY - this.offsetTop - $(this).height() / 2;
      $("#about_Title").css(
        "text-shadow",
        +rYP / 10 +
          "px " +
          rXP / 80 +
          "px rgba(227,6,19,.8), " 
          +
          rYP / 8 +
          "px " +
          rXP / 60 +
          "px rgba(255,237,0,1), " +
          rXP / 70 +
          "px " +
          rYP / 12 +
          "px rgba(0,159,227,.7)"
      );
    });
  },
  methods:{
    getImgUrl(img){
      return require('../assets/'+img)
    }
  }
}
</script>

<style scoped>

#about_Title {
  text-transform: uppercase;
  font-size: 72px;
  font-family: "Verdana";
  padding: 30px;
}

#title_sm {
  display: block;
  font-size: 11px;
  letter-spacing: 1px;
  color: #aaa;
  text-transform: uppercase;
}

.hello_text {
  margin: 2.5em 0 1em;
  padding: 0 3.5em;
  font-family: "LotteMartDream", sans-serif;
  color: #3f3f3f;
  font-size: 1.5em
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
  /* background-color:antiquewhite; */
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
  background: linear-gradient(90deg, rgba(15, 164, 228, 0.7) 0%,  rgba(0, 159, 227, 0.7) 100%);
  }

.button:hover {
  color: #313133;
  transform: translateY(-5px);
}

.button::after {
  content: '';
  width: 30px; height: 30px;
  border-radius: 100%;
  border: 6px solid rgb(6, 199, 233);
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

@keyframes ring {
  0% {
    width: 30px;
    height: 30px;
    opacity: 1;
  }
  100% {
    width: 100px;
    height: 100px;
    opacity: 0;
  }
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
</style>