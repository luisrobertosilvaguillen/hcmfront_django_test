# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-08 04:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hcmfront_app', '0019_auto_20170908_0033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='id_object',
        ),
        migrations.AlterField(
            model_name='notification',
            name='user_check',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
