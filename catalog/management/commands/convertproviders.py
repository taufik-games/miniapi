import sys
from django.core.management.base import BaseCommand
from crawl.models import File
from catalog.models import Provider


class Command(BaseCommand):
    """
    Convert file to provider model
    """
    help = 'Convert data file to providers.'

    def handle(self, *args, **options):
        f_all = File.objects.all()

        progress = 0
        for f_rec in f_all:
            # Print progress
            progress += 1
            sys.stdout.write('\r%d' % progress)
            sys.stdout.flush()

            try:
                Provider.objects.get(name=f_rec.provider)
            except Provider.DoesNotExist:
                p_rec = Provider(name=f_rec.provider)
                p_rec.save()

        print '\nConverting has been finished!'

