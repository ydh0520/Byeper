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
          <v-card dark flat class="mb-12" style="margin: 10px 20%">
            <h3 class="mb-0">강의 제목</h3>
            <v-text-field class="classdesc mb-0" height="20" outlined></v-text-field>
            <h3 class="my-0">강의 설명</h3>
            <v-text-field class="classdesc" height="20" outlined></v-text-field>
            <h3 class="my-0">선수 과목, 지식</h3>
            <v-text-field class="classdesc" height="20" outlined></v-text-field>
            <h3>카테고리</h3>
            <v-chip-group column multiple v-model="LectureCategories">
              <v-chip label filter outlined>
                개발ㆍ프로그래밍
              </v-chip>
              <v-chip label filter outlined>
                데이터 사이언스
              </v-chip>
              <v-chip label filter outlined>
                크리에이티브
              </v-chip>
              <v-chip label filter outlined>
                업무 스킬
              </v-chip>
              <v-chip label filter outlined>
                직무기초ㆍ학문
              </v-chip>
              <v-chip label filter outlined>
                커리어
              </v-chip>
            </v-chip-group>
            <h3>강의 수준</h3>
            <v-chip-group mandatory v-model="LectureDifficulty">
              <v-chip filter outlined>
                입문
              </v-chip>
              <v-chip filter outlined>
                초급
              </v-chip>
              <v-chip filter outlined>
                중급이상
              </v-chip>
            </v-chip-group>
          <v-btn class="mt-12 mx-auto" color="primary" @click="CreateLectureStep = 2">
            다음 단계로
          </v-btn>
          <v-btn class="mt-12">
            취소하기
          </v-btn>
          </v-card>
        </v-stepper-content>

        <v-stepper-content step="2">
          <v-card class="mb-12">
            <v-container fluid class="wrapper">
              <v-row>
                <v-col>
                  <v-card>
                    <h2>내 동영상</h2>
                    <div class="list" style="height: 75vh">
                      <drag
                          v-for="video in UserVideos"
                          :data="video"
                          class="item"
                          :key="video"
                      >
                        <v-list-item>
                          <v-list-item-content>
                            <v-list-item-title>파이썬 조아</v-list-item-title>
                            <v-list-item-content>호호</v-list-item-content>
                          </v-list-item-content>
                        </v-list-item>
                      </drag
                      >
                    </div>
                  </v-card>
                </v-col>
                <v-col>
                  <drop-list
                    v-for="(Section, idx) in SelectedVideos"
                    :items="Section"
                    :key="idx"
                    class="list"
                    style="min-height: 380px"
                    @insert="onInsert($event, Section)"
                    @reorder="$event.apply(Section)"
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
              {{ SelectedVideos }}
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
          <v-card class="mb-12" color="grey lighten-1" height="200px">
            {{ UserVideos }}
            {{ SelectedVideos }}
          </v-card>

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

<script>
import { Vue, Component } from "vue-property-decorator";
import { Drag, DropList } from "vue-easy-dnd";

@Component({
  components: {
    Drag,
    DropList
  }
})
export default class CreateLecture extends Vue {
  UserVideos = ["1", "2", "3", "4", "5","6"];
  SelectedVideos = [["1"], []];
  CreateLectureStep = 1;
  LectureCategories = [];
  LectureDifficulty = "";

  onInsert(event, Section) {
    console.log(event);
    Section.splice(event.index, 0, event.data);
    this.UserVideos = this.UserVideos.filter(item => item !== event.data);
  }

  addSection() {
    this.SelectedVideos.push([]);
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
.classdesc {
  width: 45vw;
}

.wrapper {
  .list {
    border: 1px solid black;
    margin: 10px auto;
    overflow-y: scroll;
    .item {
      padding: 20px;
      margin: 10px;
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
