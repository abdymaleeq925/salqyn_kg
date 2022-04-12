from django.shortcuts import render
from django.http import Http404
from .models import Tour
# Create your views here.


def get_tour_list(request):
    tours = Tour.objects.filter(is_active=True)
    context = {
        "tours": tours
    }
    return render(request, 'tour_list.html', context=context)


def get_tour_detail(request, pk):
    try:
        tour = Tour.objects.get(id=pk)
    except Tour.DoesNotExist:
        raise Http404
    context = {
        "tour": tour
    }
    return render(request, 'tour_detail.html', context)
