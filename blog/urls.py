from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/<int:pk>', views.post_show, name='post.show'),
    path('posts/listar', views.post_list, name='post.list'),
    path('posts/crear', views.post_create, name='post.create'),

]
