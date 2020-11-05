<template>
  <div>
    <div class="banner">
      <div class="videoBx">
        <video
          src="@/assets/mainVideo.mp4"
          muted
          autoplay
          loop
          type="mp4"
        ></video>
      </div>

      <div class="textBox">
        <h2>{{ playList.playListName }}</h2>
        <p>{{ playList.playListDescription }}</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class IntroMain extends Vue {
  playList = {
    playListName: this.$route.params.playListName,
    playListDescription:
      "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Obcaecatieum voluptate est eius, voluptatibus earum ipsum asperiores modi odit numquam alias. Reiciendis saepe ex, eius animi maxime non debitis! Recusandae!"
  };
}
</script>

<style scoped>
.banner {
  position: relative;
  width: 100%;
  padding: 0 100px;
  display: flex;
  min-height: 500px;
  justify-content: flex-start;
  align-items: center;
}
.banner:before {
  content: "";
  position: absolute;
  right: 0;
  top: 0;
  width: 400px;
  height: 100%;
  /* background: rgba(0, 0, 0, 0.5); */
}

.banner video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.1;
  pointer-events: none;
}

.banner .textBox {
  position: relative;
  max-width: 550px;
  z-index: 2;
}
.banner .textBox:before {
  content: "";
  position: absolute;
  background: #121212;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  transform-origin: right;
  animation: revealText 2s ease-in-out forwards;
}
@keyframes revealText {
  0% {
    transform: scaleX(1);
  }
  100% {
    transform: scaleX(0);
  }
}
.banner .textBox h2 {
  font-size: 3em;
}

.banner .textBox p {
  font-size: 1.1em;
  margin: 5px 0 25px;
}

.banner .textBox a {
  position: relative;
  display: inline-block;
  background: #fff;
  color: #111;
  padding: 15px 25px;
  text-decoration: none;
  font-size: 1.1em;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 500;
}
.banner .videoBx {
  position: relative;
  background: #fff;
  margin-right: 80px;
  width: 500px;
  height: 300px;
  z-index: 1;
}

.banner .videoBx video {
  opacity: 1;
}
</style>
