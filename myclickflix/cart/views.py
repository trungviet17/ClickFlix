from django.shortcuts import render, get_object_or_404, redirect
from main.models import Movie
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from main.models import Movie

# from cart.models import Cart
from cart.cart import Cart

# Create your views here.


@require_POST
def add_to_cart(request, movie_id):
    cart = Cart(request)
    movie = get_object_or_404(Movie, id=movie_id)
    cart.add(movie=movie)

    # chuyển hướng về trang cũ
    return redirect("cart:cart_detail")


@require_POST
def remove_from_cart(request, movie_id):
    cart = Cart(request)
    movie = get_object_or_404(Movie, id=movie_id)
    cart.remove(movie)

    # chuyển về trang cũ
    return redirect("cart:cart_detail")


def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/detail.html", {"cart": cart})
