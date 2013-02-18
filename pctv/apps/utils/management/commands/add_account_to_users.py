from django.core.management import BaseCommand
from django.contrib.auth.models import User
from apps.account.models import Account

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for u in users:
            Account(user=u, commission_percentage=10.0).save()

