# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 09:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0005_student_gender'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
