<template>
  <v-row justify="center" align="center">
    <v-chip class="chip chip-btn ma-2" color="indigo darken-3" outlined x-large>
      <v-btn class="mx-2" fab icon large color="teal" @click="imageCapture">
        <v-icon>mdi-camera-outline</v-icon>
      </v-btn>
      <v-btn class="mx-2" fab icon large color="teal" @click="imageCaptureAll">
        <v-icon>mdi-image-multiple-outline</v-icon>
      </v-btn>
    </v-chip>
  </v-row>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class ImageCaptureChip extends Vue {
  imageCapture() {
    console.log("capture");
  }

  imageCaptureAll() {
    console.log("all");
  }
}
</script>

<style scoped>
.v-chip:before {
  background-color: inherit !important;
}
.chip-btn {
  width: 186px;
  position: fixed;
  bottom: 3%;
  margin: 0;
}
</style>
