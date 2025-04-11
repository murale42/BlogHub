<template>
  <div class="p-3">
    <h5 class="mb-3">Комментарии</h5>

   
    <div v-if="userAuthenticated">
      <form @submit.prevent="submitComment">
        <div class="mb-2">
          <textarea
            v-model="newComment"
            class="form-control"
            rows="3"
            placeholder="Оставьте комментарий..."
          ></textarea>
        </div>
        <button type="submit" class="btn btn-primary btn-sm">Отправить</button>
      </form>
    </div>
    <div v-else class="text-muted">Войдите, чтобы оставить комментарий.</div>

    <hr />

   
    <div v-if="comments.length">
      <div
        v-for="comment in comments"
        :key="comment.id"
        class="mb-3"
      >
        <h6>
          <a :href="'/profile/' + comment.author">@{{ comment.author }}</a>
          <small class="text-muted ms-2">{{ comment.date }}</small>
        </h6>
        <p>{{ comment.text }}</p>

        <div
          v-if="comment.author === currentUser"
          class="text-muted small"
        >
          <a href="#" class="me-2">Редактировать</a>
          <a href="#">Удалить</a>
        </div>
        <hr />
      </div>
    </div>
    <div v-else class="text-muted">Комментариев пока нет.</div>
  </div>
</template>

<script>
export default {
  props: {
    postId: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      userAuthenticated: false,
      currentUser: null,
      newComment: "",
      comments: []
    };
  },
  mounted() {
    this.checkAuth();
    this.fetchComments();
  },
  methods: {
    
    checkAuth() {
      const token = localStorage.getItem("authToken");
      const username = localStorage.getItem("username"); 

      if (token && username) {
        this.userAuthenticated = true;
        this.currentUser = username;
      }
    },

   
    async fetchComments() {
      try {
        const response = await fetch(`/api/posts/${this.postId}/comments/`);
        if (!response.ok) throw new Error("Ошибка при загрузке комментариев");

        const data = await response.json();
        this.comments = data.map(comment => ({
          id: comment.id,
          author: comment.author,
          text: comment.content,
          date: new Date(comment.created_at).toLocaleDateString("ru-RU")
        }));
      } catch (error) {
        console.error("Ошибка загрузки комментариев:", error);
      }
    },

  
    async submitComment() {
      if (this.newComment.trim() === "") return;

      try {
        const token = localStorage.getItem("authToken");

        const response = await fetch(`/api/posts/${this.postId}/comments/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${token}`
          },
          body: JSON.stringify({
            content: this.newComment
          })
        });

        if (!response.ok) throw new Error("Ошибка при отправке комментария");

        const createdComment = await response.json();

        this.comments.unshift({
          id: createdComment.id,
          author: createdComment.author,
          text: createdComment.content,
          date: new Date(createdComment.created_at).toLocaleDateString("ru-RU")
        });

        this.newComment = "";
      } catch (error) {
        console.error("Ошибка при добавлении комментария:", error);
      }
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
