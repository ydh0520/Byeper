<template>
  <div class="playlistvideos">
    <div class="container">
      <div
        class="card"
        v-for="item in list"
        :key="item.id"
        @mouseover="isHover = !isHover"
      >
        <div class="imgBx" :data-text="item.playListName">
          <img class="bigimg" src="@/assets/jun.png" />
          <img class="smallimg" src="@/assets/playBtn.png" @click="goHome" />
        </div>
        <div class="content" @click="goHome">
          <div style="color: black">
            <h3>
              쿠팡개발자 김씨의 하루
            </h3>
            <p style="font-weight: light; ">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Alias
              quis consequuntur magni accusantium similique corporis dolores
              voluptatum ipsum distinctio maiores. Voluptas ullam ratione
              nostrum non maiores quia molestiae aperiam. Magnam.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class PlayListRoadmap extends Vue {
  isHover = true;
  list = [
    {
      id: 1,
      playListName: "junho"
    },
    {
      id: 2,
      playListName: "junho"
    },
    {
      id: 3,
      playListName: "junho"
    },
    {
      id: 4,
      playListName: "junho"
    },
    {
      id: 5,
      playListName: "junho"
    },
    {
      id: 6,
      playListName: "junho"
    },
    {
      id: 7,
      playListName: "junho"
    },
    {
      id: 8,
      playListName: "junho"
    },
    {
      id: 9,
      playListName: "junho"
    }
  ];
  goHome() {
    this.$router.push({ name: "Home" });
  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Do Hyeon", sans-serif;
}
.playlistvideos {
  display: flex;
  justify-content: center;
  align-items: center;
  background: #222;
  min-height: 100vh;
}
.container {
  position: relative;
  width: 1000px;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  margin: 20px;
}
.container .card {
  position: relative;
  height: 250px;
  background: #fff;
  display: flex;
  width: 45%;
  margin: 30px 0;
}

.container .card .imgBx {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: #333;
  z-index: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  transition: 0.5s ease-in-out;
}
.container .card:hover .imgBx {
  width: 150px;
  height: 150px;
  left: -75px;
  top: calc(50% - 75px);
  transition: 0.5s ease-in-out;
  background: #ff00ff00;
}
.container .card .smallimg {
  display: none;
}
.container .card:hover .smallimg {
  display: block;
  cursor: pointer;
}
.container .card:hover .bigimg {
  display: none;
}
.container .card .imgBx img {
  max-height: 100%;
  transition: 0.5s ease-in-out;
}

.container .card .content {
  position: absolute;
  right: 0;
  width: calc(100% - 75px);
  height: 100%;
  padding: 20px;
  justify-content: center;
  align-items: center;
  overflow: auto;
  cursor: pointer;
}
.container .card .content h3 {
  margin-bottom: 5px;
  font-size: 24px;
}

@media (max-width: 992px) {
  .container {
    width: 100%;
    flex-direction: column;
    align-items: center;
  }
  .container .card {
    width: 400px;
  }
}
@media (max-width: 768px) {
  .container .card {
    max-width: 300px;
    flex-direction: column;
    height: auto;
  }
  .container .card .imgBx {
    position: relative;
  }
  .container .card .imgBx,
  .container .card:hover .imgBx {
    width: 100%;
    height: 200px;
    left: 0;
  }
  .container .card .imgBx img,
  .container .card:hover .imgBx img {
    max-width: 100px;
  }
  .container .card .content {
    position: relative;
    width: 100%;
  }
}
</style>
