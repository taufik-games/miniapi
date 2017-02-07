import sys
from haystack.query import SearchQuerySet
from django.core.management.base import BaseCommand
from crawl.models import Page
from catalog.models import Product, Category


class Command(BaseCommand):
    """
    Add category to product.
    Search product on page which has type of the product_listing,
    and add category from that page to current product.
    """
    help = 'Add category to Product.'

    def handle(self, *args, **options):
        products = Product.objects.all()
        for i in range(0, products.count() - 1):
            # Print progress
            sys.stdout.write('\r%d' % i)
            sys.stdout.flush()

            product = products[i]
            pages = SearchQuerySet().models(Page).filter(type='product_listing',
                                                         provider=product.provider.name,
                                                         body__exact=product.name)
            if pages:
                page = pages.best_match()
            else:
                pages = SearchQuerySet().models(Page).filter(type='product_listing',
                                                             provider=product.provider.name,
                                                             body=product.name)
                if pages:
                    page = pages[0]

            if pages:
                # Convert category of the page to array
                names = eval(page.category)
                for name in names:
                    category = Category.objects.get(name=name)
                    # Added category to current product
                    product.categories.add(category)

        print '\nAdded category to products is finished!'



