from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_view, name='blog_view'),
    path('<int:sl_no>/', views.blogPost, name='blogPost'),
]
