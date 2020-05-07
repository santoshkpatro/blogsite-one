from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogHome, name='blogHome'),
    path('<int:sl_no>/', views.blogPost, name='blogPost'),
    path('blogComment/', views.blogComment, name='blogComment'),
]
