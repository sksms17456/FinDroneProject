<template>
    <div>
        <div class="float" style="height:722px;">
            <img id="img" src="../assets/noDroneMap.jpg" style="height: 722px; width:901px; position:absolute;">
            <canvas id="myCanvas" width="901px" height="722px" style=" position:absolute; z-index:2;">
                Your browser does not support the canvas element.
            </canvas>
        </div>
        <div style="width: 618px;height:722px; float:right; background:black;">
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
                                width="440"
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
            <div style="background:black; height:154px; text-align:center">
                <v-btn to="/central" class="button" flat>
                    <img src = "../assets/centralIcon.png" style="width:80px; height:80px;">
				</v-btn>				
                <v-btn to="/home" class="button" flat>
					<img src = "../assets/homeIcon.png" style="width:80px; height:80px;">
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
            drones : [
                {
                    x : -670,
                    y : 31697,
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
        drawRoute(){
            var curThis = this
            this.polling = setInterval(() => {
                const path = `/api/getImg`
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

                    ctx.drawImage(img, 0, 0, 901, 722);
                    ctx.fillStyle = "#FF0000";
                    for(var i=1; i<4; i++){
                        ctx.fillRect((curThis.drones[i].x+curThis.drones[0].x)*3.375 + 137, (curThis.drones[i].y+curThis.drones[0].y)*3.375 + 100, 8, 8);
                    }

                    ctx.beginPath();
                    ctx.lineWidth = "3";
                    ctx.strokeStyle = "blue";
                    ctx.rect(117, 80,580, 580);
                    ctx.stroke();
                    
                    ctx.fillStyle = "rgba(0, 0, 255, 0.1)";
                    ctx.fillRect(117, 80, 580, 580);
                    
                    if(document.getElementsByClassName('error').length>0){
                        ctx.beginPath();
                        ctx.strokeStyle = "red";
                        var idx = document.getElementsByClassName('error')[0].firstChild.firstChild.textContent.substring(7,8);
                        ctx.arc((curThis.drones[idx].x+curThis.drones[0].x)*3.375 + 137+4, (curThis.drones[idx].y+curThis.drones[0].y)*3.375 + 100+4, 50, 50, Math.PI*2, true);
                        ctx.fillStyle = "rgba(255, 0, 0, 0.15)";
                        ctx.fill();
                        ctx.stroke();
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
                ctx.drawImage(img, 0, 0, 901, 722);
            });
        }
    }
}
</script>

<style scoped>
.button{
    width: 170px;
    height: 80px;
    padding: 0px;
    margin-left: 50px;
    margin-right: 50px;
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