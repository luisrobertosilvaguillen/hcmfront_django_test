# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-06 04:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hcmfront_app', '0011_auto_20170904_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='status',
        ),
    ]