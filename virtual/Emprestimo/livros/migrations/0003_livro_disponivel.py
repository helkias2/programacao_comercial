# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_auto_20170503_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
    ]
