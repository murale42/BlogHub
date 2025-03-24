<template>
  <div class="wrapper">
    <HeaderComponent />
    
    <main>
      <div class="container py-5">
        <!-- Пока нет контента на главной странице -->
      </div>
    </main>

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
  }
};
</script>

<style scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  text-align: center;
  width: 100%;
}

footer {
  margin-top: auto;
}
</style>
