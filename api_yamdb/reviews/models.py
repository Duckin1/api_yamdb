import datetime as dt

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User


class Category(models.Model):
    name = models.TextField(max_length=256)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.TextField(max_length=256)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='categories',
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(Genre, through='GenreTitle')
    name = models.TextField(max_length=256)
    year = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(int(dt.date.today().year))
    ])
    description = models.TextField()


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    score = models.IntegerField(db_index=True, validators=[
        MinValueValidator(1, message='Рейтинг не может быть меньше 1!'),
        MaxValueValidator(10, message='Рейтинг не может быть больше 10!')
    ])
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'], name='unique_title_author'
            )
        ]


class Comment(models.Model):
    """Модель комментариев."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
