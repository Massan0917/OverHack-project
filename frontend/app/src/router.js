import { createRouter, createWebHistory } from 'vue-router';
import CreatePost from './components/CreatePost.vue';
import ViewPost from './components/ViewPost.vue';
import Carousel from './components/Carousel.vue';

const routes = [
  { path: '/', component: CreatePost },
  { path: '/view', component: Carousel }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;

