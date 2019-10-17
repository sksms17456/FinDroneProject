<template>
  <v-toolbar>
    <v-toolbar-side-icon class="hidden-sm-and-up"></v-toolbar-side-icon>
      <v-icon src=""></v-icon>
      <v-toolbar-title>여기에 로고넣어줘욤</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn to="/" flat>FinDrone</v-btn>
        <v-btn to="/about" flat>About</v-btn>
        <v-btn to="/service" flat>Service</v-btn>
        <v-btn to="/central" flat>Central</v-btn>
     </v-toolbar-items>
     <v-spacer></v-spacer>
     <v-toolbar-items>
        <v-btn flat>Log In - Sign Up</v-btn>
        <v-btn flat>Log Out</v-btn>
     </v-toolbar-items>
  </v-toolbar>
</template>