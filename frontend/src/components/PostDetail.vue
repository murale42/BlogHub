<template>
  <div class="wrapper">
    <HeaderComponent />

    <div class="content-container d-flex justify-content-center">
      <div class="card post-detail-card">
        <div class="card-body">

          <!-- РЕЖИМ ПРОСМОТРА -->
          <template v-if="mode === 'view'">
            <h5 class="card-title">{{ post.title }}</h5>
            
            <h6 class="card-subtitle mb-2 text-muted" style="margin-top: 20px;">
              <small>
                <span v-if="post.is_published === false" class="text-danger">
                  Пост снят с публикации админом
                </span>
                {{ formattedDate }}<br />
                <span v-if="post.author && post.author.username">
                  От автора <span class="text-muted">@{{ post.author.username }}</span> в категории {{ post.category?.name || 'Без категории' }}
                </span>

                <span v-else>
                  От автора (неизвестный) в категории {{ post.category?.name || 'Без категории' }}
                </span>
              </small>
            </h6>

            <p v-if="post.content" class="card-text" v-html="post.content" style="margin-top: 15px;"></p>
            <p v-else>Текст поста не доступен.</p>

            <img
              v-if="post.image"
              :src="post.image"
              class="border-3 rounded img-fluid img-thumbnail mb-2 mx-auto d-block"
            />

            <div v-if="userIsAuthor" class="mt-3 text-start">
              <span class="text-muted">
                <a href="#" @click.prevent="mode = 'edit'" class="text-decoration-underline">
                  Редактировать текст поста
                </a>
                <span v-if="post.image" class="mx-2"></span>
                <a href="#" @click.prevent="mode = 'confirm-delete'" class="text-decoration-underline">
                  Удалить
                </a>
              </span>
            </div>

            <div class="actions mt-3 d-flex">
              <img src="../assets/heart.png" alt="Like" class="action-icon me-3" />
              <img src="../assets/share.png" alt="Share" class="action-icon" />
            </div>
          </template>
          

          <!-- РЕЖИМ РЕДАКТИРОВАНИЯ -->
          <template v-else-if="mode === 'edit'">
            <form @submit.prevent="submitEdit">
              <input v-model="form.title" class="form-control mb-2" placeholder="Заголовок" />
              <textarea v-model="form.text" class="form-control mb-2" placeholder="Текст"></textarea>
              <button class="btn btn-sm btn-success me-2" type="submit">Сохранить</button>
              <button class="btn btn-sm btn-secondary" @click="cancelEdit">Отмена</button>
            </form>
          </template>

          <!-- ПОДТВЕРЖДЕНИЕ УДАЛЕНИЯ -->
          <template v-else-if="mode === 'confirm-delete'">
            <p>Вы уверены, что хотите удалить пост?</p>
            <button class="btn btn-sm btn-danger me-2" @click="deletePost">Да, удалить</button>
            <button class="btn btn-sm btn-secondary" @click="mode = 'view'">Отмена</button>
          </template>

        </div>
      </div>
    </div>

    <FooterComponent />
  </div>
</template>


<script>
import axios from 'axios';
import { useRouter } from 'vue-router';
import HeaderComponent from './Header.vue';
import FooterComponent from './Footer.vue';

export default {
  name: 'PostDetail',
  components: {
    HeaderComponent,
    FooterComponent
  },
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      post: {},
      form: {
        title: '',
        text: ''
      },
      mode: 'view'
    };
  },
  computed: {
    formattedDate() {
      if (!this.post.created_at) return '';
      const date = new Date(this.post.created_at);

      const dateFormatted = date.toLocaleDateString('ru-RU', {
        day: 'numeric',
        month: 'long',
        year: 'numeric',
      });

      const timeFormatted = date.toLocaleTimeString('ru-RU', {
        hour: '2-digit',
        minute: '2-digit',
        hour12: false
      });

      return `${dateFormatted}, ${timeFormatted}`;
    },
    userIsAuthor() {
      const currentUser = localStorage.getItem('username');
      return currentUser && currentUser === this.post.author?.username;
    }
  },
  created() {
    this.fetchPost();
  },
  methods: {
    async fetchPost() {
      const { id } = this;
      const token = localStorage.getItem('authToken');
      try {
        const response = await axios.get(`http://localhost:8000/api/posts/${id}/`, {
          headers: {
            Authorization: `Token ${token}`
          }
        });
        this.post = response.data;
        this.form.title = this.post.title;
        this.form.text = this.post.content;
      } catch (error) {
        console.error('Ошибка при загрузке поста', error);
      }
    },
    async submitEdit() {
      const token = localStorage.getItem('authToken');
      try {
        await axios.put(`http://localhost:8000/api/posts/${this.post.id}/`, {
          title: this.form.title,
          content: this.form.text
        }, {
          headers: {
            Authorization: `Token ${token}`
          }
        });
        this.mode = 'view';
        this.fetchPost();
      } catch (error) {
        console.error('Ошибка при редактировании', error);
      }
    },
    cancelEdit() {
      this.form.title = this.post.title;
      this.form.text = this.post.content;
      this.mode = 'view';
    },
    async deletePost() {
      const router = useRouter();
      const token = localStorage.getItem('authToken');
      try {
        await axios.delete(`http://localhost:8000/api/posts/${this.post.id}/`, {
          headers: {
            Authorization: `Token ${token}`
          }
        });
        router.push('/');
      } catch (error) {
        console.error('Ошибка при удалении', error);
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

.content-container {
  flex: 1;
  padding-top: 20px;
  align-items: flex-start;
}

.post-detail-card {
  width: 100%;
  max-width: 800px;
  margin-bottom: 1rem;
  height: auto;
}

.post-detail-card .card-body {
  padding: 20px;
  display: flex;
  flex-direction: column;
  height: auto;
}

.post-detail-card .card-body p:last-child {
  margin-bottom: 0;
}

.card-subtitle {
  margin-top: 20px;
}

.card-text {
  margin-top: 15px;
}

form textarea {
  min-height: 50px;
  resize: vertical;
}

.actions {
  display: flex;
  justify-content: start;
  
}

.action-icon {
  width: 30px;
  height: 30px;
  cursor: pointer;
}
</style>

