<template>
  <div>
    <v-tabs :key="tab.name" v-for="tab in instructorTabs">
      <v-tab>
        {{ tab.name }}
      </v-tab>
    </v-tabs>
    <v-stepper v-model="CreateLectureStep">
      <v-stepper-header>
        <v-stepper-step
            :complete="CreateLectureStep > 1"
            step="1"
        >
          Name of step 1
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step
            :complete="CreateLectureStep > 2"
            step="2"
        >
          Name of step 2
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step step="3">
          Name of step 3
        </v-stepper-step>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content step="1">
          <v-card
              class="mb-12"
              color="grey lighten-1"
              height="200px"
          ></v-card>

          <v-btn
              color="primary"
              @click="CreateLectureStep = 2"
          >
            Continue
          </v-btn>

          <v-btn text>
            Cancel
          </v-btn>
        </v-stepper-content>

        <v-stepper-content step="2">
          <v-card
              class="mb-12"
              color="grey lighten-1"
              height="200px"
          ></v-card>

          <v-btn
              color="primary"
              @click="CreateLectureStep = 3"
          >
            Continue
          </v-btn>

          <v-btn text>
            Cancel
          </v-btn>
        </v-stepper-content>

        <v-stepper-content step="3">
          <v-card
              class="mb-12"
              color="grey lighten-1"
              height="200px"
          ></v-card>

          <v-btn
              color="primary"
              @click="CreateLectureStep = 1"
          >
            Continue
          </v-btn>

          <v-btn text>
            Cancel
          </v-btn>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";

@Component
export default class CreateLecture extends Vue {
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
      ],
      CreateLectureStep: 1,
    }
  }

}
</script>

<style scoped></style>
