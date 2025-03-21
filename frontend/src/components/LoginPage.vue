<template>
  <div class="wrapper">
    <HeaderComponent />
    <div class="form-container">
      <div class="card">
        <div class="card-header text-center">
          Войти в систему
        </div>
        <div class="card-body">
          <p v-if="errorMessage" class="text-danger text-center">{{ errorMessage }}</p>
          <form @submit.prevent="login">
            <div class="mb-2">
              <label for="username" class="form-label">Имя пользователя</label>
              <input 
                type="text" 
                id="username" 
                v-model="form.username" 
                class="form-control" 
                placeholder="Имя пользователя" 
                required 
              />
            </div>
            <div class="mb-2">
              <label for="password" class="form-label">Пароль</label>
              <input 
                type="password" 
                id="password" 
                v-model="form.password" 
                class="form-control" 
                placeholder="Пароль" 
                required 
              />
            </div>
            <input type="hidden" v-model="form.next" />
            
            <div class="d-flex justify-content-start">
              <button type="submit" class="btn btn-login btn-sm">Войти</button>
            </div>
            
            <div class="mt-2 text-left">
              <router-link to="/password-reset" class="text-decoration-none">Забыли пароль?</router-link>
            </div>
          </form>
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
        next: this.$route.query.next || '',
      },
      errorMessage: '',
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('/api/auth/login/', this.form, { withCredentials: true });
        
        if (response.data.success) {
          localStorage.setItem('authToken', response.data.token);
          localStorage.setItem('username', this.form.username);
          
          this.$router.push(this.form.next || '/');
        } else {
          this.errorMessage = 'Неправильные учетные данные';
        }
      } catch (error) {
        this.errorMessage = 'Ошибка входа. Проверьте имя пользователя и пароль.';
      }
    },
  },
};
</script>

<style scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.form-container {
  display: flex;
  justify-content: center;
  flex: 1;
  align-items: flex-start;
  padding-top: 30px;
}

.card {
  width: 100%;
  max-width: 40rem;
  margin-bottom: 20px;
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

.text-left {
  text-align: left;
  font-size: 0.8rem;
}

.mt-2 {
  margin-top: 0.5rem;
}

.btn-sm {
  font-size: 0.8rem;
  padding: 0.4rem 1rem;
  width: auto;
}

footer {
  margin-top: auto;
}
</style>
