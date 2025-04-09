from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="customuser_groups")
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions")

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Заголовок')
    slug = models.SlugField(unique=True,
                            verbose_name='Идентификатор',
                            help_text='Идентификатор страницы для URL;'
                                      ' разрешены символы латиницы, цифры,'
                                      ' дефис и подчёркивание.')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(verbose_name='Текст')  
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='posts', verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор публикации')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = RichTextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Комментарий от {self.author.username} к "{self.post.title}"'
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')