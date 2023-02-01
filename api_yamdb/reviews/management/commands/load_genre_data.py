from csv import DictReader

from django.core.management import BaseCommand
from reviews.models import Genre


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('static/data/genre.csv', 'r', encoding='utf-8') as csvfile:
            reader = DictReader(csvfile)
            print(reader)
            for row in reader:
                genre = Genre(id=row['id'], name=row['name'],
                              slug=row['slug'])
                genre.save()
