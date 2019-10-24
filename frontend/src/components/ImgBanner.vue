<template>
    <div>
        <div v-if="call==='home'">
           <section id="bilog-bilog"></section>
            <!-- <v-carousel 
              aspect-ratio="1.7" 
              :height="height">

                <v-carousel-item
                  v-for="(item,i) in home_items"
                  :key="i"
                  :src="item.src"
                >
                      <span
                        class="text-shadow display-2 text-weight"
                        style="font-size:15vmin!important; color:white"
                      >
                          <slot name="text" />
                      </span>
                </v-carousel-item>

            </v-carousel> -->
        </div>
        <div v-else-if="call==='central'">
            <v-img :src="getImgUrl('controltower.gif')" :height="height">
                <span
                    class="text-shadow display-2 text-weight"
                    style="font-size:15vmin!important; color:white"
                    >
                    <slot name="text" />
                    </span>
            <goDownBtn />
            </v-img>
        </div>
    </div>
</template>

<script>
import goDownBtn from '../components/goDownBtn'
import $ from 'jquery'

var SEPARATION = 100, AMOUNTX = 50, AMOUNTY = 50;
var container, stats;
var camera, scene, renderer;
var particles, particle, count = 0;
var mouseX = 0, mouseY = 0;
var windowHalfX = window.innerWidth / 2;
var windowHalfY = window.innerHeight / 2;

export default {
    name:'ImgBanner',
    components: {
      goDownBtn
    },
    props: {
        call:{type:String, default:"home"},
        text: { type: String },
        height: { type: String, default: "100vh" }
    },
    methods:{
        getImgUrl(img){
            return require('../assets/'+img)
        },
        init() {
        container = document.createElement('div',{  id: "particles", class: "particles"});
        document.getElementById('bilog-bilog').appendChild( container );
        camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 1, 10000 );
        camera.position.z = 1000;
        scene = new THREE.Scene();
        particles = new Array();
        var PI2 = Math.PI * 2;
        var material = new THREE.SpriteCanvasMaterial( {
          //color: 0x3f6e86,
          color: 0x3f6e86,
          // color: 0xffffff,
          program: function ( context ) {
            context.beginPath();
            context.arc( 0, 0, .3, 0, PI2, true );
            context.fill();
          }
        } )
        var i = 0;
        for ( var ix = 0; ix < AMOUNTX; ix ++ ) {
          for ( var iy = 0; iy < AMOUNTY; iy ++ ) {
            particle = particles[ i ++ ] = new THREE.Sprite( material )
            particle.position.x = ix * SEPARATION - ( ( AMOUNTX * SEPARATION ) / 2 )
            particle.position.z = iy * SEPARATION - ( ( AMOUNTY * SEPARATION ) / 2 )
            // scene.background = new THREE.Color( 0x254a5d ); // UPDATED
            scene.add( particle )
          }
        }
        renderer = new THREE.CanvasRenderer()
        renderer.setPixelRatio( window.devicePixelRatio )
        renderer = new THREE.CanvasRenderer( { alpha: true }) // gradient
        renderer.setSize( window.innerWidth, window.innerHeight )
        container.appendChild( renderer.domElement )
        //stats = new Stats();
        //container.appendChild( stats.dom );
        // document.addEventListener( 'mousemove', this.onDocumentMouseMove, false )
        // document.addEventListener( 'touchstart', this.onDocumentTouchStart, false )
        // document.addEventListener( 'touchmove', this.onDocumentTouchMove, false )
        //
        window.addEventListener( 'resize', this.onWindowResize, false )
      },
      onWindowResize() {
        windowHalfX = window.innerWidth / 2;
        windowHalfY = window.innerHeight / 2;
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize( window.innerWidth, window.innerHeight );
      },
      onDocumentMouseMove( event ) {
        mouseX = event.clientX - windowHalfX;
        mouseY = event.clientY - windowHalfY;
      },
      onDocumentTouchStart( event ) {
        if ( event.touches.length === 1 ) {
          event.preventDefault();
          mouseX = event.touches[ 0 ].pageX - windowHalfX;
          mouseY = event.touches[ 0 ].pageY - windowHalfY;
        }
      },
      onDocumentTouchMove( event ) {
        if ( event.touches.length === 1 ) {
          event.preventDefault();
          mouseX = event.touches[ 0 ].pageX - windowHalfX;
          mouseY = event.touches[ 0 ].pageY - windowHalfY;
        }
      },
      animate() {
        requestAnimationFrame( this.animate );
        this.render();
      },
      render() {
        // camera.position.x += ( mouseX - camera.position.x ) * .05;
        // camera.position.y += ( - mouseY - camera.position.y ) * .05;
        camera.position.x = 100;
        camera.position.y = 150;
        camera.lookAt( scene.position );
        var i = 0;
        for ( var ix = 0; ix < AMOUNTX; ix ++ ) {
          for ( var iy = 0; iy < AMOUNTY; iy ++ ) {
            particle = particles[ i++ ];
            particle.position.y = ( Math.sin( ( ix + count ) * 0.3 ) * 50 ) +
              ( Math.sin( ( iy + count ) * 0.5 ) * 50 );
            particle.scale.x = particle.scale.y = ( Math.sin( ( ix + count ) * 0.3 ) + 1 ) * 4 +
              ( Math.sin( ( iy + count ) * 0.5 ) + 1 ) * 4;
          }
        }
        
        renderer.render( scene, camera );
        count += 0.1;
      }
    },
    mounted() {
      this.init()
      this.animate()
    },
    data(){
        return {
            home_items:[
                {
                    src:this.getImgUrl('valley.gif')
                },
                {
                    src:this.getImgUrl('mabig.gif')
                },
                {
                    src:this.getImgUrl('beach.gif')
                }
            ]
        }
    }
}
</script>

<style scoped>
#home_wave {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100vh;
  overflow: hidden;
  background-color: white;
}
</style>
