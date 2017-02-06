import os.path
import ast
import sys
from django.core.management.base import BaseCommand
from crawl.models import File, Page


class Command(BaseCommand):
    """
    Extract crawl file to database.
    Need argument path of file and provider name.
    Exp: ./manage.py extract filename.txt omoda.nl
    """
    help = 'Extract a crawl file.'
    options = {}

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)
        parser.add_argument('provider', type=str)

    def process(self):
        path = self.options.get('path', None)

        if not os.path.isfile(path):
            print "Error: file path doesn't exist!"

            return False

        provider = self.options.get('provider', None)

        # Avoid double extract
        try:
            File.objects.get(path=path)
            print "Error: {} is already extracted!".format(path)

            return False
        except File.DoesNotExist:
            f_rec = File(path=path, provider=provider)
            f_rec.save()

        # Read crawl file
        c_file = open(path)
        progress = 0

        for line in c_file:
            try:
                # Print progress
                progress += 1
                sys.stdout.write('\r%d' % progress)
                sys.stdout.flush()

                # Convert to dictionary
                l_dict = ast.literal_eval(line)

                p_rec = Page()
                p_rec.file = f_rec
                # Add Z aware to UTC time zone
                p_rec.crawled_at = '{}Z'.format(l_dict['crawled_at'])
                p_rec.type = l_dict['page_type']
                p_rec.url = l_dict['page_url']
                p_rec.number = l_dict['page_number'] if 'page_number' in l_dict else None
                p_rec.ordering = l_dict['ordering'] if 'ordering' in l_dict else None
                p_rec.category = l_dict['product_category'] if 'product_category' in l_dict else None
                p_rec.body = l_dict['body']
                p_rec.save()
            except ValueError:
                # Not a dictionary value
                print " - Error: Value."

        c_file.close()

        return True

    def handle(self, *args, **options):
        self.options = options

        if self.process():
            print " - Success: extracted!"
