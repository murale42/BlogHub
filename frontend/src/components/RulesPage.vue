<template>
  <div class="wrapper">
    <HeaderComponent />
    <div class="form-container">
      <div class="card narrow-card">
        <div class="card-header">
          Правила сайта
        </div>
        <div class="card-body">
          <p>
            <b>Самовыражение.</b> У наших пользователей должна
            быть возможность создать что-то своё, выразить себя,
            свои мысли и чувства.
          </p>
          <p>
            <b>Многообразие.</b> Мы уважаем и приветствуем разные
            мнения и культуры. Блогикум — это место, объединяющее
            самых разных людей. Поделитесь своим уникальным взглядом на мир.
          </p>
          <p>
            <b>Творчество.</b> Не важно, в какой области вы творите,
            это может быть литература, дизайн, программирование.
            Наши инструменты помогут вам раскрыть талант максимально
            просто и комфортно.
          </p>
          <p>
            <b>Личность.</b> Мы сохраним ваши сокровенные мысли в тайне.
            Делитесь своей информацией только с теми, кого выбрали.
            Как и насколько засекречивать вашу личную информацию —
            определяете вы и только вы.
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
  max-width: 30rem;
  margin-bottom: 20px;
}

.narrow-card {
  max-width: 32rem;
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
</style>
