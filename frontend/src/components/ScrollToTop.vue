<template>
    <v-fade-transition>
        <v-btn
            v-show="showButton()"
            v-scroll="onScroll"
            fab
            bottom
            right
            color="white"
            dark
            fixed
            @click="top"
        >
        <i class="fas fa-arrow-up" color="black" ></i> 
        </v-btn>
    </v-fade-transition>
</template>

<script>
export default {
    name: "Scrolltotop",
    data() {
        return {
            offsetTop: 0
        };
    },
    methods: {
        top() {
            window.scrollTo({
                top: 0,
                left: 0,
                behavior: "smooth"
            });
        },
        onScroll() {
            this.offsetTop = window.scrollY;
        },
        showButton() {
            if (this.offsetTop > 30) {
                return true;
            }
            return false;
        }
    }
};
</script>
