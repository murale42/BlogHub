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
                :maxlength="field.maxLength"
                :placeholder="field.placeholder"
              />
              <div v-if="field.hint" class="form-hint" v-html="field.hint"></div>
            </div>
            <button type="submit" class="btn btn-create">Зарегистрироваться</button>
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
        username: {
          label: "Имя пользователя", 
          value: "", 
          type: "text", 
          required: true,
          maxLength: 30,
          placeholder: "Имя пользователя*",
          hint: `*Обязательное поле.<br>Не более 30 символов.<br>Только буквы, цифры и символы @/./+/-/_.`
        },
        first_name: { label: "Имя", value: "", type: "text", required: true, placeholder: "Имя" },
        last_name: { label: "Фамилия", value: "", type: "text", required: true, placeholder: "Фамилия" },
        email: { label: "Адрес электронной почты", value: "", type: "email", required: true, placeholder: "Адрес электронной почты" },
        password: {
          label: "Пароль", 
          value: "", 
          type: "password", 
          required: true,
          placeholder: "Пароль",
          hint: `<ul class='password-hint'>
                   <li class="spisok">Пароль не должен быть слишком похож на другую вашу личную информацию.</li>
                   <li class="spisok">Ваш пароль должен содержать как минимум 8 символов.</li>
                   <li class="spisok">Пароль не должен быть слишком простым и распространенным.</li>
                   <li class="spisok">Пароль не может состоять только из цифр.</li>
                 </ul>`
        },
        password2: {
          label: "Подтверждение пароля", 
          value: "", 
          type: "password", 
          required: true,
          placeholder: "Подтверждение пароля",
          hint: "Для подтверждения введите, пожалуйста, пароль еще раз."
        }
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

.spisok {
  margin-bottom: 0.15rem; 
  font-size: 0.75rem; 
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
  text-transform: uppercase; 
}

.card-header {
  text-transform: none; 
}

.btn-create {
  text-transform: none; 
}

.form-hint {
  font-size: 0.75rem;
  color: #6c757d;
  margin-top: 0.25rem;
  white-space: pre-line;
  line-height: 1.4; 
}

.password-hint {
  padding-left: 0.75rem;
  margin: 0;
  list-style-type: disc;
  line-height: 1.4; 
}

.password-hint li {
  margin-bottom: 0.15rem; 
  font-size: 0.75rem; 
}

.text-danger {
  color: red;
}

.d-flex {
  display: flex;
}

.justify-content-center {
  justify-content: center;
}
</style>
