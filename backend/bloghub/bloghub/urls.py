from blog.forms import UserCreateForm
from django.conf import settings
from django.conf.urls.static import static

from blog.views import RegisterView
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Добро пожаловать в BlogHub!")
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),  # Добавляем маршрут для "/"
    path('api/register/', RegisterView.as_view(), name='register'),
]