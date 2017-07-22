# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('uname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('pic', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('uname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('pic', models.FileField(upload_to='')),
            ],
        ),
    ]
