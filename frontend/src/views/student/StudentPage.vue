<template>
  <div class="student-page mx-auto mt-10">
    <div class="text-h3 my-5">
      학생페이지
    </div>
    <v-row>
      <v-col>
        <profile />
        <statistics-by-all />
      </v-col>
      <v-col>
        <finished-lecture />
        <learning-video />
      </v-col>
    </v-row>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import Profile from "@/components/dashboard/Profile.vue";
import StatisticsByAll from "@/components/dashboard/StatisticsByAll.vue";
import LearningVideo from "@/components/dashboard/LearningVideo.vue";
import FinishedLecture from "@/components/dashboard/FinishedLecture.vue";

@Component({
  components: {
    Profile,
    StatisticsByAll,
    LearningVideo,
    FinishedLecture
  }
})
export default class StudentPage extends Vue {}
</script>

<style scoped>
.student-page {
  width: 80%;
}
</style>
