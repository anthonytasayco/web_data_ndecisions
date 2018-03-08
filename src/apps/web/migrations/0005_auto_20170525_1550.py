# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-25 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_somos_texto_redes'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='slug',
            field=models.SlugField(blank=True, max_length=180, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='nombre',
            field=models.CharField(max_length=120, verbose_name='Nombre'),
        ),
    ]
