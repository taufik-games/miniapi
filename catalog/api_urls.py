from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^product/search/$',
        api.Search.as_view({'get': 'get'}),
        name='api_v1_catalog_product_search'),
]
