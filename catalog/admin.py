from django.contrib import admin
from . import models


class Category(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(models.Category, Category)


class Provider(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(models.Provider, Provider)


class Brand(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(models.Brand, Brand)


class Product(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(models.Product, Product)

