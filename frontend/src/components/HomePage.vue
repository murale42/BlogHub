<template>
  <div class="wrapper">
    <HeaderComponent />

    <main>
      <div class="container py-5">
        <transition-group name="fade" tag="div">
          <PostCard
            v-for="post in posts"
            :key="post.id"
            :post="post"
            @remove-post="removePostFromList"
          />
        </transition-group>

        <div v-if="!posts.length" class="mt-4">
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
    },
    removePostFromList(postId) {
      this.posts = this.posts.filter(p => p.id !== postId);
    }
  }
};
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: all 0.5s ease;
}
.fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}

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
