# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 04:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacao', '0003_auto_20170517_0056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitacao',
            old_name='livros_solicitados',
            new_name='livro_solicitado',
        ),
    ]
