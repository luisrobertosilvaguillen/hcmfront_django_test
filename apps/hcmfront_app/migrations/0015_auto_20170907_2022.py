# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-08 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hcmfront_app', '0014_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.CharField(max_length=255),
        ),
    ]
