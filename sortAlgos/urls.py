from django.urls import path
from . import views
urlpatterns = [
    path("", views.homePageEmpty),
    path("sort/", views.sortingPage)
]