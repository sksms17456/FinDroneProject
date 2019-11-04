<template>
	<div>
		<div style="width:50%; float:left;">
			<div class="droneName divcolor" style="height:10%">
				<v-btn to="/home" class="button" flat>
					<img :src='getImgUrl("homeIcon.png")' class="buttonImg">
				</v-btn>
				<div style="width:500px; display:inline-block;">
					Drone-{{target.idx}}
				</div>
				<v-btn to="/rootmap" class="button" flat>
                    <img :src='getImgUrl("mapIcon.png")' class="buttonImg">
				</v-btn>				
			</div>
			<div style="height:628px">
				<img
				:src='getImgUrl("detect.png")'
				id="screen_img"
				width="100%"
				height="100%"
            	>
			</div>
			<div style="height:10%">
				<div class="dronePos divcolor">{{target.x_pos}} </div>
				<div class="dronePos divcolor">{{target.y_pos}} </div>
				<div class="dronePos divcolor">{{target.z_pos}} </div>
			</div>
			<div style="text-align:-webkit-center; padding-top:15px; background:linear-gradient(50deg, black, transparent);">
				<img :src='getImgUrl("logoText.png")'
				width="500px"
				height="124px"
				>
			</div>
		</div>

		<div class = "div_border" style="width:50%; float:left;">
			<div id="container" style="width:100%"></div>
			<div id="menu" style="width:inherit">
				<button id="table">TABLE</button>
				<button id="sphere">SPHERE</button>
				<button id="helix">HELIX</button>
				<button id="grid">GRID</button>
			</div>
    	</div>
	</div>    
</template>

<script>
import * as THREE from '../plugins/three.module.js';
import { TWEEN } from '../plugins/tween.module.min.js';
import { TrackballControls } from '../plugins/TrackballControls.js';
import { CSS3DRenderer, CSS3DObject } from '../plugins/CSS3DRenderer.js';
import axios from 'axios'
import $ from 'jquery'

