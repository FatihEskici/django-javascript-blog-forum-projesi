from django.contrib import admin
from django.urls import path, include
from blog import views  # blog/views modülünü içe aktarıyoruz
from blog.views import CustomLoginView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin paneli için
    path('blog/', include('blog.urls')),  # Blog URL'leri
    path('', include('blog.urls')),  # Ana sayfa yönlendirmesi
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='blog-home'), name='logout'),
]

