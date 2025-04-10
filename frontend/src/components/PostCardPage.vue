<template>
  <div class="col d-flex justify-content-center mb-4">
    <div class="card" style="width: 40rem;">
      <div class="card-body">
        <a v-if="post.image" :href="post.image || '#'" target="_blank">
          <img
            class="border-3 rounded img-fluid img-thumbnail mb-2 mx-auto d-block"
            :src="post.image || '/default-image.jpg'"
            alt="Изображение поста"
          />
        </a>

        <h5 class="card-title">{{ post.title || 'Без названия' }}</h5>

        <h6 class="card-subtitle mb-2 text-muted">
          <small>
            <p v-if="!post.is_published" class="text-danger">Пост снят с публикации админом</p>
            {{ formattedDate }} | {{ post.location || 'Планета Земля' }}<br>
            От автора <a class="text-muted" href="#">@{{ post.author }}</a> в категории
            <a href="#">{{ post.category }}</a>
          </small>
        </h6>

        <p class="card-text">{{ post.text ? post.text.slice(0, 150) : 'Нет описания' }}...</p>

        <router-link :to="'/post/' + post.id" class="card-link">Читать полный текст</router-link>
        <a href="#" class="card-link text-muted">Комментарии ({{ post.comments_count || 0 }})</a>

        <!-- Кнопка для раскрытия комментариев -->
        <button @click="toggleComments" class="btn btn-link">Показать комментарии</button>
      </div>

      <!-- Комментарии свернуты по умолчанию -->
      <Comments :post-id="post.id" v-if="showComments" />
    </div>
  </div>
</template>

<script>
import Comments from './PostComments.vue';

export default {
  name: 'PostCard',
  components: {
    Comments
  },
  props: {
    post: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      showComments: false
    };
  },
  methods: {
    toggleComments() {
      this.showComments = !this.showComments;
    }
  },
  computed: {
    formattedDate() {
      if (!this.post.pub_date) return 'Дата не указана';
      const date = new Date(this.post.pub_date);
      return date.toLocaleString('ru-RU', {
        day: '2-digit',
        month: 'long',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      });
    }
  }
};
</script>

<style scoped>
.card {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card-body {
  padding: 1rem;
}

.card-title {
  font-size: 1.25rem;
  font-weight: bold;
}

.card-subtitle {
  font-size: 0.9rem;
}

.card-text {
  font-size: 0.95rem;
}
</style>