export default {
    name:'Central',
    data(){
        return{
			mapImg: 'mappin.gif',
			target : {
				idx : 1,
				x_pos : 0,
				y_pos : 0,
				z_pos : 0,
			},
            table : [
				"1", "0.0", "0.0", "0.0", 1, 1,
				"2", "0.0", "0.0", "4.002602", 2, 1,
				"3", "0.0", "0.0", "6.941", 3, 1,
				"4", "0.0", "0.0", "0.0", 4, 1,
				"5", "0.0", "0.0", "0.0", 5, 1,
				"6", "0.0", "0.0", "0.0", 6, 1,
				"7", "0.0", "0.0", "0.0", 7, 1,
				"8", "0.0", "0.0", "0.0", 8, 1,
				"9", "0.0", "0.0", "0.0", 1, 2,
				"10", "0.0", "0.0", "0.0", 2, 2,
				"11", "0.0", "0.0", "0.0", 3, 2,
				"12", "0.0", "0.0", "0.0", 4, 2,
				"13", "0.0", "0.0", "0.0", 5, 2,
				"14", "0.0", "0.0", "0.0", 6, 2,
				"15", "0.0", "0.0", "0.0", 7, 2,
				"16", "0.0", "0.0", "0.0", 8, 2,
				"17", "0.0", "0.0", "0.0", 1, 3,
				"18", "0.0", "0.0", "0.0", 2, 3,
				"19", "0.0", "0.0", "0.0", 3, 3,
				"20", "0.0", "0.0", "0.0", 4, 3,
				"21", "0.0", "0.0", "0.0", 5, 3,
				"22", "0.0", "0.0", "0.0", 6, 3,
				"23", "0.0", "0.0", "0.0", 7, 3,
				"24", "0.0", "0.0", "0.0", 8, 3,
				"25", "0.0", "0.0", "0.0", 1, 4,
				"26", "0.0", "0.0", "0.0", 2, 4,
				"27", "0.0", "0.0", "0.0", 3, 4,
				"28", "0.0", "0.0", "0.0", 4, 4,
				"29", "0.0", "0.0", "0.0", 5, 4,
				"30", "0.0", "0.0", "0.0", 6, 4,				
				"31", "0.0", "0.0", "0.0", 7, 4,
				"32", "0.0", "0.0", "0.0", 8, 4,
				"33", "0.0", "0.0", "0.0", 1, 5,
				"34", "0.0", "0.0", "0.0", 2, 5,
				"35", "0.0", "0.0", "0.0", 3, 5,
				"36", "0.0", "0.0", "0.0", 4, 5,
				"37", "0.0", "0.0", "0.0", 5, 5,
				"38", "0.0", "0.0", "0.0", 6, 5,
				"39", "0.0", "0.0", "0.0", 7, 5,
				"40", "0.0", "0.0", "0.0", 8, 5,
				"41", "0.0", "0.0", "0.0", 1, 6,
				"42", "0.0", "0.0", "0.0", 2, 6,
				"43", "0.0", "0.0", "0.0", 3, 6,
				"44", "0.0", "0.0", "0.0", 4, 6,
				"45", "0.0", "0.0", "0.0", 5, 6,
				"46", "0.0", "0.0", "0.0", 6, 6,
				"47", "0.0", "0.0", "0.0", 7, 6,
				"48", "0.0", "0.0", "0.0", 8, 6,				
			],
            camera:'',
            scene:'',
            renderer:'',
			controls:'',
			objects : [],
			targets : { table: [], sphere: [], helix: [], grid: [] },
        }
	},
	created(){
		this.getImgUrlFromBack();
	},
    mounted(){
        this.init();
		this.animate();
    },
    methods:{
        getImgUrl(img){
            return require('../assets/'+img);
		},
		getImgUrlFromBack(){
			var curThis = this
			this.polling = setInterval(() => {
				const path = `/api/getInfo`
					axios.get(path)
					.then(response => {
						const contain = [response.data.iter0, response.data.iter1, response.data.iter2]
						const pos = [response.data.pos0, response.data.pos1, response.data.pos2]
						const find = [response.data.find0, response.data.find1, response.data.find2]
						for(var i=0; i<3; i++){
							curThis.table[i*6+1] = String(pos[i][0]);
							curThis.table[i*6+2] = String(pos[i][1]);
							curThis.table[i*6+3] = String(pos[i][2]);
							const path = '/api/getDroneImg?drone='+i+'&num_img'+contain[i]
							document.getElementsByClassName('details '+String(i+1))[0].innerHTML = String(pos[i][0]) + '<br>' +String(pos[i][1]) + '<br>' + String(pos[i][2]);
							document.getElementsByClassName('symbol '+String(i+1))[0].src = path;
							if(curThis.target.idx==(i+1)){
								$('#screen_img').attr("src",path);
							}
							if(find[i]){
								document.getElementsByClassName('element '+String(i+1))[0].style.backgroundColor = "darkred";
							}else {
								document.getElementsByClassName('element '+String(i+1))[0].style.backgroundColor = 'rgba(0,127,127,' + ( Math.random() * 0.5 + 0.25 ) + ')';
							}
						}
						var idx = curThis.target.idx;
						curThis.target.x_pos = pos[idx-1][0];
						curThis.target.y_pos = pos[idx-1][1];
						curThis.target.z_pos = pos[idx-1][2];
					})
					.catch(error => {
						console.log(error)
					})
			}, 500)
		},
        init() {
			this.camera = new THREE.PerspectiveCamera( 40, window.innerWidth / window.innerHeight, 1, 10000 );
			this.camera.position.z = 1800
            this.scene = new THREE.Scene();
            var self= this;
				// table
			for ( var i = 0; i < this.table.length; i += 6 ) {
				var element = document.createElement( 'div' );
				element.className = 'element ' + String(( i / 6) + 1);
				// element.style.backgroundColor = 'rgba(0,127,127,' + ( Math.random() * 0.5 + 0.25 ) + ')';
				if(i<18){
					element.style.backgroundColor = 'rgba(0,127,127,0.8)';
				}else{
					element.style.backgroundColor = 'rgba(0,127,127,0.1)';
				}

				var number = document.createElement( 'div' );
				number.className = 'number';
				number.style = 'text-align:center; width:100%; top:2px; font-size:15px; right:0px;'
				number.textContent = ( i / 6 ) + 1;
                element.appendChild( number );

				var symbol = document.createElement( 'img' );
				symbol.className = 'symbol '+ String(( i / 6 ) + 1);
				symbol.id = 'symbol ' + String(( i / 6 ) + 1);
				symbol.style = 'top:20px; height:90px;'
                symbol.src=this.getImgUrl('footerlogo.png')
                element.appendChild( symbol );
                
				var details = document.createElement( 'div' );
				details.className = 'details '+ String(( i / 6 ) + 1);
				details.id = 'details '+ String(( i / 6 ) + 1);
				details.style = 'bottom:5px;'
				details.innerHTML = this.table[ i + 1 ] + '<br>' + this.table[ i + 2 ] + '<br>' + this.table[ i + 3 ];
                element.appendChild( details );
				
				element.addEventListener('click',function() {
					document.getElementsByClassName('details 4')[0].innerHTML = '1.1' + '<br>' + '2.2' + '<br>' + '3.3'
					self.target.idx = this.getElementsByClassName('number')[0].textContent;
					self.target.x_pos = self.table[((self.target.idx-1)*6)+1];
					self.target.y_pos = self.table[((self.target.idx-1)*6)+2];
					self.target.z_pos = self.table[((self.target.idx-1)*6)+3];
				},false)

				var object = new CSS3DObject( element );
				object.position.x = Math.random() * 4000 - 2000;
				object.position.y = Math.random() * 4000 - 2000;
				object.position.z = Math.random() * 4000 - 2000;
				this.scene.add( object );
                this.objects.push( object );
                
				var object = new THREE.Object3D();
				object.position.x = ( this.table[ i + 4 ] * 140 ) - 620;
				object.position.y = - ( this.table[ i + 5 ] * 180 ) + 660;
				this.targets.table.push( object );
            }
                
				// sphere
			var vector = new THREE.Vector3();
			for ( var i = 0, l = this.objects.length; i < l; i ++ ) {
				var phi = Math.acos( - 1 + ( 2 * i ) / l );
				var theta = Math.sqrt( l * Math.PI ) * phi;
				var object = new THREE.Object3D();
				object.position.setFromSphericalCoords( 800, phi, theta );
				vector.copy( object.position ).multiplyScalar( 2 );
				object.lookAt( vector );
				this.targets.sphere.push( object );
			}
			    // helix
			var vector = new THREE.Vector3();
			for ( var i = 0, l = this.objects.length; i < l; i ++ ) {
				var theta = i * 0.175 + Math.PI;
				var y = - ( i * 8 ) + 450;
				var object = new THREE.Object3D();
				object.position.setFromCylindricalCoords( 900, theta, y );
				vector.x = object.position.x * 2;
				vector.y = object.position.y;
				vector.z = object.position.z * 2;
				object.lookAt( vector );
				this.targets.helix.push( object );
			}
				// grid
			for ( var i = 0; i < this.objects.length; i ++ ) {
				var object = new THREE.Object3D();
				object.position.x = ( ( i % 5 ) * 400 ) - 800;
				object.position.y = ( - ( Math.floor( i / 5 ) % 5 ) * 400 ) + 800;
				object.position.z = ( Math.floor( i / 25 ) ) * 1000 - 2000;
				this.targets.grid.push( object );
			}
				//
			this.renderer = new CSS3DRenderer();
			this.renderer.setSize( window.innerWidth/2, window.innerHeight );
			document.getElementById( 'container' ).appendChild( this.renderer.domElement );
            
                //
			this.controls = new TrackballControls( this.camera, this.renderer.domElement );
			this.controls.minDistance = 500;
			this.controls.maxDistance = 6000;
			this.controls.addEventListener( 'change', this.render );
            var button = document.getElementById( 'table' );
            var self = this;
			button.addEventListener( 'click', function () {
				self.transform( self.targets.table, 2000 );
			}, false );
            var button = document.getElementById( 'sphere' );
			button.addEventListener( 'click', function () {
				self.transform( self.targets.sphere, 2000 );
			}, false );
			var button = document.getElementById( 'helix' );
			button.addEventListener( 'click', function () {
				self.transform( self.targets.helix, 2000 );
			}, false );
			var button = document.getElementById( 'grid' );
			button.addEventListener( 'click', function () {
				self.transform( self.targets.grid, 2000 );
			}, false );
			this.transform( this.targets.table, 2000 );
                //
			window.addEventListener( 'resize', this.onWindowResize, false );
        },
		transform( targets, duration ) {
			TWEEN.removeAll();
			for ( var i = 0; i < this.objects.length; i ++ ) {
				var object = this.objects[ i ];
				var target = targets[ i ];
				new TWEEN.Tween( object.position )
					.to( { x: target.position.x, y: target.position.y, z: target.position.z }, Math.random() * duration + duration )
					.easing( TWEEN.Easing.Exponential.InOut )
					.start();
				new TWEEN.Tween( object.rotation )
					.to( { x: target.rotation.x, y: target.rotation.y, z: target.rotation.z }, Math.random() * duration + duration )
					.easing( TWEEN.Easing.Exponential.InOut )
					.start();
			}
			new TWEEN.Tween( this )
				.to( {}, duration * 2 )
				.onUpdate( this.render )
				.start();
        },
        
		onWindowResize() {
			this.camera.aspect = window.innerWidth / window.innerHeight;
			this.camera.updateProjectionMatrix();
			this.renderer.setSize( window.innerWidth, window.innerHeight );
			this.render();
        },
        
		animate() {
			requestAnimationFrame( this.animate );
			TWEEN.update();
			this.controls.update();
        },
        
		render() {
			this.renderer.render( this.scene, this.camera );
		}
    }
}
</script>
		

