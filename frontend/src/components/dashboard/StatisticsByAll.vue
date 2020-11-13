<template>
  <v-card class="mx-auto" min-width="344" width="100%" height="250" outlined>
    <v-card-title>학습통계</v-card-title>
    <v-list-item>
      <v-row>
        <v-col>
          <v-progress-circular
            v-if="totalLectureProgress"
            rotate="-90"
            size="100"
            width="15"
            :value="value"
            color="teal"
            >{{ totalLectureProgress.complete }}</v-progress-circular
          >
          <v-card-text>완료 강의수</v-card-text>
        </v-col>
        <v-col>
          <v-progress-circular
            class="graph-class"
            rotate="-90"
            size="100"
            width="15"
            :value="value2"
            color="red"
            >{{ value2 }}</v-progress-circular
          >
          <v-card-text>완료 수업수</v-card-text>
        </v-col>
      </v-row>
    </v-list-item>
  </v-card>
</template>

<script>
import { Component, Vue, Watch } from "vue-property-decorator";
import { namespace } from "vuex-class";

const LecturesModule = namespace("LecturesModule");

@Component
export default class StatisticsByAll extends Vue {
  @LecturesModule.State totalLectureProgress;

  value = 0;
  value2 = 0;
  interval = {};
  interval2 = {};

  beforeDestroy() {
    clearInterval(this.interval);
    clearInterval(this.interval2);
  }

  @Watch("totalLectureProgress", { immediate: true })
  totalCourseInterval() {
    if (this.totalLectureProgress) {
      this.interval = setInterval(() => {
        if (
          this.totalLectureProgress.complete === 0 ||
          this.value >= (20 / this.totalLectureProgress.total) * 100
        ) {
          return;
        }
        this.value += 5;
      }, 80);
    }
  }

  queryAndIndeterminate() {
    this.interval2 = setInterval(() => {
      if (this.value2 === 60) {
        return;
      }
      this.value2 += 10;
    }, 150);

    // this.interval2 = setInterval(() => {
    //   if (this.value2 === 30) {
    //     return;
    //   }
    //   this.value2 += 10;
    // }, 150);
  }

  mounted() {
    this.queryAndIndeterminate();
  }
}
</script>

<style scoped></style>
