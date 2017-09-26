# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField(null=True)),
                ('done', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('changed', models.DateTimeField(auto_now_add=True)),
                ('ranking', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'TODOs',
                'verbose_name': 'TODO',
                'ordering': ('-ranking',),
            },
        ),
    ]