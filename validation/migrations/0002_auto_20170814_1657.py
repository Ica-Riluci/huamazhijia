# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='classx',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='emailadd',
            field=models.CharField(default='thss15_weiyh@163.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.IntegerField(default='6'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='pphone',
            field=models.CharField(default='13719341305', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='school',
            field=models.CharField(default='广州市第六中学', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='sphone',
            field=models.CharField(default='13719165905', max_length=20),
            preserve_default=False,
        ),
    ]
