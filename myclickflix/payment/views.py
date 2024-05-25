from django.shortcuts import render, redirect, get_object_or_404
from .form import RechargeForm
from django.contrib.auth.decorators import login_required
from .models import RechargeCode, Order, OrderDetail, PurchasedMovie
from django.contrib import messages
from account.models import Profile
from cart.cart import Cart
from django.conf import settings

from django.urls import reverse
from decimal import Decimal
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


@login_required
def payment_process(request):
    order_id = request.session.get("order_id", None)
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        success_url = request.build_absolute_uri(
            reverse("payment:completed", kwargs={"order_id": order_id})
        )
        cancel_url = request.build_absolute_uri(
            reverse("payment:canceled", kwargs={"order_id": order_id})
        )

        # Stripe checkout session data
        session_data = {
            "mode": "payment",
            "client_reference_id": order.id,
            "success_url": success_url,
            "cancel_url": cancel_url,
            "line_items": [],
        }
        # add order items to the Stripe checkout session
        for item in order.items.all():
            print(int(item.price))
            session_data["line_items"].append(
                {
                    "price_data": {
                        "unit_amount": int(item.price * Decimal("100")),
                        "currency": "usd",
                        "product_data": {
                            "name": item.movie.title,
                        },
                    },
                    "quantity": 1,
                }
            )

        # create Stripe checkout session
        session = stripe.checkout.Session.create(**session_data)

        # redirect to Stripe payment form
        return redirect(session.url, code=303)

    else:
        return render(request, "payment/process.html", locals())


@login_required
def payment_completed(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.state = Order.TypeOfState.PAID

    for item in order.items.all():
        PurchasedMovie.objects.create(movie=item.movie, profile=request.user.profile)

    order.save()
    # add movie into punchase tabel

    return render(request, "payment/completed.html")


@login_required
def payment_canceled(request, order_id):

    order = get_object_or_404(Order, id=order_id)
    order.state = Order.TypeOfState.CANCELED
    order.save()

    return render(request, "payment/canceled.html")


@login_required
def create_order(request):
    cart = Cart(request)

    if request.method == "POST":
        order = Order.objects.create(profile=request.user.profile)
        for item in cart:
            OrderDetail.objects.create(
                order=order, movie=item["movie"], price=item["price"]
            )
        cart.clear()
        order.total_amount = order.get_total_amount()
        order.state = Order.TypeOfState.PAYING
        order.save()
        request.session["order_id"] = order.id
        # redirect for payment
        return redirect(reverse("payment:process"))

    return render(request, "payment/checkout.html", {"cart": cart})


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


def delete_order_detail(request, orderdetail_id):

    orderdetail = get_object_or_404(OrderDetail, id=orderdetail_id)

    return redirect(reverse("payment:create_order"))


def delete_order(request):
    order = get_object_or_404(Order, id=request.session["order_id"])
    order.delete()
    return redirect(reverse("payment:create_order"))


@login_required
def order_history(request):
    orders = Order.objects.filter(profile=request.user.profile).all()

    return render(request, "payment/order_history.html", {"orders": orders})