<style>
#container{
    background-color:black;
}
a {
	color: #8ff;
}

#menu {
    position: absolute;
    bottom: 20px;
	width: 100%;
	text-align: center;
}

.button{
    height: 42px;
    padding: 0px;
	min-width: 42px;
}

.buttonImg{
	width: 45px;
	height: 45px;
}

.element {
	width: 120px;
	height: 160px;
	box-shadow: 0px 0px 12px rgba(0,255,255,0.5);
	border: 1px solid rgba(127,255,255,0.25);
	font-family: Helvetica, sans-serif;
	text-align: center;
    line-height: normal;
	cursor: default;
}
			
.element:hover {
	box-shadow: 0px 0px 12px rgba(0,255,255,0.75);
	border: 1px solid rgba(127,255,255,0.75);
}
		
.element .number {
	position: absolute;
	top: 20px;
	right: 20px;
	font-size: 12px;
	color: rgba(127,255,255,0.75);
}

.element .symbol {
	position: absolute;
    top: 40px;
	left: 0px;
	right: 0px;
	font-size: 60px;
	font-weight: bold;
	color: rgba(255,255,255,0.75);
	text-shadow: 0 0 10px rgba(0,255,255,0.95);
    width:120px;
    height:70px;
}

.element .details {
	position: absolute;
	bottom: 15px;
	left: 0px;
	right: 0px;
	font-size: 12px;
	color: rgba(127,255,255,0.75);
}

.iconClass{
	font-size:40px;
	color: rgba(127,255,255,0.75)!important;
}


.divcolor{
	background-color: rgba(1, 69, 71, 9.267);
}
.droneName{
	font-size: 40px;
	color: rgba(127,255,255,0.75);
	text-align: center;
	font-weight: bold;
}

.dronePos{
	display:inline-block; 
	width:33.3%;
	text-align: center;
	font-weight: bold;
	color: rgba(155, 255, 255, 0.75);
	font-size:20px;
}
button {
    color: rgba(155,255,255,0.75);
	background: transparent;
	outline: 1px solid rgba(127,255,255,0.75);
	border: 0px;
	padding: 5px 10px;
	cursor: pointer;
}
			
button:hover {
	background-color: rgba(0,255,255,0.5);
}

button:active {
	color: #000000;
	background-color: rgba(0,255,255,0.75);
}
</style>