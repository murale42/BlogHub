<template>
  <div class="p-3">
    <h5 class="mb-3">Комментарии</h5>

    <div v-if="userAuthenticated">
      <form @submit.prevent="submitComment">
        <div class="mb-2">
          <textarea v-model="newComment" class="form-control" rows="3" placeholder="Оставьте комментарий..."></textarea>
        </div>
        <button type="submit" class="btn btn-primary btn-sm">Отправить</button>
      </form>
    </div>
    <div v-else class="text-muted">Войдите, чтобы оставить комментарий.</div>

    <hr />

    <div v-for="comment in comments" :key="comment.id" class="mb-3">
      <h6>
        <a :href="'/profile/' + comment.author">@{{ comment.author }}</a>
        <small class="text-muted ms-2">{{ comment.date }}</small>
      </h6>
      <p>{{ comment.text }}</p>
      <div v-if="comment.author === currentUser" class="text-muted small">
        <a href="#" class="me-2">Редактировать</a>
        <a href="#">Удалить</a>
      </div>
      <hr />
    </div>
  </div>
</template>

<script>
export default {
  props: {
    postId: Number
  },
  data() {
    return {
      userAuthenticated: true, // пока фиктивно
      currentUser: "eliza", // заменишь позже на из auth
      newComment: "",
      comments: [
        {
          id: 1,
          author: "eliza",
          date: "7 апреля 2025",
          text: "Очень интересный пост!"
        },
        {
          id: 2,
          author: "alex",
          date: "6 апреля 2025",
          text: "Спасибо за информацию!"
        }
      ]
    };
  },
  methods: {
    submitComment() {
      if (this.newComment.trim() === "") return;

      this.comments.unshift({
        id: Date.now(),
        author: this.currentUser,
        date: new Date().toLocaleDateString("ru-RU"),
        text: this.newComment
      });

      this.newComment = "";
    }
  }
};
</script>

<style scoped>
textarea.form-control {
  font-size: 0.9rem;
}
a {
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}
</style>
