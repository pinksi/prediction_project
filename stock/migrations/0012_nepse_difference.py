# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-18 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0011_auto_20160818_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='nepse',
            name='difference',
            field=models.FloatField(default=0.0),
        ),
    ]
