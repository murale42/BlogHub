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
        </h6>
        <small class="text-muted">{{ comment.date }}</small>

        <div v-if="editingCommentId === comment.id">
          <textarea
            v-model="editedCommentText"
            class="form-control mb-2"
            rows="3"
          ></textarea>
          <button class="btn btn-sm btn-purple me-2" @click="saveEditedComment(comment.id)">
            Сохранить
          </button>

          <button class="btn btn-sm btn-secondary" @click="cancelEditing">
            Отмена
          </button>
        </div>

        <p v-else>{{ comment.text }}</p>

        <div v-if="comment.author === currentUser" class="text-muted small">
          <a href="#" class="me-2" @click.prevent="startEditing(comment)">Отредактировать комментарий</a>
          <a href="#" @click.prevent="deleteComment(comment.id)">Удалить комментарий</a>
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
      comments: [],
      editingCommentId: null,
      editedCommentText: ""
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
        console.error("postId is not available");
      }
    },

    formatDate(datetime) {
      const date = new Date(datetime);
      const optionsDate = { day: 'numeric', month: 'long', year: 'numeric' };
      const optionsTime = { hour: '2-digit', minute: '2-digit' };

      const formattedDate = new Intl.DateTimeFormat('ru-RU', optionsDate).format(date).replace(' г.', '');
      const formattedTime = new Intl.DateTimeFormat('ru-RU', optionsTime).format(date);

      return `${formattedDate}, ${formattedTime}`;
    },

    async fetchComments() {
      if (!this.postId) {
        console.error("postId is not available");
        return;
      }

      try {
        const response = await fetch(`http://localhost:8000/api/posts/${this.postId}/comments/`);
        if (!response.ok) throw new Error("Ошибка при загрузке комментариев");

        const data = await response.json();
        this.comments = data.map(comment => ({
          id: comment.id,
          author: comment.author,
          text: comment.content,
          date: this.formatDate(comment.created_at)
        }));
      } catch (error) {
        console.error("Ошибка загрузки комментариев:", error);
        alert("Не удалось загрузить комментарии");
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
          date: this.formatDate(createdComment.created_at)
        });

        this.newComment = "";
      } catch (error) {
        console.error("Ошибка при добавлении комментария:", error);
        alert("Не удалось отправить комментарий");
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
        alert("Не удалось удалить комментарий");
      }
    },

    startEditing(comment) {
      this.editingCommentId = comment.id;
      this.editedCommentText = comment.text;
    },

    cancelEditing() {
      this.editingCommentId = null;
      this.editedCommentText = "";
    },

    async saveEditedComment(commentId) {
  const token = localStorage.getItem("authToken");

  try {
    const response = await fetch(`http://localhost:8000/api/comments/${commentId}/`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`
      },
      body: JSON.stringify({
        content: this.editedCommentText,
        post: this.postId 
      })
    });

    const responseBody = await response.text();
    if (!response.ok) {
      console.error("Ответ сервера:", responseBody);
      throw new Error("Ошибка при редактировании комментария");
    }

    const updatedComment = JSON.parse(responseBody);

    const index = this.comments.findIndex(c => c.id === commentId);
    if (index !== -1) {
      this.comments[index].text = updatedComment.content;
    }

    this.cancelEditing();
  } catch (error) {
    console.error("Ошибка при редактировании комментария:", error);
    alert("Не удалось отредактировать комментарий");
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
  color: inherit;
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

.text-muted a {
  color: #6c757d;
}

.text-muted a:hover {
  color: #5a6268;
}

h6 > a {
  color: #0d6efd;
  font-weight: 500;
}

h6 > a:hover {
  color: #0a58ca;
}
</style>
