import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import HelloWorld from "@/components/HelloWorld.vue";
import StudentPage from "@/views/student/StudentPage.vue";
import LectureListPage from "@/views/student/LectureListPage.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    name: "Home",
    component: HelloWorld
  },
  {
    path: "/student",
    name: "StudentPage",
    component: StudentPage
  },
  {
    path: "/course",
    name: "LectureListPage",
    component: LectureListPage
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
