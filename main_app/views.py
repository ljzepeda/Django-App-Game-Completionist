from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game
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
  activity_form = ActivityForm()
  return render(request, 'games/detail.html', {
    'game': game, 'activity_form': activity_form
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

# Activity Views
def add_activity(request, game_id):
  # create a ModelForm instance using 
  # the data that was submitted in the form
  form = ActivityForm(request.POST)
  # validate the form
  if form.is_valid():
    # We want a model instance, but
    # we can't save to the db yet
    # because we have not assigned the
    # game_id FK.
    new_activity = form.save(commit=False)
    new_activity.game_id = game_id
    new_activity.save()
  return redirect('detail', game_id=game_id)