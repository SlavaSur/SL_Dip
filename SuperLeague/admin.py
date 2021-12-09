from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Club)
class ClubAdmin (admin.ModelAdmin):
    list_display = ('id','club_name','coutry','rating')

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('home','goal_home','goal_away', 'away', 'is_done')

@admin.register(Turnament_table)
class Turnament_tableAdmin(admin.ModelAdmin):
     list_display = ('clubs','matches','goal_difference', 'points')
