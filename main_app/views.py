from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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
@login_required
def games_index(request):
  games = Game.objects.all() # Retrieve all games
  return render(request, 'games/index.html', {
    'games': games
  })

# View game
@login_required
def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  id_list = game.achievements.all().values_list('id')
  achievements_game_doesnt_have = Achievement.objects.exclude(id__in=id_list)
  activity_form = ActivityForm()
  return render(request, 'games/detail.html', {
    'game': game, 'activity_form': activity_form,
    'achievements': achievements_game_doesnt_have
  })

class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  #fields = '__all__'
  fields = ['name', 'genre', 'description', 'year']
  #success_url = '/games/{game_id}'

  def form_valid(self, form):
   form.instance.user = self.request.user
   return super().form_valid(form)

class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = ['genre', 'description', 'year']

class GameDelete(LoginRequiredMixin, DeleteView):
  model = Game
  success_url = '/games'

# Activity Views

@login_required 
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
  fields = ['title', 'task']

class AchievementDelete(DeleteView):
  model = Achievement
  success_url = '/achievements'

@login_required
def assoc_achievement(request, game_id, achievement_id):
  Game.objects.get(id=game_id).achievements.add(achievement_id)
  return redirect('detail', game_id=game_id)

@login_required
def unassoc_achievement(request, game_id, achievement_id):
  Game.objects.get(id=game_id).achievements.remove(achievement_id)
  return redirect('detail', game_id=game_id)

# Sign Up View

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
