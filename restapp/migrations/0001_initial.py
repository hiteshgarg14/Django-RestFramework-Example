# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-21 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
    ]
