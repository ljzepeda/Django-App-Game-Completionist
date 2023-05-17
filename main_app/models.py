from django.db import models
from django.urls import reverse
from datetime import date

PROGRESS = (
  ('NS', 'Not Started'),
  ('IP', 'In Progress'),
  ('C', 'Completed'),
  ('NG+', 'New Game+'),
)

# Create your models here.

# Achievement Model (Many to Many)
class Achievement(models.Model):
  title = models.CharField(max_length=50)
  task = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('achievements_detail', kwargs={'pk': self.id})


# Game Model (Main)
class Game(models.Model):
  name = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  year = models.IntegerField()
  achievements = models.ManyToManyField(Achievement)

  def __str__(self):
    #return self.name
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'game_id': self.id})
  
  def activity_for_today(self):
    return self.activity_set.filter(date=date.today()).count() >= 1

#Activity Model (One to Many)
class Activity(models.Model):
  date = models.DateField('Activity Date')
  progress = models.CharField(
    max_length=3,
    choices=PROGRESS,
    default=PROGRESS[0][0]
  )
  # Create a game_id FK
  game = models.ForeignKey(
    Game,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_progress_display()} on {self.date}"

  class Meta:
    ordering = ['-date']