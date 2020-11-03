<template>
  <div class="full-height">
    <intro-main />
    <v-divider
      class="light"
      style="font-weight: bold; margin-top: 30px; "
    ></v-divider>
    <div
      style="font-family: 'Black Han Sans', sans-serif; font-size:40px; margin-bottom: 50px;"
    >
      <div style="font-size: 25px; margin-right:30px;">
        <vue-odometer :value="myValue"></vue-odometer>
      </div>
    </div>
    <all-play-list />
  </div>
</template>

<script>
import { Component, Vue } from "vue-property-decorator";
import VueOdometer from "v-odometer/src";
import AllPlayList from "@/components/main/AllPlayList.vue";
import IntroMain from "@/components/main/IntroMain.vue";

@Component({
  components: {
    "vue-odometer": VueOdometer,
    AllPlayList,
    IntroMain
  }
})
export default class Home extends Vue {
  myValue = 0;
  mounted() {
    this.myValue = 170;
  }
}
</script>

<style scoped>
.full-height {
  height: 100%;
  margin: 0px;
  padding: 0px;
}
</style>
