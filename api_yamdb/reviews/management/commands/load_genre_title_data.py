from csv import DictReader

from django.core.management import BaseCommand
from reviews.models import GenreTitle


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(
                'static/data/genre_title.csv', 'r', encoding='utf-8'
        ) as csvfile:
            reader = DictReader(csvfile)
            print(reader)
            for row in reader:
                genre_title = GenreTitle(id=row['id'],
                                         title_id=row['title_id'],
                                         genre_id=row['genre_id'])
                genre_title.save()
