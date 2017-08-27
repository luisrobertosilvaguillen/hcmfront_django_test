# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-27 10:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hcmfront_app', '0002_auto_20170826_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('hour_from', models.TimeField()),
                ('hour_to', models.TimeField()),
                ('quantity', models.IntegerField(default=0)),
                ('supply', models.ManyToManyField(to='hcmfront_app.Supply')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=80)),
                ('allow_request', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='room_status',
            field=models.ManyToManyField(to='hcmfront_app.Room_Status'),
        ),
    ]