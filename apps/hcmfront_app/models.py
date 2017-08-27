from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Supply(models.Model):
	name =  models.CharField(max_length=80, default='')

class Room_Status(models.Model):
	name =  models.CharField(max_length=80, default='')
	allow_request = models.BooleanField(default=False)

class Room(models.Model):
	name =  models.CharField(max_length=80, default='')
	location =  models.CharField(max_length=255, default='')
	capacity =  models.IntegerField(default=0)
	hour_from = models.TimeField()
	hour_to = models.TimeField()
	supply = models.ManyToManyField(Supply)
	room_status = models.ManyToManyField(Room_Status)

class Reservation(models.Model):
	date = models.DateField()
	hour_from = models.TimeField()
	hour_to = models.TimeField()
	quantity =  models.IntegerField(default=0)
	supply = models.ManyToManyField(Supply)
	user = models.OneToOneField(User, on_delete=models.CASCADE)





