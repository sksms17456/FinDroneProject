<template>
    <div>
        <div class="float" style="height:864px;">
            <img id="img" :src='getImgUrl("noDroneMap.jpg")' style="height:864px; width:1110px; position:absolute;">
            <canvas id="myCanvas" width="1110px" height="864px" style=" position:absolute; z-index:2;">
                Your browser does not support the canvas element.
            </canvas>
        </div>
        <div style="width:635px; height:864px; width:426px; float:right; background:black;">
            <v-item-group style="height:568px;">
                <v-container grid-list-md style="width:inherit; height:inherit;">
                    <v-layout wrap class="align-center justify-center">
                        <v-flex
                        v-for="n in 3"
                        :key="n"
                        xs12
                        md4
                        style="padding:28px;"
                        >
                            <v-item>
                                <v-card
                                slot-scope="{ active, toggle }"
                                :color="active ? 'error' : 'primary'"
                                class="d-flex align-center"
                                dark
                                height="120"
                                width="340"
                                @click="toggle"
                                >
                                    <v-scroll-y-transition>
                                        <div class="display-1 text-xs-center">
                                            <div style="padding:3px;"> Drone {{n}}</div>
                                            <div style="font-size:22px; white-space:pre-line; line-height:26px;">X : {{drones[n].x}}
                                                Y : {{drones[n].y}} 
                                                Z : {{drones[n].z}}
                                            </div> 
                                        </div>
                                    </v-scroll-y-transition>
                                </v-card>
                            </v-item>
                        </v-flex>
                    </v-layout> 
                </v-container>
            </v-item-group>
            <div style="background:black; height:296px; text-align:center; padding-top:100px;">
                <v-btn to="/central" class="button" flat>
                    <img :src='getImgUrl("centralIcon.png")' class="buttonImg">
				</v-btn>				
                <v-btn to="/home" class="button" flat>
					<img :src='getImgUrl("homeIcon.png")' class="buttonImg">
				</v-btn>
            </div>
        </div>
    </div>
</template>

<script>
import $ from 'jquery';
import axios from 'axios';

export default {
    name: "RootMap",
    data(){
        return{
            scale : 3.9875,
            mapWidth:1110,
            mapHeight:864,
            drones : [
                {
                    x : 627.23,
                    y : -31727.1,
                },
                {
                    x : 0,
                    y : 0,
                    z : 0
                },
                {
                    x : 0,
                    y : 0,
                    z : 0
                },
                {
                    x : 0,
                    y : 0,
                    z : 0
                }
            ]
        }
    },
    created(){
        this.drawCanvas();
        this.drawRoute();
    },
    methods:{
        getImgUrl(img){
            return require('../assets/'+img);
		},
        drawRoute(){
            var curThis = this
            this.polling = setInterval(() => {
                const path = `/api/getInfo`
                    axios.get(path)
                    .then(response => {
                        const pos = [response.data.pos0, response.data.pos1, response.data.pos2]
                        for(var i=0; i<3; i++){
                            curThis.drones[i+1].x = pos[i][0];
                            curThis.drones[i+1].y = pos[i][1];
                            curThis.drones[i+1].z = pos[i][2];
                        }
                    })
                    .catch(error => {
                        console.log(error)
                    })

                $(function(){
                    var canvas = document.getElementById("myCanvas");
                    var ctx = canvas.getContext("2d");
                    var img = document.getElementById("img");

                    ctx.drawImage(img, 0, 0, curThis.mapWidth, curThis.mapHeight);
                    for(var i=1; i<4; i++){
                        ctx.beginPath();
                        ctx.fillStyle = "#FF0000";
                        ctx.fillRect((curThis.drones[i].x-curThis.drones[0].x)*curThis.scale, (curThis.drones[i].y-curThis.drones[0].y)*curThis.scale, 8, 8);
                        ctx.strokeStyle = "red";
                        ctx.arc((curThis.drones[i].x-curThis.drones[0].x)*curThis.scale + 4, (curThis.drones[i].y-curThis.drones[0].y)*curThis.scale + 4, 50, 50, Math.PI*2, true);
                        ctx.stroke();
                        ctx.fillStyle = "rgba(255, 0, 0, 0.15)";
                        ctx.fill();
                    }

                    ctx.beginPath();
                    ctx.lineWidth = "3";
                    ctx.strokeStyle = "blue";
                    ctx.rect((669.86-curThis.drones[0].x)*curThis.scale - curThis.scale*10, (-31697.01-curThis.drones[0].y)*curThis.scale - curThis.scale*10, 180*curThis.scale, 180*curThis.scale);
                    ctx.stroke();
                    ctx.fillStyle = "rgba(0, 0, 255, 0.1)";
                    ctx.fillRect((669.86-curThis.drones[0].x)*curThis.scale - curThis.scale*10, (-31697.01-curThis.drones[0].y)*curThis.scale - curThis.scale*10, 180*curThis.scale, 180*curThis.scale);
                    
                    const path = `/api/getFindArea`
                        axios.get(path)
                        .then(response => {
                            if(response.data.isFind){
                                const pos = [response.data.x, response.data.y]
                                ctx.beginPath();
                                ctx.strokeStyle = "green";
                                ctx.arc((pos[0]-curThis.drones[0].x)*curThis.scale, (pos[1]-curThis.drones[0].y)*curThis.scale, 35.35*curThis.scale, 50, Math.PI*2, true);
                                ctx.stroke();
                                ctx.fillStyle = "rgba(0,255,0,0.1)";
                                ctx.fill();
                            }
                        })
                        .catch(error => {
                            console.log(error)
                        })

                    if(document.getElementsByClassName('error').length>0){
                        var idx = document.getElementsByClassName('error')[0].firstChild.firstChild.textContent.substring(7,8);
                        ctx.beginPath();
                        ctx.strokeStyle = "red";
                        ctx.arc((curThis.drones[idx].x-curThis.drones[0].x)*curThis.scale + 4, (curThis.drones[idx].y-curThis.drones[0].y)*curThis.scale + 4, 50, 50, Math.PI*2, true);
                        ctx.stroke();
                        ctx.fillStyle = "rgba(255, 0, 0, 0.4)";
                        ctx.fill();
                    }
                }); 
            }, 1000)
        },
        drawCanvas(){
            var curThis = this;
            $(function(){
                var canvas = document.getElementById("myCanvas");
                var ctx = canvas.getContext("2d");
                var img = document.getElementById("img");
                ctx.drawImage(img, 0, 0, curThis.mapWidth, curThis.mapHeight);
            });
        }
    }
}
</script>

<style scoped>
.button{
    width: 80px;
    height: 80px;
    padding: 0px;
    margin-left: 50px;
    margin-right: 50px;
}
.buttonImg{
    width: 80px;
    height: 80px;
}
.iconClass{
    font-size:60px;
}
.float {
    float:left;
}
.v-content__wrap{
    background: black;
}
.flex.md4{
    max-width:100%;
}
</style>