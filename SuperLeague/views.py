from django.shortcuts import render
from random import shuffle, choice
from .models import *
from rest_framework import generics
from .serializers import *
from django.http import JsonResponse

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

#Функция формирования турнирной сетки
def tour():
    Tour.objects.all().delete()
    matches = []
    clubs = []
    for ell in Club.objects.all():
        clubs.append(ell.id)
    for i in clubs:
        clubs_copy = clubs.copy()
        clubs_copy.remove(i)
        for j in clubs_copy:
            one_match = [i,j]
            matches.append(one_match)
    shuffle(matches)
    for k in matches:
        Tour.objects.create(home=Club.objects.get(pk=k[0]), away=Club.objects.get(pk=k[1]))

def game():
    shot = [i for i in range(1, 7)]
    matches = []
    matches_one_tour = []
    for ell in Tour.objects.filter(is_done=False):
        matches.append(ell.id)
    for i in range(10):
        matches_one_tour.append(matches[i])
    for k in matches_one_tour:
        h = 12
        a = 11
        goal_h = 0
        goal_a = 0
        for _ in range(1, h):
            shot_home = choice(shot)
            if shot_home == 1:
                goal_h += 1
        for _ in range(1, a):
            shot_away = choice(shot)
            if shot_away == 1:
                goal_a += 1
        Tour.objects.filter(id=k).update(goal_home = goal_h, goal_away = goal_a, is_done = True)

def cr_table ():
    Turnament_table.objects.all().delete()
    for ell in Club.objects.all():
        Turnament_table.objects.create(clubs=Club.objects.get(pk=ell.id))

def upd_table():
    for j in Turnament_table.objects.all():
        match = 0
        d_g = 0
        point = 0
        for i in Tour.objects.filter(is_done=True).all():
            if j.clubs_id == i.home_id:
                match += 1
                d_g += i.goal_home
                d_g -= i.goal_away
                if i.goal_home > i.goal_away:
                    point +=3
                elif i.goal_home == i.goal_away:
                    point +=1
            if j.clubs_id == i.away_id:
                match += 1
                d_g -= i.goal_home
                d_g += i.goal_away
                if i.goal_home < i.goal_away:
                    point += 3
                elif i.goal_home == i.goal_away:
                    point += 1
        Turnament_table.objects.filter(id=j.id).update(matches=match,goal_difference=d_g,points=point)
