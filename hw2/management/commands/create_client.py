from django.core.management.base import BaseCommand
from hw2.models import Client


class Command(BaseCommand):
    help = 'Create client'

    def handle(self, *args, **kwargs):
        client = Client(
            name='Jack',
            email='sparrow@example.com',
            phone='87651231221',
            address='black pearl',
        )
        client.save()
        self.stdout.write(f'{client.name} was created')