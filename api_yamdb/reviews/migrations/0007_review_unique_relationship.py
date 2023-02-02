# Generated by Django 3.2 on 2023-02-01 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_remove_review_unique_relationship'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='unique_relationship'),
        ),
    ]