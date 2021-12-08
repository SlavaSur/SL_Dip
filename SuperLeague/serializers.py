from rest_framework import serializers
from .models import *

class ClubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ('id', 'club_name', 'coutry','rating',)

class ToursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ('home', 'goal_home', 'goal_away','away',)