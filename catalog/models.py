from __future__ import unicode_literals

from django.db import models
import base.models


class Provider(base.models.Created, base.models.Name):
    pass


class Category(base.models.Created, base.models.Name):

    class Meta:
        verbose_name_plural = "categories"


class Brand(base.models.Created, base.models.Name):
    pass


class Product(base.models.Created):
    # Name is not unique to avoid the same name on different provider
    name = models.CharField(max_length=200)
    provider = models.ForeignKey(Provider)
    brand = models.ForeignKey(Brand)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    old_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    url = models.URLField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return '{}'.format(self.name)
