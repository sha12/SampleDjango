# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 07:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Testline_Details', '0008_auto_20161121_1853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testlines',
            old_name='Investigations',
            new_name='Issues_Investigations',
        ),
        migrations.RemoveField(
            model_name='testlines',
            name='Issues',
        ),
    ]
