from django.db import models

User = 'just_test'


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
        null=True
    )
    genre = models.ManyToManyField(Genre)
    name = models.TextField(max_length=256)
    year = models.IntegerField()
    description = models.TextField()
