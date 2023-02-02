from csv import DictReader

from django.core.management import BaseCommand
from reviews.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(
                'static/data/category.csv', 'r', encoding='utf-8'
        ) as csvfile:
            reader = DictReader(csvfile)
            print(reader)
            for row in reader:
                category = Category(id=row['id'], name=row['name'],
                                    slug=row['slug'])
                category.save()
