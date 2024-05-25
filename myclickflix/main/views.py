from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from main.models import Movie, Actor, Category
from account.models import Profile
from main.forms import MovieFilterForm
from main.recommend import recommend
from payment.models import PurchasedMovie


def move_list(request):
    form = MovieFilterForm(request.GET)
    movies = Movie.objects.all().filter(available=True)

    if form.is_valid():
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
    return render(request, "product/shop.html", {"form": form, "movies": page_obj})


def movie_detail(request, movie_slug):
    try:
        movie = Movie.objects.get(slug=movie_slug, available=True)
    except Movie.DoesNotExist:
        return HttpResponseNotFound("Movie not found")
    actors = movie.actors.all()
    categories = movie.categories.all()
    recommendations = recommend(movie.id)
    recommendations = Movie.objects.filter(id__in=recommendations)
    if request.user.is_authenticated == None:
        is_purchased = False
    else:
        is_purchased = PurchasedMovie.objects.filter(
            movie_id=movie.id, profile_id=request.user.profile.id
        ).exists()
        print(1)
    context = {
        "movie": movie,
        "actors": actors,
        "categories": categories,
        "recommendations": recommendations,
        "is_purchased": is_purchased,
    }

    print(is_purchased)
    return render(request, "product/product-detals.html", context=context)


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


def get_category(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "product/category.html", context=context)


@login_required
def your_movie_list(request):

    movies = PurchasedMovie.objects.filter(profile_id=request.user.profile.id)
    context = {"movies": movies}
    return render(request, "product/your-movie-list.html", context=context)
