<template>
  <div>
    <!-- 홈 화면(sector1) -->
    <ImgBanner call="home">
      <div
        style="line-height:1.1em; font-weight:bold;text-align:center"
        slot="text"
        class="layout align-center justify-center row fill-height"
      >
        <br />Start!
        <br />with StartDroneTeam
      </div>
    </ImgBanner>

    <!-- 간단소개 (sector2) -->
    <div style="text-align:center">
      <h1 id="hello">Hello.</h1>
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
      <div class="more">
        <a href="/about" class="more_link">
          <span class="more_link_text">'출발 드론팀'에 대해 더 궁금하신가요?</span>
        </a>
        <v-btn class="button" fab to="/about" > <i class="fas fa-users"></i> </v-btn>
      </div>

      <h1 id="service">SERVICE.</h1>
    </div>

    <!-- 서비스 단계 표시(sector3) -->
    <v-container fluid grid-list-md>
      <h1 class="service_title">1. Service Steps Using Drones</h1>
      <v-layout row justify-center>
        <v-flex v-for="(step,index) in steps" :key="index" xs4>
          <v-card class="hidden-sm-and-down; ma-4">
            <v-img pd-4 :src="step.src" aspect-ratio="1.7" contain></v-img>
            <v-card-title primary-title style="text-align:center">
              <div style="width:100%">
                <h3 class="headline mb-0">{{ step.card_title }}</h3>
                <div>{{ step.card_text }}</div>
              </div>
            </v-card-title>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>

    <!-- 주요 서비스 소개(sector4) -->
    <v-container fluid grid-list-md>
      <h1 class="service_title">2. Platform Main Function</h1>
      <v-tabs color="black" dark slider-color="white" centered>
        <v-tab v-for="(service,index) in services" :key="index" ripple>{{service.card_title}}</v-tab>
        <v-tab-item v-for="(service,index) in services" :key="index">
          <v-layout row wrap mt-4>
            <v-flex xs6>
              <v-card style="text-align:center;">
                
                <v-card-text>
                  <h1>{{service.card_title}}</h1><br/>
                  {{ service.card_text }}</v-card-text>
                <v-divider></v-divider>
                <v-card-text> 기능 더 알아보기 
                    <v-btn icon to="/service" id="goService">
                      <i class="fas fa-arrow-right"></i>
                    </v-btn>
                </v-card-text>
              </v-card>
            </v-flex>

            <v-flex xs6>
              <v-card>
                <v-img :src="service.src" aspect-ratio="1.7" contain></v-img>
              </v-card>
            </v-flex>
          </v-layout>
        </v-tab-item>
      </v-tabs>
    </v-container>
  </div>
</template>

<script>
import ImgBanner from "../components/ImgBanner";
import $ from "jquery";

export default {
  name: "Home",
  components: {
    ImgBanner
  },
  mounted() {
    window.onpopstate = event => {
      if (this.$route.path == "/") {
        this.$router.push("/home");
      }
    };
    $("#hello").mousemove(function(e) {
      var rXP = e.pageX - this.offsetLeft - $(this).width() / 2;
      var rYP = e.pageY - this.offsetTop - $(this).height() / 2;
      $("#hello").css(
        "text-shadow",
        +rYP / 10 +
          "px " +
          rXP / 80 +
          "px rgba(227,6,19,.8), " +
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

    $("#service").mousemove(function(e) {
      var rXP = e.pageX - this.offsetLeft - $(this).width() / 2;
      var rYP = e.pageY - this.offsetTop - $(this).height() / 2;
      $("#service").css(
        "text-shadow",
        +rYP / 10 +
          "px " +
          rXP / 80 +
          "px rgba(227,6,19,.8), " +
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

  methods: {
    getImgUrl(img) {
      return require("../assets/" + img);
    }
  },

  data() {
    return {
      steps: [
        {
          src: this.getImgUrl("launch.png"),
          card_title: "STEP 01 LAUNCH",
          card_text: "사람, 동물 등의 목표물을 입력하면 3대의 드론이 입력된 목표물을 찾기위해 이륙합니다."
        },
        {
          src: this.getImgUrl("detect.png"),
          card_title: "STEP 02 DETECT",
          card_text: "Spin Square 알고리즘을 기반으로 지정된 영역을 수색하기 시작합니다."
        },
        {
          src: this.getImgUrl("stop.png"),
          card_title: "STEP 03 TRACE",
          card_text: "목표물을 발견하면 각 드론들이 전체 수색 / 근방 수색 / 타겟 추적으로 전환되어 임무를 수행합니다."
        }
      ],
      services: [
        {
          src: this.getImgUrl("monitoring.gif"),
          card_title: "수색 현장 모니터링",
          card_text:
            "수색하고 있는 드론의 화면을 웹상에서 간편하게 볼 수 있습니다."
        },
        {
          src: this.getImgUrl("mappin.gif"),
          card_title: "타겟 위치 변화 시각화",
          card_text: "지정한 타겟이 이동하는 위치를 쉽게 파악할 수 있습니다."
        }
      ]
    };
  }
};
</script>

<style scoped>
@font-face {
  font-family: "LotteMartDream";
  src: url("//cdn.jsdelivr.net/korean-webfonts/1/corps/lottemart/LotteMartDream/LotteMartDreamMedium.woff2")
      format("woff2")
}

.container {
  width: 100%;
}

#hello,#service {
  text-transform: uppercase;
  font-size: 72px;
  font-family: "Verdana";
  padding: 30px;
}

.hello_text {
  margin: 2.5em 0 1em;
  padding: 0 3.5em;
  font-family: "LotteMartDream", sans-serif;
  color: #3f3f3f;
  font-size: 1.5em
}

#title_sm {
  display: block;
  font-size: 11px;
  letter-spacing: 1px;
  color: #aaa;
  text-transform: uppercase;
}

.more {
  position: relative;
  margin-top: 5em;
  margin-bottom:6em;
}

.more:before {
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

.more_link {
  top:20px;
  position: relative;
  letter-spacing: 0.12rem;
  color: #656565;
}

.more_link_text {
  position: relative;
  padding: 0 20px;
  border-radius:0;
  background-color:antiquewhite;
}

.button {
  margin-top:25px;
  font-size: 22px;
  background: #4FD1C5;
  background: linear-gradient(90deg, rgba(129,230,217,1) 0%, rgba(79,209,197,1) 100%);
  }

.button:hover {
  color: #313133;
  transform: translateY(-5px);
}

.button::after {
  content: '';
  width: 30px; height: 30px;
  border-radius: 100%;
  border: 6px solid #00FFCB;
  position: absolute;
  z-index: -1;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  animation: ring 1.5s infinite;
}

.service_title{
  text-align:center;
  font-family: "LotteMartDream", sans-serif;
}

#goService {
  margin-left:10px;
  margin-bottom:10px;
}

#goService:hover{
  margin-left:10px;
  margin-bottom:10px;
  left:10%;
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

</style>