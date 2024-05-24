from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.cart_detail, name="cart_detail"),
    path("remove/<int:movie_id>", views.remove_from_cart, name="remove_from_cart"),
]
