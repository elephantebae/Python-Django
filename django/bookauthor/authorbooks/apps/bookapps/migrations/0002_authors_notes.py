# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-10 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notes',
            field=models.TextField(default='nothing'),
            preserve_default=False,
        ),
    ]
