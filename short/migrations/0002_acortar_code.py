# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-22 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acortar',
            name='code',
            field=models.CharField(default='ggg', max_length=15, unique=True),
            preserve_default=False,
        ),
    ]