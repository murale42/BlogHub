<template>
  <div class="wrapper">
    <HeaderComponent />
    <div class="form-container">
      <div class="card narrow-card">
        <div class="card-header">
          О проекте
        </div>
        <div class="card-body">
          <p>
            BlogHub — это дом для творческих людей. Это — сообщество людей, для которых
            нет грани между ведением блога и дружбой в социальных сетях.
          </p>
          <p>
            Дружба и рассказы о новых, неизведанных впечатлениях — вот
            что вы найдете на нашем ресурсе. Миллионы блогов по различным темам.
            Путешествия, политика, развлечения, мода, литература, дизайн и все
            другие сферы человеческой деятельности.
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

.narrow-card {
  max-width: 30rem;
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
  max-width: 33rem;
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
</style>