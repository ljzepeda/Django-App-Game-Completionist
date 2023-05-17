from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game, Achievement
from .forms import ActivityForm

# Dummy Python List for Data
#games = [
  #{'name': 'Legend of Zelda BoW 2', 'genre': 'Family', 'description': 'Rediscover Hyrule', 'year': 2023},
  #{'name': 'Splatoon 3', 'genre': 'Family', 'description': 'Have fun in this co-op shooter', 'year': 2023},
#]

# Create your views here.
# Game Views
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# View all games
def games_index(request):
  games = Game.objects.all() # Retrieve all games
  return render(request, 'games/index.html', {
    'games': games
  })

# View game
def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  id_list = game.achievements.all().values_list('id')
  achievements_game_doesnt_have = Achievement.objects.exclude(id__in=id_list)
  activity_form = ActivityForm()
  return render(request, 'games/detail.html', {
    'game': game, 'activity_form': activity_form
    'achievements': achievements_game_doesnt_have
  })

class GameCreate(CreateView):
  model = Game
  #fields = '__all__'
  fields = ['name', 'genre', 'description', 'year']
  #success_url = '/games/{game_id}'

class GameUpdate(UpdateView):
  model = Game
  fields = ['genre', 'description', 'year']

class GameDelete(DeleteView):
  model = Game
  success_url = '/games'

# Activity Views
def add_activity(request, game_id):
  form = ActivityForm(request.POST)
  if form.is_valid():
    new_activity = form.save(commit=False)
    new_activity.game_id = game_id
    new_activity.save()
  return redirect('detail', game_id=game_id)

# Achievement Views

class AchievementList(ListView):
  model = Achievement

class AchievementDetail(DetailView):
  model = Achievement

class AchievementCreate(CreateView):
  model = Achievement
  fields = '__all__'

class AchievementUpdate(UpdateView):
  model = Achievement
  fields = ['name', 'color']

class AchievementDelete(DeleteView):
  model = Achievement
  success_url = '/achievements'

def assoc_achievement(request, game_id, achievement_id):
  Game.objects.get(id=game_id).achievements.add(achievement_id)
  return redirect('detail', game_id=game_id)

def unassoc_achievement(request, game_id, achievement_id):
  Game.objects.get(id=game_id).achievements.remove(achievement_id)
  return redirect('detail', game_id=game_id)
