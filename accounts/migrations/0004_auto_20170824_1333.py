# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170823_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact_no',
            field=models.IntegerField(default=12345, unique=True),
            preserve_default=False,
        ),
    ]
