from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from main.models import Movie, Actor, RechargeCode, Category
from account.models import Profile
from main.forms import MovieFilterForm, RechargeForm
from main.recommend import recommend


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
    context = {
        "movie": movie,
        "actors": actors,
        "categories": categories,
        "recommendations": recommendations,
    }
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
def recharge_account(request):
    if request.method == "POST":
        form = RechargeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            try:
                recharge_code = RechargeCode.objects.get(code=code, quantity__gte=1)
            except RechargeCode.DoesNotExist:
                messages.error(request, "Invalid or already used recharge code!")
            profile = Profile.objects.get(user=request.user)
            profile.balance += recharge_code.amount
            profile.save()

            recharge_code.quantity -= 1
            recharge_code.save()
            messages.success(
                request,
                f"Successfully recharged {recharge_code.amount} to your account!",
            )
            return render(request, "payment/recharge.html", {"form": form})
    else:
        form = RechargeForm()
    return render(request, "payment/recharge.html", {"form": form})
