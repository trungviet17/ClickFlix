from django.urls import path
from main.views import (
    movie_detail,
    actor_detail,
    move_list,
    recharge_account,
    get_category,
)


urlpatterns = [
    path("category", get_category, name="category"),
    path("search/", move_list, name="search_movie"),
    path("movie/<slug:movie_slug>/", movie_detail, name="movie_detail"),
    path("actor/<slug:actor_slug>/", actor_detail, name="actor_detail"),
    path("recharge/", recharge_account, name="recharge"),
]
