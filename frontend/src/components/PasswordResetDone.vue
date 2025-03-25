<template>
  <div class="wrapper">
    <HeaderComponent />
    <div class="form-container">
      <div class="card">
        <div class="card-header text-center">
          Письмо с инструкциями по восстановлению пароля отправлено
        </div>
        <div class="card-body">
          <p class="text-center">
            Мы отправили вам инструкцию по установке нового пароля
            на указанный адрес электронной почты (если в нашей базе данных есть такой адрес).
            Вы должны получить ее в ближайшее время.
          </p>
          <p class="text-center">
            Если вы не получили письмо, пожалуйста,
            убедитесь, что вы ввели адрес, с которым зарегистрировались,
            и проверьте папку со спамом.
          </p>
          <p class="text-center">
            <router-link to="/">На главную</router-link>
          </p>
        </div>
      </div>
    </div>
    <FooterComponent />
  </div>
</template>

<script>
import HeaderComponent from "./Header.vue";
import FooterComponent from "./Footer.vue";

export default {
  components: {
    HeaderComponent,
    FooterComponent,
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

.text-center {
  text-align: center;
  font-size: 0.9rem;
}

footer {
  margin-top: auto;
}
</style>
