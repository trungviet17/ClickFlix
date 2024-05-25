from django.urls import path
from main.views import (
    movie_detail,
    actor_detail,
    move_list,
    get_category,
    your_movie_list,
)


urlpatterns = [
    path("mymovie/", your_movie_list, name="my_movie_list"),
    path("search/", move_list, name="search_movie"),
    path("movie/<slug:movie_slug>/", movie_detail, name="movie_detail"),
    path("actor/<slug:actor_slug>/", actor_detail, name="actor_detail"),
]
