import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import AboutPage from '../components/AboutPage.vue';
import RulesPage from '../components/RulesPage.vue';
import LoginPage from '../components/LoginPage.vue';
import RegistrationForm from '../components/RegistrationForm.vue';
import PasswordResetForm from "../components/PasswordResetForm.vue";
import PasswordResetDone from "../components/PasswordResetDone.vue";
import LogoutPage from '../components/LogoutPage.vue';
import PostCardPage from '../components/PostCardPage.vue';
import CreatePost from '../components/CreatePost.vue';
import PostDetail from '../components/PostDetail.vue';
import PostComments from '../components/PostComments.vue';
const routes = [
  { path: '/', name: 'HomePage', component: HomePage },
  { path: '/about', name: 'AboutPage', component: AboutPage },
  { path: '/rules', name: 'RulesPage', component: RulesPage },
  { path: '/login', name: 'LoginPage', component: LoginPage },
  { path: '/register', name: 'RegistrationForm', component: RegistrationForm },
  { path: "/password-reset", name: "PasswordResetForm", component: PasswordResetForm },
  { path: "/password-reset-done", name: "PasswordResetDone", component: PasswordResetDone },
  { path: '/logout', component: LogoutPage },
  { path: '/postcard', component: PostCardPage },
  { path: '/create-post', component: CreatePost },
  {path: '/post/:id', name: 'PostDetail', component: PostDetail, props: true},
  { path: '/post/:id/comments', name: 'PostComments', component: PostComments, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
