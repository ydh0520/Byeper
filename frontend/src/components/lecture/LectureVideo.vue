<template>
  <youtube :video-id="videoURL" fitParent ref="youtube"></youtube>
</template>

<script>
import { Component, Vue } from "vue-property-decorator";

@Component
export default class LectureVideo extends Vue {
  videoURL = "6AnnvVrth4w";
  mounted() {
    this.$emit("player", this.$refs.youtube.player);
  }
}
</script>

<style scoped></style>
