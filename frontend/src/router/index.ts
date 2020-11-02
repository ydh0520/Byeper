import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import Home from "../views/Home.vue";
import HelloWorld from "@/components/HelloWorld.vue";

// lecturer
import InstructorDashboard from "@/views/lecturer/InstructorDashboard.vue";
import CreateLecture from "@/views/lecturer/CreateLecture.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    name: "Home",
    component: HelloWorld
  },
  {
    path: "/instructor",
    name: "InstructorDashboard",
    component: InstructorDashboard
  },
  {
    path: "/instructor/CreateLecture",
    name: "CreateLecture",
    component: CreateLecture
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
