from django.contrib import admin
from . import models


class File(admin.ModelAdmin):
    list_display = ('id', 'path', 'provider')

admin.site.register(models.File, File)


class Page(admin.ModelAdmin):
    list_display = ('id', 'crawled_at', 'file', 'type', 'url')
    list_filter = ('file', 'type', )
    search_fields = ['id', ]

admin.site.register(models.Page, Page)
