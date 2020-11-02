<template>
  <div>
    <v-app-bar color="white">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-col cols="3">
        <v-toolbar-title>VideoSummary</v-toolbar-title>
      </v-col>
      <v-col cols="6">
        <v-text-field
          style="margin-top: 30px"
          solo
          placeholder="검색"
          clearable
          prepend-inner-icon="mdi-magnify"
          v-model="inputText"
          color="white"
        >
        </v-text-field>
      </v-col>
    </v-app-bar>

    <v-navigation-drawer
      app
      clipped
      permanent
      v-if="drawer"
      style="height: 100vh; margin-top: 64px"
    >
      <v-list nav dense>
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>홈</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>계정</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-fire</v-icon>
            </v-list-item-icon>
            <v-list-item-title>인기</v-list-item-title>
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
  drawer = false;
  group = null;
}
</script>

<style></style>
