from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game

# Dummy Python List for Data
#games = [
  #{'name': 'Legend of Zelda BoW 2', 'genre': 'Family', 'description': 'Rediscover Hyrule', 'year': 2023},
  #{'name': 'Splatoon 3', 'genre': 'Family', 'description': 'Have fun in this co-op shooter', 'year': 2023},
#]

# Create your views here.
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
  return render(request, 'games/detail.html', {
    'game': game
  })

class GameCreate(CreateView):
  model = Game
  fields = '__all__'
  #success_url = '/games/{game_id}'

class GameUpdate(UpdateView):
  model = Game
  fields = ['genre', 'description', 'year']

class GameDelete(DeleteView):
  model = Game
  success_url = '/games'