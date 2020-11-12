import { Module } from "vuex";
import { RootState } from "./index";
import { LecturesModule } from "./Lectures.interface";
import { Axios } from "@/service/axios.service";

const module: Module<LecturesModule, RootState> = {
  namespaced: true,
  state: {
    lectures: [],
    allCaptureImgs: [],
    courses: []
  },

  getters: {},

  mutations: {
    SET_ALL_CAPTURE_IMAGES(state, imgs) {
      state.allCaptureImgs = imgs;
    },
    SET_COURSE_BY_STUDENT(state, courses) {
      state.courses = courses;
    }
  },

  actions: {
    FETCH_CAPTURE_IMAGE(_, { id, time }) {
      return Axios.instanceDjango
        .post("/api/django/summary/extract_time/", { id, time })
        .then(({ data }) => data)
        .catch(err => console.error(err));
    },
    FETCH_ALL_CAPTURE_IMAGES({ commit }, videoId) {
      // Axios.instanceDjango
      //   .get(`/file/${videoId}/${videoId}.json`)
      //   .then(res => console.log(res))
      //   .catch(err => console.error(err));
      const xhr = new XMLHttpRequest();
      xhr.addEventListener("load", function() {
        commit("SET_ALL_CAPTURE_IMAGES", JSON.parse(this.responseText));
      });
      xhr.open(
        "GET",
        `http://k3b108.p.ssafy.io/file/${videoId}/${videoId}.json`
      );
      xhr.send();
    },
    FETCH_COURSE_BY_STUDENT({ commit }) {
      Axios.instance
        .get("/api/public/playlist/user")
        .then(({ data }) => commit("SET_COURSE_BY_STUDENT", data.data))
        .catch(err => console.error(err));
    }
  }
};

export default module;
