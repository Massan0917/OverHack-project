import { createRouter, createWebHistory } from 'vue-router';
import CreatePost from './components/CreatePost.vue';
import ViewPost from './components/ViewPost.vue';
import Carousel from './components/Carousel.vue';
import ConfirmPost from './components/ConfirmPost.vue';

const routes = [
  { path: '/', name:'CreatePost', component: CreatePost },
  { path: '/view', component: Carousel },
  { path: '/confirm', 
    name: 'PostConfirm',
    component: ConfirmPost,
    props: route => ({
      image: route.params.image,
      name: route.params.name,
      comment : route.params.comment,
    })
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;

