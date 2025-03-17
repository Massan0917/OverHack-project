import { createRouter, createWebHistory } from 'vue-router';
import CreatePost from './components/CreatePost.vue';
import ViewPost from './components/ViewPost.vue';

const routes = [
  { path: '/', component: CreatePost },
  { path: '/view', component: ViewPost }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;

