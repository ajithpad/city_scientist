# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0004_changed_my_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
