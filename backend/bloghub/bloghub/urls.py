from blog.forms import UserCreateForm
from django.conf import settings
from django.conf.urls.static import static

from blog.views import RegisterView
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from rest_framework.authtoken.views import obtain_auth_token
from blog.views import RegisterView, LoginView
from blog.views import ProtectedView
from django.urls import path
from blog.views import PasswordResetRequestView, PasswordResetConfirmView
from blog.views import ChangePasswordView
from blog.views import PostListCreateView, PostDetailView, CategoryDetailView, CategoryListView
from blog.views import PostsByCategoryView, PostsByAuthorView


def home(request):
    return HttpResponse("Добро пожаловать в BlogHub!")
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),  # Добавляем маршрут для "/"
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token-auth/', obtain_auth_token, name='token-auth'), 
    path("api/protected/", ProtectedView.as_view(), name="protected"),
    path('login/', LoginView.as_view(), name='login'),
    path('api/password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('api/password-reset/confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('api/posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('api/categories/', CategoryListView.as_view(), name='category-list'),
    path('api/categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('posts/category/<slug:slug>/', PostsByCategoryView.as_view(), name='posts-by-category'),
    path('posts/author/<str:username>/', PostsByAuthorView.as_view(), name='posts-by-author'),
    path('api/authors/<str:username>/', AuthorDetailView.as_view(), name='author-detail'),
]

# Подключение маршрутов для медиа-файлов
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)