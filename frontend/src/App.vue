<template>
  <v-app>
    <app-navbar />

    <v-main> </v-main>
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import HelloWorld from "./components/HelloWorld.vue";
import AppNavbar from "@/components/app/AppNavbar.vue";

@Component({
  components: {
    HelloWorld,
    AppNavbar
  }
})
export default class App extends Vue {}
</script>
