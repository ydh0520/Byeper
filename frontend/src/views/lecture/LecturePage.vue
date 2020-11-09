<template>
  <v-row class="lecture-container">
    <v-col class="video-container">
      <div class="lecture-video">
        <lecture-video @player="getPlayer" />
      </div>
      <!-- <youtube :video-id="videoURL" ref="youtube"></youtube> -->
      <!-- <iframe
        class="lecture-video"
        width="100%"
        height="371"
        :src="videoURL"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe> -->
    </v-col>
    <v-col class="editor-container">
      <v-row style="margin: 0px">
        <v-col class="menu-col">
          <v-btn class="menu-btn" tile @click="toNoteTab">노트</v-btn>
        </v-col>
        <v-col class="menu-col">
          <v-btn class="menu-btn" tile @click="toListTab">목록</v-btn>
        </v-col>
      </v-row>
      <text-editor
        :player="player"
        v-if="$route.query.tab === 'note' || !$route.query.tab"
      />
      <v-btn @click="startVideo">{{ $route.query.tab }}</v-btn>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import TextEditor from "@/components/lecture/TextEditor.vue";
import Curriculum from "@/components/lecture/Curriculum.vue";
import LectureVideo from "@/components/lecture/LectureVideo.vue";

@Component({
  components: {
    TextEditor,
    Curriculum,
    LectureVideo
  }
})
export default class LecturePage extends Vue {
  player: {} | null = null;
  start = 0;

  videoURL = "s9FHdj6jd_U";

  startVideo() {
    this.start += 10;
    this.player.seekTo(this.start);
  }
  toNoteTab() {
    this.$router.replace({ name: "LecturePage", query: { tab: "note" } });
  }
  toListTab() {
    this.$router.replace({ name: "LecturePage", query: { tab: "list" } });
  }
  getPlayer(v: {}) {
    this.player = v;
  }
  scroll(event) {
    event.preventDefault();
    event.stopPropagation();
  }
  async preventScroll() {
    const video = await document.querySelector(".video-container");
    video?.addEventListener("scroll", this.scroll);
    video?.addEventListener("mousewheel", this.scroll);
  }

  mounted() {
    this.preventScroll();
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
  min-width: 650px;
  height: 100%;
  padding: 0;
  background-color: black;
  overflow: hidden;
  overflow-x: hidden;
  overflow-y: hidden;
}
.editor-container {
  width: 50%;
  min-width: 300px;
  height: 100%;
  padding: 0;
  background-color: white;
  padding-bottom: 100px;
}
.lecture-video {
  position: fixed;
  top: 30%;
}
.menu-col {
  padding: 0;
}
.menu-btn {
  width: 100%;
}
</style>
