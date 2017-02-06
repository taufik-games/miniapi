from __future__ import unicode_literals

from django.db import models


class Created(models.Model):
    """
    Base model by created at
    """
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Name(models.Model):
    """
    Base model of unique name
    """
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '{}'.format(self.name)
