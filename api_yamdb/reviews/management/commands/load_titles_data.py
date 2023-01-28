from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Title


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('static/data/titles.csv', 'r') as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                title = Title(id=row['id'], name=row['name'],
                              year=row['year'], category=row['category'])
                title.save()