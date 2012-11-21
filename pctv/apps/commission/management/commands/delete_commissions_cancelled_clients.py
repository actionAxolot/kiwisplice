from django.core.management.base import BaseCommand, CommandError
from apps.client.models import Client
from apps.commission.models import Commission


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Get all cancelled clients
        cancelled = Client.objects.filter(status="Cancelado")
        for c in cancelled:
            print c.pk
            Commission.objects.filter(client=c).delete()
