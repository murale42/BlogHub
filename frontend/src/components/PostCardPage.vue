<!-- src/components/PostCard.vue -->
<template>
  <div class="col d-flex justify-content-center">
    <div class="card" style="width: 40rem;">
      <div class="card-body">
        <a href="#" target="_blank">
          <img class="border-3 rounded img-fluid img-thumbnail mb-2 mx-auto d-block" src="https://via.placeholder.com/600" />
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
