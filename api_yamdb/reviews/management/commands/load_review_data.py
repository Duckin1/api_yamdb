from csv import DictReader

from django.core.management import BaseCommand
from reviews.models import Review
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('static/data/review.csv', 'r', encoding='utf-8') as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                review = Review(id=row['id'], title_id=row['title_id'],
                                text=row['text'], score=row['score'],
                                author=User.objects.get(id=row['author']),
                                pub_date=row['pub_date'])
                review.save()
