<template>
    <div class="sector">
      <p class="mainTitle">Hello.</p>
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

      
    </div>
</template>

<style scoped>
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