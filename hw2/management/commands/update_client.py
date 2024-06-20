from django.core.management.base import BaseCommand
from hw2.models import Client


class Command(BaseCommand):
    help = 'Update client'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int)
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone', type=str)
        parser.add_argument('address', type=str)

    def handle(self, *args, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        address = kwargs.get('address')
        client = Client.objects.filter(id=id).first()
        client.name = name
        client.email = email
        client.phone = phone
        client.address = address
        client.save()
        self.stdout.write(f'Client {client.name} was updated')
