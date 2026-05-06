import django.core.management.base as base

from app_people.models import Person

class Command(base.BaseCommand):
    def handle(self, *args, **options):
        print(Person.objects.all())