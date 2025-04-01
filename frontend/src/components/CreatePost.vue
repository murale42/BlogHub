// index.js
import { createApp } from 'vue';
import PostForm from './PostForm.vue';

const app = createApp(PostForm);
app.mount('#app');

// PostForm.vue
<template>
  <div class="col d-flex justify-content-center">
    <div class="card" style="width: 40rem;">
      <div class="card-header">
        {{ pageTitle }}
      </div>
      <div class="card-body">
        <form @submit.prevent="handleSubmit" enctype="multipart/form-data">
          <div v-if="!isDelete">
            <div class="form-check mb-2">
              <input type="checkbox" v-model="form.is_published" class="form-check-input" id="publishCheckbox" />
              <label class="form-check-label" for="publishCheckbox">Опубликовать</label>
            </div>
            <input type="text" v-model="form.title" placeholder="Заголовок" class="form-control mb-2" />
            <textarea v-model="form.text" placeholder="Текст" class="form-control mb-2"></textarea>
            <label class="form-label">Дата и время публикации</label>
            <input type="datetime-local" v-model="form.pub_date" class="form-control mb-2" />
            <label class="form-label">Местоположение</label>
            <input type="text" v-model="form.location.name" placeholder="Местоположение" class="form-control mb-2" />
            <label class="form-label">Категория</label>
            <select v-model="form.category" class="form-select mb-2">
              <option value="Новости">Новости</option>
              <option value="Спорт">Спорт</option>
              <option value="Культура">Культура</option>
            </select>
            <label class="form-label">Фото</label>
            <input type="file" @change="handleFileUpload" class="form-control mb-2" />
          </div>
          <div v-else>
            <article>
              <img v-if="form.image" :src="form.image" class="border-3 rounded img-fluid img-thumbnail mb-2" />
              <p>{{ formattedDate }} | {{ locationName }} | {{ form.category }}</p>
              <h3>{{ form.title }}</h3>
              <p>{{ form.text }}</p>
            </article>
          </div>
          <button type="submit" class="btn btn-primary">Отправить</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        title: '',
        text: '',
        image: null,
        pub_date: new Date().toISOString().slice(0, 16),
        location: { name: 'Планета Земля', is_published: true },
        category: '',
        is_published: false
      },
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
      return this.form.location && this.form.location.is_published ? this.form.location.name : 'Планета Земля';
    },
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.form.image = URL.createObjectURL(file);
      }
    },
    handleSubmit() {
      console.log('Форма отправлена', this.form);
    },
  },
};
</script>

<style>
.card {
  margin-top: 20px;
}
</style>
