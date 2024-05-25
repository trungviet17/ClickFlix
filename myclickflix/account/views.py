from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from cart.cart import Cart

from account.form import UserEditForm, UserRegistrationForm, ProfileForm
from account.models import Profile

from main.models import Category, Movie

from django.db.models import Count


"""Hàm view cho màn hình đăng kí tài khoản của người dùng """


def register(request):

    if request.method == "POST":
        userform = UserRegistrationForm(request.POST)

        if userform.is_valid():
            new_user = userform.save(commit=False)
            new_user.set_password(userform.cleaned_data["password"])
            new_user.username = str(userform.cleaned_data["email"]).split("@")[0]
            new_user.save()

            Profile.objects.create(user=new_user)

            return render(request, "account/register_done.html", {"new_user": new_user})

    else:
        userform = UserRegistrationForm()

    return render(request, "account/register.html", {"userform": userform})


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)

        profile_form = ProfileForm(instance=request.user.profile, data=request.POST)

        form_edit_password = PasswordChangeForm(user=request.user, data=request.POST)

        if form_edit_password.is_valid():
            form_edit_password.save()
        else:

            messages.error(request, "Error updating your profile")

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            print(1)

            messages.success(request, "Profile update sucessfully")

        else:
            messages.error(request, "Error updating your profile")

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        form_edit_password = PasswordChangeForm(user=request.user)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "edit_password_form": form_edit_password,
    }

    return render(request, "account/edit.html", context)


def dashboard(request):
    # categories = Category.objects.all()[:12]
    categories = Category.objects.annotate(num_movies=Count("movie")).order_by(
        "-num_movies"
    )[:12]
    popular_movies = Movie.objects.filter().order_by("-popularity")[:15]
    latest_movies = Movie.objects.filter().order_by("-released")[:10]

    context = {
        "categories": categories,
        "popular_movies": popular_movies,
        "latest_movies": latest_movies,
    }
    return render(request, "account/dashboard.html", context=context)
