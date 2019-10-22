<template>
  <v-toolbar fixed>
    <!-- <img alt="FinDrone logo" src="../assets/headerlogo.png"> -->
    <v-toolbar-side-icon></v-toolbar-side-icon>
    <v-toolbar-title>FinDrone</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">
      <v-btn to="/" flat>HOME</v-btn>
      <v-btn flat>POST</v-btn>
      <v-btn to="/find" flat>FIND</v-btn>
      <v-btn flat>LOGIN</v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>