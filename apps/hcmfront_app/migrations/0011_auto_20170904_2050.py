# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-05 00:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hcmfront_app', '0010_auto_20170904_2028'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Room_Status',
            new_name='Reservation_Status',
        ),
        migrations.AddField(
            model_name='reservation',
            name='priority',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hcmfront_app.Reservation_Priority'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hcmfront_app.Reservation_Priority'),
        ),
    ]
