# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-22 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0002_acortar_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acortar',
            name='code',
            field=models.CharField(default='Exde', max_length=15),
        ),
    ]