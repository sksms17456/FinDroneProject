<template>
  <v-footer
    dark
    height="auto"
    id="footer"
  >
    <v-card
      flat
      tile
      class="text-xs-center"
      style="width:100%; background-color:#002148;"
    >
      <v-card-text class="white--text">
        <v-btn
          v-for="icon in icons"
          :href="icon.link"
          :key="icon.icon"
          class="mx-3 white--text"
          icon
        >
          <v-icon size="24px">{{ icon.icon }}</v-icon>
        </v-btn>

        <p>
          &copy;2019 — <strong>출발 드론팀</strong>
        </p>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
  export default {
    data: () => ({
      icons: [
        {icon: 'fab fa-github', link: 'https://www.youtube.com/channel/UC-J0CCwYpjfoBxmvcuBGz_w'},
        {icon: 'fab fa-youtube', link: 'https://www.youtube.com/channel/UC-J0CCwYpjfoBxmvcuBGz_w'}
      ]
    }),
    mounted(){
      this.init();
    },
    methods:{
        getImgUrl(img){
            return require('../assets/'+img)
        },
        init(){
          if(this.$route.path==='/central' || this.$route.path==='/rootmap'){
            var footerElement = document.getElementById("footer");
            footerElement.style.display = "none";
          }
        }
    },
  }
</script>