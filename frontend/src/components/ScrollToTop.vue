<template>
    <v-fade-transition>
        <v-btn
            v-show="showButton()"
            v-scroll="onScroll"
            class="md-5 mr-3 elevation-21"
            fab
            bottom
            right
            color="black"
            dark
            fixed
            @click="top"
        >
        <v-icon color="white">mdi mdi-arrow-up</v-icon>
        </v-btn>
    </v-fade-transition>
</template>

<script>
export default {
    name: "Scrolltotop",
    data() {
        return {
            offsetTop: 0,
            icon:"fab fa-arrow-up"
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
