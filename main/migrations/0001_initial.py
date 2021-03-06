# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 16:44
from __future__ import unicode_literals

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InspectionUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_email', models.EmailField(max_length=254)),
                ('inspection_file', models.FileField(upload_to=main.models.get_upload_path)),
            ],
        ),
    ]
