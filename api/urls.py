from django.urls import path

from . import views
from rest_framework_simplejwt import views as jwt_views


from .apiviews import all_characters, characterCRUD, add_characters, characterDetails


urlpatterns = [
    path("all_characters", all_characters.as_view(), name="all_characters"),
    path("add_characters", add_characters.as_view(), name="add_characters"),
    path("characterCRUD/<str:name>/<int:pk>", characterCRUD.as_view(), name="delete_character"),
    path("character_details/<str:name>/<int:pk>", characterDetails.as_view(), name="character_details"),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

# urlpatterns = [
#     path("all_characters", views.all_characters, name="home"),
#     path("add_character", views.add_character, name="add_character"),
#     path("delete_character/<str:name>", views.delete_character, name="delete_character"),
#     path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
# ]
