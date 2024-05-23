from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.core.paginator import Paginator
from main.models import Category, Movie, Actor


def movie_detail(request, movie_slug):
    try:
        movie = Movie.objects.get(slug=movie_slug)
    except Movie.DoesNotExist:
        return HttpResponseNotFound("Movie not found")
    actors = movie.actors.all()
    categories = movie.categories.all()

    context = {
        "movie": movie,
        "actors": actors,
        "categories": categories,
    }
    return render(request, "product/movie.html", context=context)


def actor_detail(request, actor_slug):
    try:
        actor = Actor.objects.get(slug=actor_slug)
    except Movie.DoesNotExist:
        return HttpResponseNotFound("Actor not found")
    movies = actor.movie.all()

    context = {
        "actor": actor,
        "movies": movies,
    }
    return render(request, "product/actor.html", context=context)


def category_detail(request, category_slug):
    try:
        category = Category.objects.get(slug=category_slug)
    except Category.DoesNotExist:
        return HttpResponseNotFound("Category not found")

    movies = category.movie.all()
    paginator = Paginator(movies, 25)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "category": category,
        "movies": page_obj,
    }
    return render(request, "product/category.html", context=context)
