<template>
  <div class="home full-height">
    <v-row class="full-height">
      <v-row align="start" justify="center">
        <div>
          <div
            style="font-family: 'Black Han Sans', sans-serif; font-size:40px; margin-bottom: 50px;"
          >
            <div>
              <vue-odometer :value="myValue"></vue-odometer>
            </div>
          </div>
        </div>
      </v-row>
    </v-row>
  </div>
</template>

<script>
import { Component, Vue } from "vue-property-decorator";
import VueOdometer from "v-odometer/src";

@Component({
  components: {
    "vue-odometer": VueOdometer
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
