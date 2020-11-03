<template>
  <div>
    <v-app-bar color="white" style="position: fixed; z-index: 100">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-col cols="3">
        <v-toolbar-title>VideoSummary</v-toolbar-title>
      </v-col>
      <v-col cols="6">
        <v-text-field
          style="margin-top: 30px"
          outlined
          dense
          label="검색"
          prepend-inner-icon="mdi-magnify"
          v-model="inputText"
        >
        </v-text-field>
      </v-col>
      <v-col cols="1.5"></v-col>
      <v-col cols="1">
        <v-btn> <v-icon>mdi-account</v-icon>로그인 </v-btn>
      </v-col>
    </v-app-bar>

    <v-navigation-drawer app v-model="drawer" style="margin-top: 64px;">
      <v-list nav dense>
        <v-list-item-group
          v-model="group"
          active-class="deep-gray--text text--accent-4"
        >
          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>홈</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-book-open-page-variant</v-icon>
            </v-list-item-icon>
            <v-list-item-title>학습 관리</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-fire</v-icon>
            </v-list-item-icon>
            <v-list-item-title>인기</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-play-box-multiple</v-icon>
            </v-list-item-icon>
            <v-list-item-title>구독</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class AppNavbar extends Vue {
  drawer = true;
  group = null;
  inputText = null;
}
</script>

<style scoped></style>
