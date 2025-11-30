from django.urls import path
from . import views 

urlpatterns = [
    path("leaderboard/", views.sendLeaderBoard),
    path("updateleaders/", views.updateLeaderBoard)
]