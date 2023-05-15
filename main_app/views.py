from django.shortcuts import render

# Dummy Python List
games = [
  {'name': 'Legend of Zelda BoW 2', 'genre': 'Family', 'description': 'Rediscover Hyrule', 'year': 2023},
  {'name': 'Splatoon 3', 'genre': 'Family', 'description': 'Have fun in this co-op shooter', 'year': 2023},
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# View all games
def games_index(request):
  return render(request, 'games/index.html', {
    'games': games
  })