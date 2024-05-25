from django.db import models
from main.models import TimeStampMixin, Movie
from account.models import Profile

# Create your models here.


class PurchasedMovie(TimeStampMixin):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("profile", "movie")

    def __str__(self):
        return f"{self.profile.user.username} - {self.movie.title}"


class Order(TimeStampMixin):
    class TypeOfState(models.TextChoices):
        PAYING = "paying"
        PAID = "paid"
        CANCELED = "canceled"

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    state = models.CharField(
        max_length=10, choices=TypeOfState.choices, default=TypeOfState.PAYING
    )

    def get_total_amount(self):
        return sum(item.price for item in self.items.all())

    def get_stripe_url(self):
        pass


class OrderDetail(TimeStampMixin):

    movie = models.ForeignKey(
        Movie, related_name="order_items", on_delete=models.CASCADE
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)

    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class RechargeCode(TimeStampMixin):
    code = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
