# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-25 23:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20170525_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='mensaje',
        ),
    ]
