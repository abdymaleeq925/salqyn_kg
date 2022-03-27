from django.urls import path
from .views import index, get_post_list

urlpatterns = [
    path('', index, name="index"),
    path('blog/posts/', get_post_list, name="post_list"),
]