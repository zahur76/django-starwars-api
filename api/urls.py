from django.urls import path

from . import views

# from .apiviews import all_characters, delete_character


# urlpatterns = [
#     path("all_characters", all_characters.as_view(), name="all_characters"),
#     path("delete_character/<str:name>", delete_character.as_view(), name="delete_character"),
# ]

urlpatterns = [
    path("all_characters", views.all_characters, name="home"),
    path("add_character", views.add_character, name="add_character"),
    path("delete_character/<str:name>", views.delete_character, name="delete_character"),
]
