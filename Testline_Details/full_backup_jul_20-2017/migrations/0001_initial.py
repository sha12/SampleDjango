# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-26 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testlines',
            fields=[
                ('SBTS_ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Owner', models.CharField(max_length=50)),
                ('Rack', models.CharField(max_length=50)),
                ('Hw_config', models.CharField(max_length=200)),
                ('Radio_modules', models.CharField(default='FXEB+FRGT+FXDB', max_length=200)),
                ('SBTS_Build', models.CharField(max_length=200)),
                ('Setup_config', models.CharField(max_length=200)),
                ('UEs', models.CharField(max_length=200)),
                ('IMSI', models.CharField(max_length=100)),
                ('Calls', models.CharField(max_length=200)),
                ('Issues', models.CharField(max_length=200)),
                ('Investigations', models.CharField(max_length=200)),
                ('Status_Comments', models.TextField()),
                ('lastmodifiedon', models.DateTimeField(default=None, null=True)),
                ('lastmodifiedby', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
    ]