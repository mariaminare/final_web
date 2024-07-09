from django.db import models
from django.contrib.auth.models import AbstractUser
class Nation(models.Model):
        name=models.CharField(max_length=100)
        world_ranking=models.IntegerField()
        def __str__(self):
                return f"{self.name}"
class Club(models.Model):
        name=models.CharField(max_length=100)
        foundation_date=models.DateField(null=True)
        ground=models.CharField(max_length=100)
        capacity=models.IntegerField()
        president=models.CharField(max_length=100)
        head_coach=models.CharField(max_length=100)
        league=models.CharField(max_length=100)
        website= models.URLField()

        def __str__(self):
                return self.name
# Create your models here.
class Player(models.Model):
        player_id = models.AutoField(primary_key=True)
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        date_of_birth = models.DateField()
        nation =models.ForeignKey(Nation, on_delete=models.SET("Unknown"), related_name='players')
        position = models.CharField(max_length=50)
        club = models.ForeignKey(Club, on_delete=models.SET("Unknown"), related_name='players')
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
class User(AbstractUser):
        players = models.ManyToManyField(Player, blank=True, related_name="users")