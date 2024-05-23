from django.urls import path
from main.views import movie_detail, actor_detail, category_detail, move_list


urlpatterns = [
    path("search/", move_list, name="search_movie"),
    path("movie/<slug:movie_slug>/", movie_detail, name="movie_detail"),
    path("actor/<slug:actor_slug>/", actor_detail, name="actor_detail"),
    path("category/<slug:category_slug>", category_detail, name="category_detail"),
]
