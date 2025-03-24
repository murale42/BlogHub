<template>
  <div class="wrapper">
    <HeaderComponent />
    <div class="form-container">
      <div class="card">
        <div class="card-header text-left">
          Отправить письмо для сброса пароля
        </div>
        <div class="card-body">
          <p v-if="errorMessage" class="text-danger text-left">{{ errorMessage }}</p>
          <form @submit.prevent="submitForm">
            <div class="mb-2">
              <label for="email" class="form-label">Адрес электронной почты</label>
              <input
                type="email"
                id="email"
                v-model="email"
                class="form-control"
                placeholder="Адрес электронной почты"
                required
              />
            </div>

            <div class="d-flex justify-content-start">
              <button type="submit" class="btn btn-submit btn-sm">Отправить письмо</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <FooterComponent />
  </div>
</template>

<script>
import axios from "axios";
import HeaderComponent from './Header.vue';
import FooterComponent from './Footer.vue';

export default {
  components: {
    HeaderComponent,
    FooterComponent
  },
  data() {
    return {
      email: "",
      errorMessage: "",
    };
  },
  methods: {
    async submitForm() {
      try {
        await axios.post("/api/password-reset/", { email: this.email });
        this.$router.push("/password-reset-done");
      } catch (error) {
        this.errorMessage = "Ошибка при отправке формы. Попробуйте снова.";
        console.error("Ошибка при отправке формы:", error);
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
  text-align: left;
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
  text-align: left;
}

.btn-submit {
  background-color: #A025DD;
  border-color: #A025DD;
  color: #fff;
  font-size: 1.2rem;
  padding: 0.6rem 1.2rem;
}

.btn-submit:hover {
  background-color: #702197;
  border-color: #702197;
  color: #fff;
}

.form-label {
  font-weight: 500;
  font-size: 0.8rem;
  text-align: left;
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
