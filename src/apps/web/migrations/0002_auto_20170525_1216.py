# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-25 17:16
from __future__ import unicode_literals

from django.db import migrations, models
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seccionservicios',
            options={'verbose_name': 'Sección servicios', 'verbose_name_plural': 'Sección servicios'},
        ),
        migrations.AddField(
            model_name='home',
            name='boton_somos',
            field=models.CharField(blank=True, max_length=300, verbose_name='Título boton somos'),
        ),
        migrations.AlterField(
            model_name='home',
            name='img_somos',
            field=filebrowser.fields.FileBrowseField(blank=True, help_text='Tamaño Recomendado: 585x410', max_length=200, verbose_name='Imagen'),
        ),
    ]
