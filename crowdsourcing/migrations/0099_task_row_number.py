# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-15 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0098_auto_20160615_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='row_number',
            field=models.IntegerField(null=True),
        ),
    ]
