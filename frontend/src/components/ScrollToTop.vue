<template>
    <v-fade-transition>
        <v-btn
            v-scroll="onScroll"
            fab
            bottom
            right
            light
            fixed
            @click="next"
        >
          <v-icon id="scrollBtn" style="height:20px">fas fa-arrow-down</v-icon>
        </v-btn>
    </v-fade-transition>
</template>

<script>
import $ from 'jquery'

export default {
    name: "Scrolltotop",
    data() {
        return {
            offsetTop: 0,
            next_top: 658,
            next_left: 0,
        };
    },
    watch: {
        offsetTop: function(newVal, oldVal){
            if (this.offsetTop > 30) {
                this.next_top = 0
                $('#scrollBtn').attr('data-icon', 'arrow-up')
            } else {
                this.next_top = 658
                $('#scrollBtn').attr('data-icon', 'arrow-down')
            }
        }
    },
    methods: {
        next() {
            window.scrollTo({
                top: this.next_top,
                left: this.left,
                behavior: "smooth"
            });
        },
        onScroll() {
            this.offsetTop = window.scrollY;
        }
    }
};
</script>
