from django.shortcuts import render
from .models import Tour
# Create your views here.


def get_tour_list(request):
    tours = Tour.objects.filter(is_active=True)
    context = {
        "tours": tours
    }
    return render(request, 'tour_list.html', context=context)
