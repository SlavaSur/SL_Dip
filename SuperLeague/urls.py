from django.urls import path
from . import views
from .views import ListClub, ListTours #DetailClub, DetailTours

urlpatterns = [
    path('api/clubs/',ListClub.as_view()),
    path('api/tours/',ListTours.as_view()),
    path('api/turs/generate/', views.generate),
    path('api/turs/gamegen/', views.gamegen),
    path('', views.gs, name='home'),
    path('tours/', views.tours, name='tours'),
    path('tables/', views.table,name='tables'),
    path('one_tour/', views.one_tour,name='one_tour'),

]
