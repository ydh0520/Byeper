<template>
  <v-row justify="center" align="center">
    <v-card v-if="isSlider" light outlined class="capture-slider">
      <v-subheader>민감도</v-subheader>
      <v-slider
        :tick-labels="ticksLabels"
        :max="2"
        color="teal"
        step="1"
        ticks="always"
        tick-size="4"
      ></v-slider>
    </v-card>
    <v-chip class="chip chip-btn" color="indigo darken-3" outlined x-large>
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
import { Component, Vue, Prop } from "vue-property-decorator";
import h2c from "html2canvas";

@Component
export default class ImageCaptureChip extends Vue {
  @Prop(Object) readonly player: any;

  ticksLabels = ["하", "중", "상"];

  isSlider = false;

  addCapture(img: string) {
    this.$emit("addCapture", img);
  }
  capture() {
    h2c(document.querySelector(".editor__content") as HTMLElement)
      .then(canvas => this.addCapture(canvas.toDataURL("image/jpeg")))
      .catch(err => console.error(err));
  }
  async imageCapture() {
    this.capture();
    const getVideoTime = await this.player.getCurrentTime();
    console.log(getVideoTime);
  }
  imageCaptureAll() {
    console.log("all");
    this.isSlider = !this.isSlider;
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
  bottom: 10px;
  margin: 0 auto;
}
.capture-slider {
  padding: 10px;
  position: fixed;
  bottom: 90px;
  width: 250px;
  margin: 0 auto;
}
</style>
