# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0002_auto_20170814_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
