<!-- src/components/PostCard.vue -->
<template>
  <div class="col d-flex justify-content-center">
    <div class="card" style="width: 40rem;">
      <div class="card-body">
        <a href="#" target="_blank">
          <!-- <img class="border-3 rounded img-fluid img-thumbnail mb-2 mx-auto d-block" src="https://via.placeholder.com/600" /> -->
        </a>
        <h5 class="card-title">Заголовок поста</h5>
        <h6 class="card-subtitle mb-2 text-muted">
          <small>
            <p class="text-danger">Пост снят с публикации админом</p>
            28 марта 2025, 14:00 | Планета Земля<br>
            От автора <a class="text-muted" href="#">@username</a> в категории <a href="#">Категория</a>
          </small>
        </h6>
        <p class="card-text">Краткое описание поста, отображающееся в превью...</p>
        <a href="#" class="card-link">Читать полный текст</a>
        <a href="#" class="card-link text-muted">Комментарии (5)</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PostCard'
};
</script>

<style scoped>
  .card {
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
  overflow: hidden;
  width: 100%;
  max-width: 40rem;
}

.card:hover {
  transform: translateY(-5px);
}

.card-body {
  padding: 1.5rem;
}

.card-title {
  color: #333;
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.card-subtitle {
  font-size: 0.9rem;
  color: #777;
  margin-bottom: 1rem;
}

.text-danger {
  font-weight: bold;
  color: #d9534f !important;
}

.card-text {
  font-size: 1rem;
  color: #555;
}

.card-link {
  color: #007bff;
  font-weight: 500;
  text-decoration: none;
  transition: color 0.3s;
}

.card-link:hover {
  color: #0056b3;
  text-decoration: underline;
}

.img-thumbnail {
  border-radius: 8px;
  max-width: 100%;
  height: auto;
}

@media (max-width: 768px) {
  .card {
    width: 90%;
  }
}
</style>
