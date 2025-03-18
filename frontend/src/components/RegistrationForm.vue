<template>
  <div class="d-flex justify-content-center">
    <div class="card" style="width: 40rem;">
      <div class="card-header">
        Регистрация пользователя
      </div>
      <div class="card-body">
        <form @submit.prevent="registerUser">
          <div class="mb-3" v-for="(field, key) in form" :key="key">
            <label :for="key" class="form-label">{{ field.label }}</label>
            <input 
              v-model="field.value" 
              :type="field.type" 
              :id="key" 
              class="form-control"
              required
            />
          </div>
          <button type="submit" class="btn btn-primary">Создать</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import api from "../services/api";


export default {
  data() {
    return {
      form: {
        username: { label: "Имя пользователя", value: "", type: "text" },
        email: { label: "Email", value: "", type: "email" },
        first_name: { label: "Имя", value: "", type: "text" },
        last_name: { label: "Фамилия", value: "", type: "text" },
        password: { label: "Пароль", value: "", type: "password" },
        password2: { label: "Повторите пароль", value: "", type: "password" }
      }
    };
  },
  methods: {
    async registerUser() {
      try {
        const formData = Object.fromEntries(
          Object.entries(this.form).map(([key, field]) => [key, field.value])
        );
        // eslint-disable-next-line no-unused-vars
        const response = await api.post("/register/", formData);
        alert("Регистрация успешна");
      } catch (error) {
        console.error("Ошибка регистрации:", error.response?.data || error);
        alert("Ошибка регистрации: " + (error.response?.data || "Неизвестная ошибка"));
      }
    }
  }
};
</script>

<style scoped>
.card {
  margin-top: 2rem;
}
</style>
