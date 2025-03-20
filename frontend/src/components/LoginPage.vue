<template>
  <div>
    <HeaderComponent />
    <div class="d-flex justify-content-center align-items-center vh-100">
      <div class="card">
        <div class="card-header text-center">
          Войти в систему
        </div>
        <div class="card-body">
          <p v-if="errorMessage" class="text-danger text-center">{{ errorMessage }}</p>
          <form @submit.prevent="login">
            <div class="mb-2">
              <label for="username" class="form-label">Логин</label>
              <input type="text" id="username" v-model="form.username" class="form-control" required />
            </div>
            <div class="mb-2">
              <label for="password" class="form-label">Пароль</label>
              <input type="password" id="password" v-model="form.password" class="form-control" required />
            </div>
            <input type="hidden" v-model="form.next">
            <button type="submit" class="btn btn-login w-100">Войти</button>
          </form>
          <div class="text-center mt-3">
            <router-link to="/password-reset">Забыли пароль?</router-link>
          </div>
        </div>
      </div>
    </div>
    <FooterComponent />
  </div>
</template>

<script>
import axios from 'axios';
import HeaderComponent from './Header.vue';
import FooterComponent from './Footer.vue';

export default {
  components: {
    HeaderComponent,
    FooterComponent
  },
  data() {
    return {
      form: {
        username: '',
        password: '',
        next: this.$route.query.next || '', // Передача "next" из URL
      },
      errorMessage: '',
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('/api/auth/login/', this.form, { withCredentials: true });
        if (response.data.success) {
          this.$router.push(this.form.next || '/');
        } else {
          this.errorMessage = 'Неправильные учетные данные';
        }
      } catch (error) {
        this.errorMessage = 'Ошибка входа. Проверьте логин и пароль.';
      }
    },
  },
};
</script>

<style scoped>
.card {
  margin-top: 0.5rem;
  width: 100%;
  max-width: 40rem;
  margin-bottom: 0.5rem;
}

.card-header {
  font-size: 1rem;
  font-weight: 600;
  padding: 0.75rem;
}

.card-body {
  padding: 0.75rem;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.form-control {
  border-radius: 0.25rem;
  border-color: #ddd;
  font-size: 0.8rem;
  padding: 0.25rem 0.5rem;
  height: 1.8rem;
}

.btn-login {
  background-color: #A025DD;
  border-color: #A025DD;
  color: #fff;
  font-size: 0.8rem;
  padding: 0.3rem 0.8rem;
}

.btn-login:hover {
  background-color: #702197;
  border-color: #702197;
  color: #fff;
}

.form-label {
  font-weight: 500;
  font-size: 0.8rem;
}

.d-flex {
  display: flex;
}

.justify-content-center {
  justify-content: center;
}

.align-items-center {
  align-items: center;
}

.vh-100 {
  height: 100vh;
}
</style>
