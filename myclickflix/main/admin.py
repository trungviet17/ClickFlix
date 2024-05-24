from django.contrib import admin
from .models import Category, Movie, Actor


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "slug",
        "score",
        "popularity",
        "price",
        "language",
        "released",
        "available",
        "image",
    ]
    search_fields = ["title", "overview"]
    list_filter = [
        "available",
        "created_at",
        "updated_at",
        "score",
        "popularity",
        "price",
        "language",
    ]
    list_editable = ["price", "available"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["name", "birthday", "bio"]
    list_filter = ["name", "birthday"]
    prepopulated_fields = {"slug": ("name",)}
