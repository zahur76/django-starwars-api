from django.urls import path

from . import views


urlpatterns = [
    path("all_characters", views.all_characters, name="home"),
    path("add_character", views.add_character, name="add_character"),
    path("delete_character/<str:name>", views.delete_character, name="delete_character"),
]
