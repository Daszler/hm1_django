from django.core.management.base import BaseCommand
from hw2.models import Client


class Command(BaseCommand):
    help = "Delete client by id."

    def add_arguments(self, parser):
        parser.add_argument("id", type=int)

    def handle(self, *args, **kwargs):
        id = kwargs.get("id")
        client = Client.objects.filter(id=id).first()
        if client is not None:
            client.delete()
        self.stdout.write(f"{client.name} was deleted")