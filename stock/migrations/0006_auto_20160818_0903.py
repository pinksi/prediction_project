# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-18 09:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_company_upload_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='upload_file',
        ),
        migrations.RemoveField(
            model_name='company',
            name='upload_path',
        ),
    ]
