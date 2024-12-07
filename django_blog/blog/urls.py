from django.urls import path
from . import views
from .views import feedback

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/<int:post_id>/', views.post_detail, name='post-detail'),  
    path('register/', views.register, name='register'),  
    path('profile/', views.profile, name='profile'),  
    path('categories/', views.category_list, name='category-list'),
    path('create/', views.create_post, name='create-post'),
    path('settings/', views.settings, name='settings'),
    path('newsletter-subscribe/', views.newsletter_subscribe, name='newsletter-subscribe'),
    path('feedback/', feedback, name='feedback'),
]
