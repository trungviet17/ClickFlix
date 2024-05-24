from django.db import models
from django.contrib.auth.models import User
from main.models import Movie

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date_to_add = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["date_to_add"]

    def __str__(self):
        return "Cart of " + self.user.username
