from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_view, name='blog_view'),
    path('<int:sl_no>/', views.blogPost, name='blogPost'),
    path('<int:sl_no>/user_comment/', views.user_comment, name='user_comment'),
    path('create_post/', views.create_post, name='create_post'),
    path('manage_post/', views.manage_post, name='manage_post'),
    path('<int:sl_no>/delete_post/', views.delete_post, name='delete_post'),
]
