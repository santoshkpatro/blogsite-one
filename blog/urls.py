from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_view, name='blog_view'),
    path('<int:sl_no>/', views.blogPost, name='blogPost'),
    path('<int:sl_no>/user_comment/', views.user_comment, name='user_comment'),
]
