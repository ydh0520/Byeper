<template>
  <div class="full-height">
    <div>
      <intro-main />
    </div>
    <v-divider
      class="light"
      style="font-weight: bold; margin-top: 30px; "
    ></v-divider>

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
