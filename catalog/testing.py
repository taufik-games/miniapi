"""
Test on django shell
./manage.py shell
"""
from crawl.models import Page
from catalog import parse


# from catalog.testing import *; zalando();
def zalando():
    p_all = Page.objects.filter(file__provider='zalando.nl', type='product_detail')
    for i in range(1, p_all.count()-1):
        z = parse.HTMLDoc.provider(name=p_all[i].file.provider, html_doc=p_all[i].body)
        print p_all[i].id
        print z.name
        print z.brand
        print z.price


# from catalog.testing import *; omoda();
def omoda():
    p_all = Page.objects.filter(file__provider='omoda.nl', type='product_detail')
    for i in range(0, p_all.count()-1):
        o = parse.HTMLDoc.provider(name=p_all[i].file.provider, html_doc=p_all[i].body)
        print p_all[i].id
        print o.name
        print o.brand
        print o.price


# from catalog.testing import *; provider();
def provider():
    p_all = Page.objects.filter(type='product_detail')
    for i in range(24305, p_all.count() - 1):
        p_page = parse.HTMLDoc.provider(name=p_all[i].file.provider, html_doc=p_all[i].body)
        print p_all[i].id
        print p_page.name
        print p_page.brand
        print p_page.price
