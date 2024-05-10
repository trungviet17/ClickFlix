from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampMixin):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name


class Actor(TimeStampMixin):
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    bio = models.TextField()
    image = models.ImageField(
        upload_to='actor/%Y/%M/%D',
        blank=True
    )
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = "actor"
        verbose_name_plural = "actors"

    def __str__(self) -> str:
        return self.name


class Movie(TimeStampMixin):
    category = models.ForeignKey(
        Category,
        related_name='movies',
        on_delete=models.PROTECT
    )
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    overview = models.TextField()
    score = models.FloatField()
    popularity = models.FloatField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    language = models.CharField(max_length=5)
    released = models.DateField()
    available = models.BooleanField(default=True)
    image = models.ImageField(
        upload_to='movies/%Y/%M/%D',
        blank=True
    )
    actors = models.ManyToManyField(Actor, related_name='movies')

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['title']),
            models.Index(fields=['-created_at'])
        ]
        verbose_name = "movie"
        verbose_name_plural = "movies"

    def __str__(self) -> str:
        return self.title


# class MovieActor(models.Model):
#     movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
#     actor = models.ForeignKey(Actor, on_delete=models.PROTECT)
