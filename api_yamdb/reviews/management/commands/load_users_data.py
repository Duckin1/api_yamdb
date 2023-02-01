from csv import DictReader

from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('static/data/users.csv', 'r', encoding='utf-8') as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                user = User(id=row['id'], username=row['username'],
                            email=row['email'], role=row['role'],
                            bio=row['bio'], first_name=row['first_name'],
                            last_name=row['last_name'])
                user.save()
