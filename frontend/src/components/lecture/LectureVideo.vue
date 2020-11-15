<template>
  <youtube
    v-if="lecture"
    :video-id="lecture.video_id"
    fitParent
    :player-vars="playerVars"
    @playing="playing"
    ref="youtube"
  ></youtube>
</template>

<script>
import { Component, Vue, Watch } from "vue-property-decorator";
import { namespace } from "vuex-class";
import { Lecture } from "../../store/Lectures.interface";

const LecturesModule = namespace("LecturesModule");

@Component
export default class LectureVideo extends Vue {
  @LecturesModule.State lecture;

  playerVars = {
    start: 15
  };

  @Watch("lecture", { immediate: true, deep: true })
  emitVideo() {
    console.log("수업", this.lecture);
    if (this.lecture) {
      setTimeout(() => {
        if (this.$refs.youtube) {
          console.log("제발", this.$refs.youtube);
          this.$emit("player", this.$refs.youtube.player);
        }
      }, 50);
    }
  }

  async checkComplete() {
    const currentTime = await this.$refs.youtube.player.getCurrentTime();
    console.log(currentTime);
  }
  playing() {
    console.log("재생중");
    // setInterval(this.checkComplete, 2000);
  }
}
</script>

<style scoped></style>
