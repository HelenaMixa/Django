from django.shortcuts import render
from . models import Club
from . models import Dancer
from . models import Coach
from django.views.generic import TemplateView

def start(request):

    return render(request, 'Dance_Info/index.html')


def club(request):
    show_table = Club.objects.order_by('club_name')
    return render(request, 'Dance_Info/club.html', {'title': 'База данных клубов', 'clubs': show_table})

def dancers(request):
    show_dancers = Dancer.objects.order_by('club')
    return render(request, 'Dance_Info/dancers.html', {'title': 'База данных танцоров', 'dancers': show_dancers})

def coach(request):
    show_coach = Coach.objects.all()
    return render(request, 'Dance_Info/coach.html', {'title': 'База данных тренеров', 'coaches': show_coach})

def about(request):
    return render(request, 'Dance_Info/hello.html')