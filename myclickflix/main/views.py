from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.core.paginator import Paginator

from main.models import Category, Movie, Actor
from main.forms import MovieFilterForm


def move_list(request):
    form = MovieFilterForm(request.GET)
    movies = Movie.objects.all().filter(available=True)

    if form.is_valid():
        print(form.cleaned_data["categories"])
        if form.cleaned_data["title"]:
            movies = movies.filter(title__icontains=form.cleaned_data["title"])
        if form.cleaned_data["price_min"]:
            movies = movies.filter(score_gte=form.cleaned_data["price_min"])
        if form.cleaned_data["price_max"]:
            movies = movies.filter(score_lte=form.cleaned_data["price_max"])
        categories = form.cleaned_data["categories"]
        for category in categories:
            movies = movies.filter(categories=category)

    paginator = Paginator(movies, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "product/search.html", {"form": form, "movies": page_obj})


def movie_detail(request, movie_slug):
    try:
        movie = Movie.objects.get(slug=movie_slug, available=True)
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
    movies = actor.movie.all().filter(available=True)

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

    movies = category.movie.all().filter(available=True)
    paginator = Paginator(movies, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "category": category,
        "movies": page_obj,
    }
    return render(request, "product/category.html", context=context)
