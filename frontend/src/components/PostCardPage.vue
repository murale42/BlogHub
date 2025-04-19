<template>
  <div class="col d-flex justify-content-center mb-4" v-if="post && post.created_at">
    <div class="card" style="width: 40rem;">
      <div class="card-body">
        <h5 class="card-title text-start">{{ post.title || 'Без названия' }}</h5>

        <p v-if="post.is_published === false" class="text-danger text-start">
          Пост снят с публикации админом
        </p>

        <p class="card-subtitle text-muted text-start" style="font-size: 0.85rem; margin-top: 20px;">
          {{ formattedDate }}<br>
          От автора @{{ post.author.username }} в категории {{ post.category?.name || 'Без категории' }}
        </p>

        <p class="card-text text-start" style="margin-top: 15px;">
          {{ post.content ? post.content.slice(0, 150) + '...' : '' }}
        </p>

        <div class="d-flex">
          <router-link :to="'/post/' + post.id" class="card-link text-start">
            Читать полный текст
          </router-link>

          <router-link :to="'/post/' + post.id" class="text-muted ms-2">
            Комментарии ({{ post.comments_count || 0 }})
          </router-link>
        </div>

      </div>
    </div>
  </div>
</template>



<script>
export default {
  name: 'PostCard',
  props: {
    post: {
      type: Object,
      required: true
    }
  },
  computed: {
    formattedDate() {
      if (!this.post.created_at) return 'Дата не указана';
      
      const date = new Date(this.post.created_at);

      const dateFormatted = date.toLocaleDateString('ru-RU', {
        day: 'numeric',
        month: 'long',
        year: 'numeric',
      });

      const cleanedDate = dateFormatted.replace(' г.', '');

      const timeFormatted = date.toLocaleTimeString('ru-RU', {
        hour: '2-digit',
        minute: '2-digit',
        hour12: false
      });

      return `${cleanedDate}, ${timeFormatted}`;
    }
  },
  mounted() {
    console.log('Post data in mounted:', this.post); 
  }
};

</script>

<style scoped>
.card-subtitle {
  margin-top: 20px; 
}

.card-text {
  margin-top: 15px; 
}
</style>


