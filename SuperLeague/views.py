from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import *
from django.http import JsonResponse
from .defs import *

# Create your views here.

class ListClub(generics.ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubsSerializer

class ListTours(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = ToursSerializer

def generate(request):
    tour()
    cr_table()
    return JsonResponse({})

def gamegen(request):
    game()
    upd_table()
    return JsonResponse({})

def gs(request):
    club = Club.objects.order_by('-rating')
    return render(request, 'SuperLeague/gs.html', {'club': club})

def tours(request):
    tour = Tour.objects.all()
    return render(request, 'SuperLeague/tours.html', {'tour': tour})

def table(request):
    table = Turnament_table.objects.order_by('-points')
    return render(request, 'SuperLeague/table.html', {'table': table})

def one_tour(request):
    one_tour = One_tour.objects.all()
    return render(request, 'SuperLeague/one_tour.html', {'one_tour': one_tour})
