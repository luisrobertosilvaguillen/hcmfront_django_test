# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-08 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hcmfront_app', '0015_auto_20170907_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='id_object',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='notification',
            name='type_noti',
            field=models.IntegerField(default=0),
        ),
    ]
