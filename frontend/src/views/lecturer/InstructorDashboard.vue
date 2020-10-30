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
          name: "댓글"
        },
        {
          name: "오우야"
        },
        {
          name: "타타타"
        }
      ]
    }
  }

}
</script>

<style scoped></style>
