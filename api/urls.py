from django.urls import path

from . import views

urlpatterns = [
    path("all_characters", views.all_characters, name="home"),
]
