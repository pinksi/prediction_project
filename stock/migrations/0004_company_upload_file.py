# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-17 02:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20160816_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='upload_file',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]
