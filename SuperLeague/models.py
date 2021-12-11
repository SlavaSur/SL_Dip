from django.db import models

# Create your models here.

class Club(models.Model):
    club_name = models.CharField (max_length=50)
    coutry = models.CharField (max_length=3)
    rating = models.IntegerField ()

    def query(self):
        return {id: self.id, name: self.club_name}

    class Meta:
        ordering = ["id"]

class Tour(models.Model):
    home = models.ForeignKey(Club, on_delete= models.CASCADE, related_name='club_game_hom')
    goal_home = models.IntegerField(default=0)
    goal_away = models.IntegerField(default=0)
    away = models.ForeignKey(Club, on_delete= models.CASCADE, related_name='club_game_away')
    is_done = models.BooleanField(default=False)

class Turnament_table(models.Model):
    clubs = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='clubs_id')
    matches = models.IntegerField(default=0)
    goal_difference = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

class One_tour(models.Model):
    home = models.ForeignKey(Tour, on_delete=models.CASCADE,related_name='club_tour_h')
    goal_home = models.IntegerField(default=0)
    goal_away = models.IntegerField(default=0)
    away = models.ForeignKey(Tour, on_delete=models.CASCADE,related_name='club_tour_a')
    # home = models.ForeignKey(Tour, on_delete=models.CASCADE,related_name='club_tour_h')
    # goal_home = models.ForeignKey(Tour, on_delete=models.CASCADE,related_name='club_goal_h')
    # goal_away = models.ForeignKey(Tour, on_delete=models.CASCADE,related_name='club_goal_a')
    # away = models.ForeignKey(Tour, on_delete=models.CASCADE,related_name='club_tour_a')