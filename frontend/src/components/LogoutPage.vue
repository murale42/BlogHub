<template>
  <div class="wrapper">
    <HeaderComponent />
    <div class="form-container">
      <div class="card narrow-card">
        <div class="card-header">
          Вы вышли из системы!
        </div>
        <div class="card-body">
          <p><router-link to="/login">Войти снова</router-link></p>
          <p><router-link to="/">На главную</router-link></p>
        </div>
      </div>
    </div>
    <FooterComponent />
  </div>
</template>

<script>
import HeaderComponent from './Header.vue';
import FooterComponent from './Footer.vue';

export default {
  components: {
    HeaderComponent,
    FooterComponent
  },
  mounted() {
    localStorage.removeItem('authToken');
    localStorage.removeItem('username');
  }
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
  text-align: left;
}
.narrow-card {
  max-width: 40rem;
}
.card-header {
  font-size: 1rem;
  font-weight: 600;
  padding: 0.75rem;
  text-align: left;
}

.card-body {
  padding: 0.75rem;
  text-align: left;
}
</style>
