from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Resets points for players'

    def handle(self,*args,**kwargs):
        get_user_model().objects.all().update(skips=3)