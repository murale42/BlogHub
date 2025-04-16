<template>
  <div class="p-3">
    <h5 class="mb-3">Оставить комментарий</h5>

    <div v-if="userAuthenticated">
      <form @submit.prevent="submitComment">
        <div class="mb-2">
          <textarea
            v-model="newComment"
            class="form-control"
            rows="3"
            placeholder="Текст комментария"
          ></textarea>
        </div>
        <button type="submit" class="btn btn-purple btn-sm">Отправить</button>
      </form>
    </div>
    <div v-else class="text-muted">Войдите, чтобы оставить комментарий.</div>

    <hr />

    <div v-if="comments.length">
      <div v-for="comment in comments" :key="comment.id" class="mb-3">
        <h6>
          <a :href="'/profile/' + comment.author">@{{ comment.author }}</a>
          <small class="text-muted ms-2">{{ comment.date }}</small>
        </h6>
        <p>{{ comment.text }}</p>

        <div v-if="comment.author === currentUser" class="text-muted small">
          <a href="#" class="me-2" @click.prevent="editComment(comment.id)">Редактировать</a>
          <a href="#" @click.prevent="deleteComment(comment.id)">Удалить</a>
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
    this.fetchCommentsIfNeeded();
  },
  watch: {
    postId(newId) {
      if (newId) {
        this.fetchComments();
      }
    }
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

    fetchCommentsIfNeeded() {
      if (this.postId) {
        this.fetchComments();
      } else {
        console.error('postId is not available');
      }
    },

    async fetchComments() {
      if (!this.postId) {
        console.error("postId is not available");
        return;
      }

      try {
        console.log(`Запрос комментариев для поста с ID: ${this.postId}`);
        const response = await fetch(`http://localhost:8000/api/posts/${this.postId}/comments/`);
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
        alert('Не удалось загрузить комментарии');
      }
    },

    async submitComment() {
      if (this.newComment.trim() === "") return;

      try {
        const token = localStorage.getItem("authToken");
        const response = await fetch(`http://localhost:8000/api/posts/${this.postId}/comments/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${token}`
          },
          body: JSON.stringify({
            content: this.newComment,
            post: this.postId
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
        alert('Не удалось отправить комментарий');
      }
    },

    async deleteComment(commentId) {
      const token = localStorage.getItem("authToken");
      try {
        const response = await fetch(`http://localhost:8000/api/comments/${commentId}/`, {
          method: "DELETE",
          headers: {
            Authorization: `Token ${token}`
          }
        });

        if (!response.ok) throw new Error("Ошибка при удалении комментария");

        this.comments = this.comments.filter(comment => comment.id !== commentId);
      } catch (error) {
        console.error("Ошибка при удалении комментария:", error);
        alert('Не удалось удалить комментарий');
      }
    },

    async editComment(commentId) {
      console.log("Редактировать комментарий с ID:", commentId);
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

.btn-purple {
  background-color: #6a1b9a;
  color: white;
}

.btn-purple:hover {
  background-color: #9c4dcc;
}
</style>
