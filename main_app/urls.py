from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('games/', views.games_index, name='index'),
  path('games/<int:game_id>/', views.games_detail, name='detail'),
  path('games/create/', views.GameCreate.as_view(), name='games_create'),
  path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
  path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
  path('games/<int:game_id>/add_activity/', views.add_activity, name='add_activity'),
  # Achievements
  path('achievements/', views.AchievementList.as_view(), name='achievements_index'),
  path('achievements/<int:pk>/', views.AchievementDetail.as_view(), name='achievements_detail'),
  path('achievements/create/', views.AchievementCreate.as_view(), name='achievements_create'),
  path('achievements/<int:pk>/update/', views.AchievementUpdate.as_view(), name='achievements_update'),
  path('achievements/<int:pk>/delete/', views.AchievementDelete.as_view(), name='achievements_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]