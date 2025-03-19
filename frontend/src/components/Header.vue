<template>
  <header>
    <nav class="navbar navbar-light">
      <div class="container">
        <a class="navbar-brand" href="/">
          <img src="@/assets/logotip.png" width="45" height="45" alt="Логотип" class="logo">
          <span class="brand-name">Bloghub</span>
        </a>
        <ul class="nav nav-pills">
          <li class="nav-item">
            <router-link class="nav-link" to="/about">О проекте</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/rules">Правила</router-link>
          </li>
          <div class="btn-group" role="group">
            <template v-if="isAuthenticated">
              <button type="button" class="btn btn-outline-light">
                <router-link class="text-decoration-none text-reset" to="/create-post">Написать пост</router-link>
              </button>
              <button type="button" class="btn btn-outline-light">
                <router-link class="text-decoration-none text-reset" to="/profile">{{ username }}</router-link>
              </button>
              <button type="button" class="btn btn-outline-light" @click="logout">
                Выйти
              </button>
            </template>
            <template v-else>
              <button type="button" class="btn btn-outline-light">
                <router-link class="text-decoration-none text-reset" to="/login">Войти</router-link>
              </button>
              <button type="button" class="btn btn-outline-light">
                <router-link class="text-decoration-none text-reset" to="/register">Регистрация</router-link>
              </button>
            </template>
          </div>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: "HeaderComponent",
  data() {
    return {
      isAuthenticated: false,
      username: "Пользователь"
    };
  },
  methods: {
    logout() {
      this.isAuthenticated = false;
      alert("Вы вышли из аккаунта");
    }
  }
};
</script>

<style scoped>
.navbar {
  background-color: #A025DD;
  padding: 0.5rem 1rem; 
  margin-bottom: 15px;
}

.navbar-brand {
  display: flex;
  align-items: center;
}

.logo {
  width: 45px;
  height: 45px;
  margin-right: 8px; 
}

.brand-name {
  color: white;
  font-size: 1.1rem;
  font-weight: 550;
  margin-top: 6px;
}

.text-reset {
  font-size: 1rem; 
  font-weight: 500;
}

.nav-link,
.btn {
  color: #FFFFFF !important;
  font-size: 1rem;
}

.btn-outline-light {
  border-color: #FFFFFF;
  color: #FFFFFF;
  padding: 0.3rem 0.8rem;
  font-size: 1rem;
}

.btn-outline-light:hover {
  background-color: #702197;
  color: #A025DD;
  border-color: #A025DD;
}
</style>
