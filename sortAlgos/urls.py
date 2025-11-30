from django.urls import path
from . import views
urlpatterns = [
    path("", views.homePageEmpty, name="empty_page"),
    path("sort/", views.sortingPage, name="sorting_page")
]