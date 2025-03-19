<template>
  <div>
    <HeaderComponent />
    <div class="d-flex justify-content-center">
      <div class="card">
        <div class="card-header">
          Регистрация пользователя
        </div>
        <div class="card-body">
          <form @submit.prevent="registerUser">
            <div class="mb-2" v-for="(field, key) in form" :key="key">
              <label :for="key" class="form-label">{{ field.label }}</label>
              <input 
                v-model="field.value" 
                :type="field.type" 
                :id="key" 
                class="form-control"
                required
              />
            </div>
            <button type="submit" class="btn btn-create">Создать</button>
          </form>
        </div>
      </div>
    </div>
    <FooterComponent />
  </div>
</template>

<script>
import api from "../services/api";
import HeaderComponent from "./Header.vue";
import FooterComponent from "./Footer.vue";

export default {
  components: {
    HeaderComponent,
    FooterComponent
  },
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
        await api.post("/register/", formData);
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

.btn-create {
  background-color: #A025DD;
  border-color: #A025DD;
  color: #fff;
  font-size: 0.8rem; 
  padding: 0.3rem 0.8rem; 
}

.btn-create:hover {
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
</style>
