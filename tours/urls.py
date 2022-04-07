from django.urls import path
from tours import views

urlpatterns = [
    path('', views.get_tour_list, name="tour_list"),

]