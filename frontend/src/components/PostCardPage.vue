<template>
  <div class="col d-flex justify-content-center mb-4">
    <div class="card" style="width: 40rem;">
      <div class="card-body">

        
        <h5 class="card-title text-start">{{ post.title || 'Без названия' }}</h5>

        
        <p v-if="post.is_published === false" class="text-danger text-start">
          Пост снят с публикации админом
        </p>

        
        <p class="card-subtitle mb-2 text-muted text-start" style="font-size: 0.85rem;">
          {{ formattedDate }}<br>
          От автора @{{ post.author.username }} в категории {{ post.category }}
        </p>

       
        <p class="card-text text-start">
          {{ post.content ? post.content.slice(0, 150) + '...' : '' }}
        </p>

       
        <div class="d-flex">
          <router-link :to="'/post/' + post.id" class="card-link text-start">
            Читать полный текст
          </router-link>

         
          <router-link :to="'/post/' + post.id + '/comments'" class="text-muted ms-2">
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
      if (!this.post.pub_date) return '';
      const date = new Date(this.post.pub_date);
      return date.toLocaleString('ru-RU', {
        day: 'numeric',
        month: 'long',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      }).replace(',', ''); 
    }
  }
};
</script>
