from django.db import models

# Create your models here.
class Player(models.Model):
        player_id = models.AutoField(primary_key=True)
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        date_of_birth = models.DateField()
        nationality = models.CharField(max_length=100)
        position = models.CharField(max_length=50)
        current_club = models.CharField(max_length=100)
        previous_clubs = models.TextField()
        international_caps = models.IntegerField()  # IntegerField for whole numbers
        goals_scored = models.IntegerField()  # IntegerField for whole numbers
        height = models.FloatField()  # FloatField for floating-point numbers
        weight = models.FloatField()  # FloatField for floating-point numbers
        preferred_foot = models.CharField(max_length=10)
        biography = models.TextField()
        achievements = models.TextField()
        profile_picture = models.URLField()


        def __str__(self):
                return f"{self.first_name} _ {self.last_name}"