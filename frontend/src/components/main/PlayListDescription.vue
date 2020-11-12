<template>
  <div v-if="PlayList">
    <div class="banner">
      <v-row>
        <v-col cols="3">
          <div class="videoBx">
            <video
              src="@/assets/mainVideo.mp4"
              muted
              autoplay
              loop
              type="mp4"
            ></video>
          </div>
        </v-col>

        <v-col cols="6" justify="center" align="center">
          <div class="textBox">
            <h2>{{ PlayList.playlistTitle }}</h2>
            <p>{{ PlayList.playlistDescription }}</p>
          </div>
        </v-col>
        <v-col cols="3">
          <div class="tableBox">
            <v-simple-table dense max-height="400px" width="400px">
              <template v-slot:default>
                <thead>
                  <tr>
                    <th class="text-left">
                      재생번호
                    </th>
                    <th class="text-left">
                      제목
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="item in play"
                    :key="item.id"
                    @click="moveScroll(item.id)"
                  >
                    <td class="text-center" style="cursor: pointer;">
                      {{ item.id }}
                    </td>
                    <td style="cursor: pointer">{{ item.playName }}</td>
                  </tr>
                </tbody>
              </template>
            </v-simple-table>
          </div>
        </v-col>
      </v-row>
    </div>
    <v-btn class="mx-2" fab dark color="indigo" @click="buyPlayList">
      <v-icon dark>
        mdi-plus
      </v-icon>
    </v-btn>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Watch } from "vue-property-decorator";
import { namespace } from "vuex-class";
import { PlayList } from "../../store/PlayList.interface";

const PlayListModule = namespace("PlayListModule");
const AccountsModule = namespace("AccountsModule");

@Component
export default class PlayListDescription extends Vue {
  @PlayListModule.State PlayList!: PlayList;
  @PlayListModule.State PlayListVideos!: [];
  @PlayListModule.Action FETCH_PLAYLIST_VIDEOS: any;
  @PlayListModule.Action FETCH_PLAYLIST: any;
  @PlayListModule.Action BUY_PLAYLIST: any;
  @AccountsModule.Getter isLoggedIn!: boolean;
  @AccountsModule.Action GOOGLE_LOGIN: any;

  $vuetify: any;
  $gAuth: any;

  playList = {
    playListName: "슬기로운 싸피 생활",
    playListDescription:
      "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Obcaecatieum voluptate est eius, voluptatibus earum ipsum asperiores modi odit numquam alias. Reiciendis saepe ex, eius animi maxime non debitis! Recusandae!"
  };
  headers = [
    {
      text: "커리큘럼",
      align: "start",
      value: "playName",
      groupable: false
    }
  ];

  play = [
    { id: 1, playName: "머신러닝" },
    { id: 2, playName: "인공지능 개론" },
    { id: 3, playName: "인공신경망 최적화" },
    { id: 4, playName: "IOT 접목하기" },
    { id: 5, playName: "텐서플로우와 코드" },
    { id: 6, playName: "KERAS와 코드" },
    { id: 7, playName: "CNN과 RNN" }
  ];

  @Watch("$route", { immediate: true })
  fetchPlayList() {
    this.FETCH_PLAYLIST({ playlistId: Number(this.$route.params.playListId) });
  }

  @Watch("$route", { immediate: true })
  fetchPlayListVideos() {
    this.FETCH_PLAYLIST_VIDEOS({
      playlistId: Number(this.$route.params.playListId)
    });
  }

  moveScroll(scrollId: string) {
    const target: HTMLElement = document.getElementById(
      scrollId
    ) as HTMLElement;
    const scrollLocation: number = target.offsetTop;
    this.$vuetify.goTo(scrollLocation + 500);
  }

  buyPlayList() {
    if (this.isLoggedIn) {
      this.BUY_PLAYLIST({
        playlistId: Number(this.$route.params.playListId)
      });
    } else {
      if (
        confirm("로그인이 필요합니다.\n구글 로그인을 하시겠습니까??") === true
      ) {
        this.$gAuth
          .getAuthCode()
          .then((authToken: string) => this.GOOGLE_LOGIN(authToken));
      }
    }
  }
}
</script>

<style scoped>
.banner {
  position: relative;
  width: 100%;
  display: flex;
  min-height: 500px;
  justify-content: center;
  align-items: center;
  padding: 0 50px 0 50px;
}

.banner video {
  position: relative;
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
  max-width: 500px;
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

.tableBox {
  opacity: 0;
  animation: fadeInBottom 0.5s linear forwards;
  animation-delay: 1.5s;
}
@keyframes fadeInBottom {
  0% {
    transform: translateY(20px);
    opacity: 0;
  }
  100% {
    transform: translateY();
    opacity: 1;
  }
}
.banner .textBox h2 {
  font-size: 3em;
}

.banner .textBox p {
  font-size: 1.1em;
  margin: 5px 0 0 0;
}

.banner .videoBx {
  position: relative;
  margin-top: 30px;
  display: inline;
  width: 300px;
  height: 200px;
  z-index: 1;
}

.banner .videoBx video {
  opacity: 1;
}
</style>
