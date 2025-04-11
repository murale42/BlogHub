<template>
  <div>
    <HeaderComponent />
    <div class="d-flex justify-content-center">
      <div class="card">
        <div class="card-header">
          {{ pageTitle }}
        </div>
        <div class="card-body">
          <form @submit.prevent="handleSubmit" enctype="multipart/form-data">
            <div v-if="!isDelete">
              <label class="form-label">Заголовок</label>
              <input type="text" v-model="form.title" class="form-control mb-2" />

              <label class="form-label">Текст</label>
              <textarea v-model="form.text" class="form-control mb-2"></textarea>

              <label class="form-label">Дата и время публикации</label>
              <input type="datetime-local" v-model="form.pub_date" class="form-control mb-2" />

              <label class="form-label">Категория</label>
              <select v-model="form.category" class="form-select mb-2">
                <option v-for="category in categories" :key="category.id" :value="category.id">
                  {{ category.name }}
                </option>
              </select>

              <label class="form-label">Фото</label>
              <input
                type="file"
                @change="handleFileUpload"
                class="form-control mb-2"
                ref="imageInput"
              />
            </div>

            <div v-else>
              <article>
                <img
                  v-if="form.image"
                  :src="form.image"
                  class="border-3 rounded img-fluid img-thumbnail mb-2"
                />
                <p>{{ formattedDate }} | {{ locationName }} | {{ form.category }}</p>
                <h3>{{ form.title }}</h3>
                <p>{{ form.text }}</p>
              </article>
            </div>

            <button type="submit" class="btn btn-create">Отправить</button>
          </form>
        </div>
      </div>
    </div>
    <FooterComponent />
  </div>
</template>

<script>
import axios from 'axios';
import HeaderComponent from './Header.vue';
import FooterComponent from './Footer.vue';

export default {
  components: {
    HeaderComponent,
    FooterComponent,
  },
  data() {
    return {
      form: {
        title: '',
        text: '',
        image: null,
        pub_date: new Date().toISOString().slice(0, 16),
        category: [], 
        location: { name: 'Планета Земля', is_published: true },
      },
      categories: [],  
      isDelete: window.location.pathname.includes('/delete/'),
    };
  },
  computed: {
    pageTitle() {
      if (window.location.pathname.includes('/edit/')) return 'Редактирование публикации';
      if (window.location.pathname.includes('/delete/')) return 'Удаление публикации';
      return 'Добавление публикации';
    },
    formattedDate() {
      return new Date(this.form.pub_date).toLocaleDateString('ru-RU', {
        day: '2-digit',
        month: 'long',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
      });
    },
    locationName() {
      return this.form.location && this.form.location.is_published
        ? this.form.location.name
        : 'Планета Земля';
    },
  },
  mounted() {
    this.fetchCategories();  
  },
  methods: {
    async fetchCategories() {
      try {
        const response = await axios.get('http://localhost:8000/api/categories/');
        this.categories = response.data;  
      } catch (error) {
        console.error('Ошибка при загрузке категорий:', error);
      }
    },
    handleFileUpload(event) {
      this.form.image = event.target.files[0];
    },
    async handleSubmit() {
      const formData = new FormData();
      formData.append('title', this.form.title);
      formData.append('content', this.form.text);
      formData.append('pub_date', this.form.pub_date);
      formData.append('categories', this.form.category);  

      if (this.form.image) {
        formData.append('image', this.form.image);
      }

      
      const token = localStorage.getItem('authToken'); 

      if (!token) {
        console.error('Токен не найден!');
        alert('Ошибка: не найден токен! Пожалуйста, авторизуйтесь снова.');
        return; 
      }

      try {
        
        await axios.post('http://localhost:8000/api/posts/', formData, {
          headers: {
            'Authorization': `Token ${token}`,
            'Content-Type': 'multipart/form-data',
          },
        });

        
        this.$router.push('/');
        this.$root.$emit('fetch-posts'); 

      } catch (error) {
       
        console.error('Ошибка при отправке поста:', error);
        if (error.response && error.response.status === 401) {
          console.error('Неверный токен или отсутствует авторизация');
        }
      }
    }
  },
};
</script>

<style scoped>
.card {
  margin-top: 0.5rem;
  width: 100%;
  max-width: 40rem;
  margin-bottom: 0.5rem;
}

.card-header {
  font-size: 1rem;
  font-weight: 600;
  padding: 0.75rem;
}

.card-body {
  padding: 0.75rem;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.form-control {
  border-radius: 0.25rem;
  border-color: #ddd;
  font-size: 0.8rem;
  padding: 0.25rem 0.5rem;
  height: 1.8rem;
}

.btn-create {
  background-color: #a025dd;
  border-color: #a025dd;
  color: #fff;
  font-size: 0.8rem;
  padding: 0.3rem 0.8rem;
}

.btn-create:hover {
  background-color: #702197;
  border-color: #702197;
  color: #fff;
}

.form-label {
  font-weight: 500;
  font-size: 0.8rem;
}

.text-muted {
  font-size: 0.8rem;
  color: #888;
}
</style>
