from django.db import models
from django.utils.text import slugify

from typing import List
import json

from account.models import Profile


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampMixin):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + " " + str(self.pk))
        super(Category, self).save(*args, **kwargs)


class Actor(TimeStampMixin):
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    bio = models.TextField()
    image = models.TextField()
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]
        verbose_name = "actor"
        verbose_name_plural = "actors"

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + " " + str(self.pk))
        super(Actor, self).save(*args, **kwargs)


class Movie(TimeStampMixin):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    overview = models.TextField()
    score = models.FloatField()
    popularity = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    language = models.CharField(max_length=5)
    released = models.DateField()
    available = models.BooleanField(default=True)
    keyword = models.TextField(default="")
    image = models.TextField(default="")

    actors = models.ManyToManyField(Actor, related_name="movie")
    categories = models.ManyToManyField(Category, related_name="movie")

    class Meta:
        ordering = ["title"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["title"]),
            models.Index(fields=["-created_at"]),
        ]
        verbose_name = "movie"
        verbose_name_plural = "movies"

    def __str__(self) -> str:
        return self.title

    def set_keyword(self, keyword: List[str]):
        self.keyword = json.dumps(keyword)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + " " + str(self.pk))
        super(Movie, self).save(*args, **kwargs)
