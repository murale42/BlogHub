import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import AboutPage from '../components/AboutPage.vue';
import RulesPage from '../components/RulesPage.vue';
import LoginPage from '../components/LoginPage.vue';
import RegistrationForm from '../components/RegistrationForm.vue';
import PasswordResetForm from "../components/PasswordResetForm.vue";
import PasswordResetDone from "../components/PasswordResetDone.vue";
import LogoutPage from '../components/LogoutPage.vue';

const routes = [
  { path: '/', name: 'HomePage', component: HomePage },
  { path: '/about', name: 'AboutPage', component: AboutPage },
  { path: '/rules', name: 'RulesPage', component: RulesPage },
  { path: '/login', name: 'LoginPage', component: LoginPage },
  { path: '/register', name: 'RegistrationForm', component: RegistrationForm },
  { path: "/password-reset", name: "PasswordResetForm", component: PasswordResetForm },
  { path: "/password-reset-done", name: "PasswordResetDone", component: PasswordResetDone },
  { path: '/logout', component: LogoutPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
