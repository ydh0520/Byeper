<template>
  <div>
    <v-stepper v-model="CreateLectureStep">
      <v-stepper-header>
        <v-stepper-step :complete="CreateLectureStep > 1" step="1">
          강의 정보 입력
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step :complete="CreateLectureStep > 2" step="2">
          커리큘럼
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step step="3">
          커버 이미지
        </v-stepper-step>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content step="1">
          <v-card class="mb-12" color="grey lighten-1" height="200px"></v-card>

          <v-btn color="primary" @click="CreateLectureStep = 2">
            Continue
          </v-btn>

          <v-btn text>
            Cancel
          </v-btn>
        </v-stepper-content>

        <v-stepper-content step="2">
          <v-card class="mb-12" color="grey lighten-1">
            <v-container fluid class="wrapper">
              <v-row>
                <v-col>
                  <div class="list">
                    <drag
                      v-for="n in [1, 2, 3, 4, 5]"
                      :data="n"
                      class="item"
                      :key="n"
                      >{{ n }}</drag
                    >
                  </div>
                </v-col>
                <v-col>
                  <drop-list
                    :items="items"
                    class="list"
                    @insert="onInsert"
                    @reorder="$event.apply(items)"
                  >
                    <template v-slot:item="{ item }">
                      <drag class="item" :key="item">{{ item }}</drag>
                    </template>
                    <template v-slot:feedback="{ data }">
                      <div class="item feedback" :key="data">{{ data }}</div>
                    </template>
                  </drop-list>
                </v-col>
              </v-row>
            </v-container>
          </v-card>

          <v-btn color="primary" @click="CreateLectureStep = 3">
            Continue
          </v-btn>

          <v-btn text>
            Cancel
          </v-btn>
        </v-stepper-content>

        <v-stepper-content step="3">
          <v-card class="mb-12" color="grey lighten-1" height="200px"></v-card>

          <v-btn color="primary" @click="CreateLectureStep = 1">
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
import { Drag, DropList } from "vue-easy-dnd";

@Component({
  components: {
    Drag,
    DropList
  }
})
export default class CreateLecture extends Vue {
  items = ["a", "b", "c", "d", "e"];
  CreateLectureStep = 1;

  onInsert(event: any) {
    this.items.splice(event.index, 0, event.data);
  }
}
</script>

<style lang="scss">
html,
body,
#app,
.v-application--wrap,
.v-content,
.v-content__wrap {
  height: 100%;
}

.drop-in {
  box-shadow: 0 0 10px rgba(0, 0, 255, 0.3);
}
</style>

<style scoped lang="scss">
.wrapper {
  .list {
    border: 1px solid black;
    margin: 100px auto;
    width: 200px;

    .item {
      padding: 20px;
      margin: 10px;
      background-color: rgb(220, 220, 255);
      display: flex;
      align-items: center;
      justify-content: center;

      &.feedback {
        background-color: rgb(255, 220, 220);
        border: 2px dashed black;
      }

      &.drag-image {
        background-color: rgb(220, 255, 220);
        transform: translate(-50%, -50%);
      }
    }
  }
}
</style>

