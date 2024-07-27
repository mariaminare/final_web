from django.urls import path
from . import views
urlpatterns = [
    path('', views.get_routes),
    path('players/', views.get_players),
    path('players/<str:id>', views.get_player)
]