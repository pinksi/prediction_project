# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-19 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0017_remove_date_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Date',
        ),
    ]