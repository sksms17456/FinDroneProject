<template>
	<div>
		<div style="width:50%; display:inline-block;">
			<div class="div_border droneName" style="height:10%">
				Drone-{{target.idx}}
			</div>
			<div class="div_border" style="height:80%">
				<v-img
				:src="getImgUrl('detect.png')"
				height="86.6vh"
            	>
				</v-img>
			</div>
			<div style="height:10%">
				<div class="div_border dronePos">X : {{target.x_pos}} </div>
				<div class="div_border dronePos">Y : {{target.y_pos}} </div>
				<div class="div_border dronePos">Z : {{target.z_pos}} </div>
			</div>
		</div>

		<div style="width:50%; display:inline-block;">
			<div id="container" style="width:100%"></div>
			<div id="menu" style="width:inherit">
				<button id="table">TABLE</button>
				<button id="sphere">SPHERE</button>
				<button id="helix">HELIX</button>
				<button id="grid">GRID</button>
			</div>
			<!-- <v-dialog v-model="dialog" width="600px">
				<v-card>
					<v-card-title
					class="headline grey lighten-2"
					primary-title
					>
					드론00 화면
					</v-card-title>
					<v-card-text>
						<v-img :src="getImgUrl('logo.png')"></v-img>
					</v-card-text>
					<v-divider></v-divider>
					<v-card-actions>
					<v-spacer></v-spacer>
						<v-btn
							color="primary"
							flat
							@click="dialog = false"
						>
							닫기
						</v-btn>
					</v-card-actions>
				</v-card>
			</v-dialog>         -->
    	</div>
	</div>    
</template>

<script>
import * as THREE from '../plugins/three.module.js';
import { TWEEN } from '../plugins/tween.module.min.js';
import { TrackballControls } from '../plugins/TrackballControls.js';
import { CSS3DRenderer, CSS3DObject } from '../plugins/CSS3DRenderer.js';

