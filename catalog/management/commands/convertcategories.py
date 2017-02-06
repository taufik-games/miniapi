import sys
from django.core.management.base import BaseCommand
from crawl.models import Page
from catalog.models import Category


class Command(BaseCommand):
    """
    Convert page of product_listing to category,
    """
    help = 'Convert data page to categories.'

    def handle(self, *args, **options):
        # Category only exist on page with the type of product_listing.
        p_listing = Page.objects.filter(type='product_listing')

        progress = 0
        for page in p_listing:
            # Print progress
            progress += 1
            sys.stdout.write('\r%d' % progress)
            sys.stdout.flush()

            if page.category:
                # Convert to array
                a_categories = eval(page.category)

                for arr in a_categories:
                    try:
                        Category.objects.get(name=arr)
                    except Category.DoesNotExist:
                        category = Category(name=arr)
                        category.save()

        print '\nConverting has been finished!'

