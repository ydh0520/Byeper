<template>
  <v-app>
    <app-navbar />
    <app-main style=" margin-top: 64px;" />
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import AppNavbar from "@/components/app/AppNavbar.vue";
import AppMain from "@/components/app/AppMain.vue";

@Component({
  components: {
    AppNavbar,
    AppMain
  }
})
export default class App extends Vue {}
</script>
