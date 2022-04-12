from django.urls import path
from tours import views

urlpatterns = [
    path('', views.get_tour_list, name="tour_list"),
    path('tour/<int:pk>/', views.get_tour_detail, name="tour_detail")
]