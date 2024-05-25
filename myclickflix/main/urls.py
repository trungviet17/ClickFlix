from django.urls import path
from main.views import (
    movie_detail,
    actor_detail,
    search_movie,
    your_movie_list,
)


urlpatterns = [
    path("mymovie/", your_movie_list, name="my movie"),
    path("search/", search_movie, name="search_movie"),
    path("movie/<slug:movie_slug>/", movie_detail, name="movie_detail"),
    path("actor/<slug:actor_slug>/", actor_detail, name="actor_detail"),
]
