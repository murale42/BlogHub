<template>
  <div class="wrapper">
    <HeaderComponent />

    <main>
      <div class="container py-5">
        <div v-if="posts.length">
          <PostCard
            v-for="post in posts"
            :key="post.id"
            :post="post"
          />
        </div>
        <div v-else>
          <p>Пока нет публикаций.</p>
        </div>
      </div>
    </main>

    <FooterComponent />
  </div>
</template>

<script>
import axios from 'axios';
import HeaderComponent from './Header.vue';
import FooterComponent from './Footer.vue';
import PostCard from './PostCardPage.vue';

export default {
  components: {
    HeaderComponent,
    FooterComponent,
    PostCard
  },
  data() {
    return {
      posts: []
    };
  },
  created() {
    this.fetchPosts();
  },
  methods: {
    async fetchPosts() {
      try {
        const response = await axios.get('http://localhost:8000/api/posts/');

        this.posts = response.data;
      } catch (error) {
        console.error('Ошибка при загрузке постов:', error);
      }
    }
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
  align-items: flex-start;
}

.container {
  text-align: center;
  width: 100%;
}

footer {
  margin-top: auto;
}
</style>
