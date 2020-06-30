import Vue from 'vue';
import VueRouter from 'vue-router';
import Uploader from '../components/Uploader.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'ESP32 Firmware Uploader',
    component: Uploader,
    meta: {
      title: 'ESP32 Firmware Uploader',
    },
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  next();
});

export default router;
