from django.urls import path
from . import views
urlpatterns = [
    path("sortnumbers/", views.renderSortingPage, name="sorting_page")
]