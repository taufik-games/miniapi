from django.core.management.base import BaseCommand
from catalog.models import Category


class Command(BaseCommand):
    """
    Delete all categories
    """
    help = "Clearing all records of the category"

    def handle(self, *args, **options):
        Category.objects.all().delete()

        print 'Success: clearing all categories!'
