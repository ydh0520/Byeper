<template>
  <div>
    <v-tabs :key="tab.name" v-for="tab in instructorTabs">
      <v-tab>
        {{ tab.name }}
      </v-tab>
    </v-tabs>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";

@Component
export default class InstructorDashboard extends Vue {
  data() {
    return {
      instructorTabs: [
        {
          name: "대시보드"
        },
        {
          name: "강의 만들기"
        },
        {
          name: "강의 관리"
        },
        {
          name: "피드백"
        }
      ]
    }
  }

}
</script>

<style scoped></style>
