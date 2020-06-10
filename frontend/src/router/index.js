import Vue from 'vue';
import VueRouter from 'vue-router';
import Uploader from '../components/Uploader.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'ESP32 Firmware Uploader',
    component: Uploader,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
