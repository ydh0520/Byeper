<template>
  <v-main>
    <v-fade-transition mode="out-in">
      <router-view style="background: rgba(0, 0, 0, 0.05)" />
    </v-fade-transition>
  </v-main>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class AppMain extends Vue {}
</script>

<style></style>
