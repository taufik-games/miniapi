# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0005_page_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='provider',
            field=models.CharField(max_length=50),
        ),
    ]