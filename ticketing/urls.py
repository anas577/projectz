from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("book/<int:routeid>", views.book, name="book"),
    path("bus_location", views.bus_location, name="bus_location"),
]