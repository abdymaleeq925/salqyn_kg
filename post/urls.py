from django.urls import path
from .views import index, get_post_list, get_post_detail

urlpatterns = [
    path('', index, name="index"),
    path('blog/posts/', get_post_list, name="post_list"),
    path('blog/post/<int:pk>/', get_post_detail, name="post_detail"),
]