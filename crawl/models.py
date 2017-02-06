from __future__ import unicode_literals

from django.db import models
import base.models


class File(base.models.Created):
    """
    Record of the crawl file path.
    Path is unique to avoid double entry.
    Provider is domain name.
    """
    path = models.FilePathField(unique=True)
    provider = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.provider)


class Page(base.models.Created):
    """
    JSON object of the content file.
    """
    file = models.ForeignKey(File)
    crawled_at = models.DateTimeField()
    type = models.CharField(max_length=20)
    url = models.URLField()
    number = models.IntegerField(null=True, blank=True)
    ordering = models.CharField(max_length=20, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return '{}'.format(self.url)
