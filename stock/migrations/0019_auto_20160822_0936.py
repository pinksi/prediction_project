# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-22 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0018_auto_20160819_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='closing_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='difference',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='predicted_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='previous_closing_price',
            field=models.IntegerField(default=0),
        ),
    ]
