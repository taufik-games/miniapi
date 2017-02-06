import sys
from django.core.management.base import BaseCommand
from crawl.models import Page
from catalog.models import Product, Provider, Brand
from catalog import parse


class Command(BaseCommand):
    """
    Convert page of product_deatil to product,
    """
    help = 'Convert data page to categories.'

    def handle(self, *args, **options):
        # Category only exist on page with the type of product_listing.
        p_listing = Page.objects.filter(type='product_detail')

        # Using range index of record to avoid slowly read & overload.
        for i in range(24305, p_listing.count() - 1):
            # Print progress
            sys.stdout.write('\r%d' % i)
            sys.stdout.flush()

            p_page = parse.HTMLDoc.provider(name=p_listing[i].file.provider, html_doc=p_listing[i].body)

            if p_page.brand:
                try:
                    brand = Brand.objects.get(name=p_page.brand)
                except Brand.DoesNotExist:
                    brand = Brand(name=p_page.brand)
                    brand.save()

                provider = Provider.objects.get(name=p_listing[i].file.provider)

                try:
                    Product.objects.get(name=p_page.name, provider=provider)
                except Product.DoesNotExist:
                    product = Product()
                    product.name = p_page.name
                    product.provider = provider
                    product.brand = brand

                    # Get price and old price
                    price, old_price = p_page.price
                    product.price = float(price.replace('.', '').replace(',', '.'))
                    product.old_price = float(old_price.replace('.', '').replace(',', '.'))
                    product.url = p_listing[i].url
                    product.save()

        print '\nConverting has been finished!'

