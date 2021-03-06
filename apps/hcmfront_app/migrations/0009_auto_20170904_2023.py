# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-05 00:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hcmfront_app', '0008_remove_room_room_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hcmfront_app.Reservation_Status'),
        ),
    ]
