from csv import DictReader

from django.core.management import BaseCommand
from reviews.models import Comment
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(
                'static/data/comments.csv', 'r', encoding='utf-8'
        ) as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                comment = Comment(id=row['id'], review_id=row['review_id'],
                                  text=row['text'], pub_date=row['pub_date'],
                                  author=User.objects.get(id=row['author']))
                comment.save()
