# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 04:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='coursecontent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_sub_id', models.IntegerField(default=0)),
                ('content_name', models.CharField(max_length=50)),
                ('content_description', models.CharField(default='description', max_length=500)),
                ('content_type', models.CharField(default='null', max_length=10)),
                ('content_url', models.FileField(default='abc.mp4', upload_to='')),
                ('content_sequence_no', models.IntegerField(default=-1)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='course_pic',
            field=models.FileField(default='abc.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.CharField(max_length=12),
        ),
        migrations.AddField(
            model_name='coursecontent',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructor.course'),
        ),
    ]