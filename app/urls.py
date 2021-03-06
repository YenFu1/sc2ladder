from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("search", search, name="search"),
    path("ladder", ladder, name="ladder"),
    path("about", about, name="about"),
    path(
        "player/<slug:region>/<int:realm>/<int:profile_id>/<slug:race>",
        player,
        name="player",
    ),
    path("api/player", api_search, name="api"),
    path(
        "api/player/<int:region>/<int:realm>/<int:playerid>",
        api_player,
        name="api-player",
    ),
    path("api/clans/<str:clan_name>", api_clans, name="api-clans"),
    path("api/grandmaster/<str:region>", api_grandmaster, name="api-grandmaster"),
    path("robots.txt", robots, name="robot.txt"),
]
