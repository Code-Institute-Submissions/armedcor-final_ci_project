# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-09-08 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(max_length=50),
        ),
    ]
