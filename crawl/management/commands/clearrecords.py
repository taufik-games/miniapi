from django.core.management.base import BaseCommand
from crawl.models import File


class Command(BaseCommand):
    """
    Clear all records of the file
    """
    help = "Clearing all records"

    def handle(self, *args, **options):
        File.objects.all().delete()

        print 'Success: clearing all records!'
