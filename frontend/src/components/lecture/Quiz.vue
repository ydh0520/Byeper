<template>
  <div class="quiz">
    <v-row class="quiz-content" align="center">
      <v-col cols="10" style="padding-top: 0; padding-bottom: 0">
        <v-window v-model="window" class="elevation-1" vertical>
          <v-window-item v-for="Quiz in Quizes" :key="Quiz.id">
            <v-row class="quiz-text" align="center">
              <p style="text-align: center">
                {{ Quiz.text }}
              </p>
            </v-row>
          </v-window-item>
        </v-window>
      </v-col>
      <v-col cols="1">
        <v-item-group
          v-model="window"
          class="shrink mr-6"
          mandatory
          tag="v-flex"
        >
          <v-item v-for="n in length" :key="n" v-slot="{ active, toggle }">
            <div>
              <v-btn :input-value="active" icon @click="toggle">
                <v-icon>mdi-record</v-icon>
              </v-btn>
            </div>
          </v-item>
        </v-item-group>
      </v-col>
    </v-row>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class Quiz extends Vue {
  length = 3;
  window = 0;

  Quizes = [
    { id: 1, text: "자료구조는 크게 ____구조와 ____구조로 나뉜다." },
    { id: 2, text: "DFS의 장점은 ____를 적게 사용한다." },
    { id: 3, text: "데이터 분석을 할 때 가장 많이 쓰이는 언어는 ____이다." }
  ];

  mounted() {
    const editorContainer: HTMLElement = document.querySelector(
      ".editor-container"
    ) as HTMLElement;

    editorContainer.style.backgroundColor = "#1E1E1E";
    editorContainer.style.paddingBottom = "0";
  }

  next() {
    this.window = this.window + 1 === this.length ? 0 : this.window + 1;
  }
  prev() {
    this.window = this.window - 1 < 0 ? this.length - 1 : this.window - 1;
  }
}
</script>

<style scoped>
.quiz {
  width: 100%;
}
.quiz-content {
  height: calc(100vh - 100px);
  align-items: center;
  padding: 0;
}
.quiz-text {
  height: calc(100vh - 100px);
  background-color: gray;
}
</style>
