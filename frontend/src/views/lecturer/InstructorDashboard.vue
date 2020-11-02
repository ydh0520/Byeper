<template>
  <div>
    <v-row style="margin: 10px 10%" cols="12" sm="6" offset-sm="3">

      <vue-slick-carousel
          v-if="Lectures"
          class="slick"
          v-bind="settings"
      >
        <div v-for="lecture in Lectures" :key="lecture.LectureId">
          <router-link
              class="router-link"
              :to="{ name: 'DetailArtView', params: { LectureId : lecture.LectureId } }"
          >
            <img
                class="Lecture-img"
                :src="lecture.LectureThumb"
                :alt="lecture.LectureName"
            />
          </router-link>
        </div>
      </vue-slick-carousel>

    </v-row>

  </div>
</template>

<script>
import { Vue, Component } from "vue-property-decorator";
import {namespace} from "vuex-class";
// carousel 관련 import
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";

const InstructorModule = namespace("InstructorModule");

@Component({
  components: {
    VueSlickCarousel
  }
})
export default class InstructorDashboard extends Vue {
  data() {
    return {
      Lectures: [
        {
          LectureName: "파이썬 좋아",
          LectureId: "1",
          LectureThumb: "https://images.unsplash.com/photo-1502224562085-639556652f33?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80",
          LectureDesc: "파이썬 12만원 타세요",
        },
        {
          LectureName: "파이썬 좋아",
          LectureId: "2",
          LectureThumb: "https://images.unsplash.com/photo-1502224562085-639556652f33?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80",
          LectureDesc: "파이썬 12만원 타세요",
        },
        {
          LectureName: "파이썬 좋아",
          LectureId: "3",
          LectureThumb: "https://images.unsplash.com/photo-1502224562085-639556652f33?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80",
          LectureDesc: "파이썬 12만원 타세요",
        },
        {
          LectureName: "파이썬 좋아",
          LectureId: "4",
          LectureThumb: "https://images.unsplash.com/photo-1502224562085-639556652f33?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80",
          LectureDesc: "파이썬 12만원 타세요",
        },
        {
          LectureName: "파이썬 좋아",
          LectureId: "5",
          LectureThumb: "https://images.unsplash.com/photo-1502224562085-639556652f33?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80",
          LectureDesc: "파이썬 12만원 타세요",
        },
        {
          LectureName: "파이썬 좋아",
          LectureId: "6",
          LectureThumb: "https://images.unsplash.com/photo-1502224562085-639556652f33?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80",
          LectureDesc: "파이썬 12만원 타세요",
        },
      ],
      settings:  {
        arrows: true,
        dots: false,
        infinite: true,
        slidesToShow: 5,
        slidesToScroll: 1,
        autoplay: true,
        speed: 2000,
        autoplaySpeed: 3000,
        responsive: [
          {
            breakpoint: 1399,
            settings: {
              slidesToShow: 4
            }
          },
          {
            breakpoint: 1099,
            settings: {
              slidesToShow: 3
            }
          },
          {
            breakpoint: 799,
            settings: {
              slidesToShow: 2
            }
          },
          {
            breakpoint: 499,
            settings: {
              slidesToShow: 2
            }
          }
        ]
      }


    }
  }

}
</script>


<style scoped>
.slick {
  width: 100%;
  height: 165px;
}
.Lecture-img {
  margin: 5px;
  width: 94%;
  height: 165px;
  transition: all ease 1ms;
}

.Lecture-img:hover {
  cursor: pointer;
  box-shadow: 0px 0px 10px 5px;
  transform: scale(1.1);
}

.router-link {
  text-decoration: none;
  color: inherit;
  border: 0;
  outline: none;
}

</style>
