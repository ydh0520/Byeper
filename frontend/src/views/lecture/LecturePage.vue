<template>
  <v-row class="lecture-container">
    <v-col class="video-container">
      비디오
      <iframe
        class="lecture-video"
        width="100%"
        height="371"
        :src="videoURL"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe>
    </v-col>
    <v-col class="editor-container">
      <text-editor />
      <v-btn @click="startVideo">버튼</v-btn>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import TextEditor from "@/components/lecture/TextEditor.vue";

@Component({
  components: {
    TextEditor
  }
})
export default class LecturePage extends Vue {
  start = 0;

  videoURL = "https://www.youtube.com/embed/s9FHdj6jd_U";

  startVideo() {
    this.start += 10;
    this.videoURL = `https://www.youtube.com/embed/s9FHdj6jd_U?autoplay=1&start=${this.start}`;
  }
}
</script>

<style scoped>
.lecture-container {
  height: 100%;
}
.video-container {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 50%;
  min-width: 450px;
  height: 100%;
  padding: 0;
  background-color: black;
  overflow: hidden;
}
.editor-container {
  width: 50%;
  min-width: 300px;
  height: 100%;
  padding: 0;
  background-color: white;
}
.lecture-video {
  position: fixed;
  top: 30%;
  left: 0;
  width: 50%;
}
</style>
