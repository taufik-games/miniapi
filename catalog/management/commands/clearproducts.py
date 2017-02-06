from django.core.management.base import BaseCommand
from catalog.models import Product


class Command(BaseCommand):
    """
    Delete all products
    """
    help = "Clearing all records of the product"

    def handle(self, *args, **options):
        Product.objects.all().delete()

        print 'Success: clearing all products!'
