<template>
  <div v-if="PlayList">
    <div class="banner">
      <v-row>
        <v-col cols="2">
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

        <v-col cols="5" justify="center" align="center">
          <div class="textBox">
            <h2>{{ PlayList.playlistTitle }}</h2>
            <p>{{ PlayList.playlistDescription }}</p>
          </div>
        </v-col>
        <v-col cols="5">
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
                    v-for="(video, video_index) in PlayListVideos"
                    :key="video.video_id"
                    @click="moveScroll(video.video_id)"
                  >
                    <td class="text-center" style="cursor: pointer;">
                      {{ video_index + 1 }}
                    </td>
                    <td style="cursor: pointer">{{ video.video_title }}</td>
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

  headers = [
    {
      text: "커리큘럼",
      align: "start",
      value: "playName",
      groupable: false
    }
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
