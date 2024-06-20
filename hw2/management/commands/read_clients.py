from django.core.management.base import BaseCommand
from hw2.models import Client


class Command(BaseCommand):
    help = 'Read clients'

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        for client in clients:
            self.stdout.write(f'{client.id}: {client.name}, {client.email}, {client.phone}, {client.address}')