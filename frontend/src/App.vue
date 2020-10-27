<template>
  <v-app>
    <app-navbar />
    <app-main />
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import HelloWorld from "./components/HelloWorld.vue";
import AppNavbar from "@/components/app/AppNavbar.vue";
import AppMain from "@/components/app/AppMain.vue";

@Component({
  components: {
    HelloWorld,
    AppNavbar,
    AppMain
  }
})
export default class App extends Vue {}
</script>
