# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-18 15:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0012_nepse_difference'),
    ]

    operations = [
        migrations.AddField(
            model_name='nepse',
            name='yesterday_date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2016, 8, 18, 15, 8, 10, 738512, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nepse',
            name='yesterday_price',
            field=models.FloatField(default=0.0),
        ),
    ]