export default {
    name:'MultiMonitor',
    data(){
        return{
			mapImg: 'mappin.gif',
			// dialog:false,
			target : {
				idx : 1,
				x_pos : 0,
				y_pos : 0,
				z_pos : 0
			},
            table : [
				"1", "0.0", "0.0", "0.0", 1, 1,
				"2", "0.0", "0.0", "4.002602", 2, 1,
				"3", "0.0", "0.0", "6.941", 3, 1,
				"4", "0.0", "0.0", "9.012182", 4, 1,
				"5", "0.0", "0.0", "10.811", 5, 1,
				"6", "0.0", "0.0", "12.0107", 6, 1,
				"7", "0.0", "0.0", "14.0067", 7, 1,
				"8", "0.0", "0.0", "15.9994", 8, 1,
				"9", "0.0", "0.0", "26.9815386", 1, 2,
				"10", "0.0", "0.0", "28.0855", 2, 2,
				"11", "0.0", "0.0", "30.973762", 3, 2,
				"12", "0.0", "0.0", "32.065", 4, 2,
				"13", "0.0", "0.0", "35.453", 5, 2,
				"14", "0.0", "0.0", "39.948", 6, 2,
				"15", "0.0", "0.0", "39.948", 7, 2,
				"16", "0.0", "0.0", "40.078", 8, 2,
				"17", "0.0", "0.0", "54.938045", 1, 3,
				"18", "0.0", "0.0", "55.845", 2, 3,
				"19", "0.0", "0.0", "58.933195", 3, 3,
				"20", "0.0", "0.0", "58.6934", 4, 3,
				"21", "0.0", "0.0", "63.546", 5, 3,
				"22", "0.0", "0.0", "65.38", 6, 3,
				"23", "0.0", "0.0", "69.723", 7, 3,
				"24", "0.0", "0.0", "72.63", 8, 3,
				"25", "0.0", "0.0", "114.818", 1, 4,
				"26", "0.0", "0.0", "118.71", 2, 4,
				"27", "0.0", "0.0", "121.76", 3, 4,
				"28", "0.0", "0.0", "127.6", 4, 4,
				"29", "0.0", "0.0", "126.90447", 5, 4,
				"30", "0.0", "0.0", "131.293", 6, 4,				
				"31", "0.0", "0.0", "144.242", 7, 4,
				"32", "0.0", "0.0", "(145)", 8, 4,
				"33", "0.0", "0.0", "85.4678", 1, 5,
				"34", "0.0", "0.0", "87.62", 2, 5,
				"35", "0.0", "0.0", "88.90585", 3, 5,
				"36", "0.0", "0.0", "91.224", 4, 5,
				"37", "0.0", "0.0", "92.90628", 5, 5,
				"38", "0.0", "0.0", "95.96", 6, 5,
				"39", "0.0", "0.0", "(98)", 7, 5,
				"40", "0.0", "0.0", "101.07", 8, 5,
				"41", "0.0", "0.0", "132.9054", 1, 6,
				"42", "0.0", "0.0", "132.9054", 2, 6,
				"43", "0.0", "0.0", "138.90547", 3, 6,
				"44", "0.0", "0.0", "140.116", 4, 6,
				"45", "0.0", "0.0", "140.90765", 5, 6,
				"46", "0.0", "0.0", "95.96", 6, 6,
				"47", "0.0", "0.0", "(98)", 7, 6,
				"48", "0.0", "0.0", "101.07", 8, 6,				
			],
            camera:'',
            scene:'',
            renderer:'',
			controls:'',
			objects : [],
			targets : { table: [], sphere: [], helix: [], grid: [] },
        }
    },
    mounted(){
        this.init();
		this.animate();
    },
    methods:{
        getImgUrl(img){
            return require('../assets/'+img);
        },
        // change(){
        //     console.log()
		// 	this.dialog=true
			
        // },
        init() {
			this.camera = new THREE.PerspectiveCamera( 40, window.innerWidth / window.innerHeight, 1, 10000 );
			this.camera.position.z = 1600
            this.scene = new THREE.Scene();
            var self= this;
				// table
			for ( var i = 0; i < this.table.length; i += 6 ) {
				var element = document.createElement( 'div' );
				element.className = 'element';
                element.style.backgroundColor = 'rgba(0,127,127,' + ( Math.random() * 0.5 + 0.25 ) + ')';

				var number = document.createElement( 'div' );
				number.className = 'number';
				number.style = 'text-align:center; width:100%; top:2px; font-size:15px; right:0px;'
				number.textContent = ( i / 6 ) + 1;
                element.appendChild( number );

				var symbol = document.createElement( 'img' );
				symbol.className = 'symbol '+ String(( i / 6 ) + 1);
				symbol.style = 'top:20px; height:90px;'
                // symbol.textContent = this.table[ i ];
                symbol.src=this.getImgUrl('detect.png')
                element.appendChild( symbol );
                
				var details = document.createElement( 'div' );
				details.className = 'details '+ String(( i / 6 ) + 1);
				details.style = 'bottom:5px;'
				details.innerHTML = this.table[ i + 1 ] + '<br>' + this.table[ i + 2 ] + '<br>' + this.table[ i + 3 ];
                element.appendChild( details );
				
				element.addEventListener('click',function() {
					// self.change();
					// self.target.idx = this.getElementsByClassName('number')[0].textContent;
					// self.target.x_pos = this.getElementsByClassName('details')[0].innerHTML.split("<br>")[0];
					// self.target.y_pos = this.getElementsByClassName('details')[0].innerHTML.split("<br>")[1];
					// self.target.z_pos = this.getElementsByClassName('details')[0].innerHTML.split("<br>")[2];
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

.div_border{
	border:1.5px solid black;
}

.droneName{
	font-size: 40px;
	text-align: center;
	font-weight: bold;
}

.dronePos{
	display:inline-block; 
	width:33.3%;
	text-align: center;
	font-weight: bold;
	font-size:25px;
}
button {
    color: rgba(127,255,255,0.75);
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