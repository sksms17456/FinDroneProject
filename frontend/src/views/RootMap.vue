<template>
    <div>
        <div class="float" style="height:722px; width:398px; background:black;">
        </div>
        <div class="float" style="height:722px; width:722px;">
            <img id="img" src="../assets/map.jpg" style="width:inherit; position:absolute;">
            <canvas id="myCanvas" width="722" height="722" style=" position:absolute; z-index:2;">
                Your browser does not support the canvas element.
            </canvas>
        </div>
        <div class="float" style="height:722px; width:399px; background:black;">
        </div>
    </div>
</template>

<script>
import $ from 'jquery';

export default {
    name: "RootMap",
    data(){
        return{
            drones : [
                {
                    x : 80,
                    y : 80,
                },
                {
                    x : 80,
                    y : 480,
                },
                {
                    x : 480,
                    y : 480,
                },
                {
                    x : 480,
                    y : 80,
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
                $(function(){
                    var canvas = document.getElementById("myCanvas");
                    var ctx = canvas.getContext("2d");
                    var ctx2 = canvas.getContext("2d");
                    var img = document.getElementById("img");
                    ctx.drawImage(img, 0, 0, 722, 722);
                    
                    ctx2.fillStyle = "rgba(0, 0, 255, 0.15)";
                    ctx2.fillRect(60, 60, 440, 440);
                    
                    ctx.beginPath();
                    ctx.lineWidth = "3";
                    ctx.strokeStyle = "blue";
                    ctx.rect(60, 60, 440, 440);
                    ctx.stroke();
                    ctx.fillStyle = "#FF0000";

                    curThis.drones[0].y += 3;
                    curThis.drones[1].x += 3;
                    curThis.drones[2].y -= 3;
                    curThis.drones[3].x -= 3;
                    for(var i=0; i<4; i++){
                        ctx.fillRect(curThis.drones[i].x, curThis.drones[i].y, 8, 8);
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
                ctx.drawImage(img, 0, 0, 722, 722);
            });
        }
    }
}
</script>

<style>
.float {
    float:left;
}
</style>