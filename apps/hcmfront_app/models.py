from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q
from datetime import  date
import datetime

from django.db.models import Lookup



class Supply(models.Model):
	name =  models.CharField(max_length=80, default='', blank=False)
	def __unicode__(self):
		return '{}'.format(self.name)
	
class Room(models.Model):
	name =  models.CharField(max_length=80, default='')
	location =  models.CharField(max_length=255, default='')
	capacity =  models.IntegerField(default=0)
	hour_from = models.TimeField()
	hour_to = models.TimeField()
	supply = models.ManyToManyField(Supply)
	def __unicode__(self):
		return '{}'.format(self.name)
	
	def clean(self):
		if self.capacity < 2:
			raise ValidationError("La capacidad debe ser mayor a 1")

class Reservation_Priority(models.Model):
	name =  models.CharField(max_length=20, default='', blank=False)
	def __unicode__(self):
		return '{}'.format(self.name)

class Reservation_Status(models.Model):
	name =  models.CharField(max_length=80, default='')
	allow_request = models.BooleanField(default=False)
	def __unicode__(self):
		return '{}'.format(self.name)

class Reservation(models.Model):
	date = models.DateField()
	hour_from = models.TimeField()
	hour_to = models.TimeField()
	quantity =  models.IntegerField(default=0)
	supply = models.ManyToManyField(Supply)
	room = models.ForeignKey(Room, default = None, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.ForeignKey(Reservation_Status,default = None, on_delete=models.CASCADE)
	priority = models.ForeignKey(Reservation_Priority, default = None, on_delete=models.CASCADE)

	def __unicode__(self):
		return '{} {} {}'.format(self.room.name, self.date, self.user.username)

	def clean(self):
		if self.quantity <= 1:
			raise ValidationError('La capacidad debe ser mayor a 1')

		rh = Reservation.objects.filter(date = self.date, room__id=self.room.id)#.filter(Q(hour_from__range=(self.hour_from, self.hour_to)) | Q(hour_to__range=(self.hour_from, self.hour_to))).first()
		isValid = True 
		for rs in rh:
			if self.time_in_range(rs.hour_from, rs.hour_to, self.hour_from) or self.time_in_range(rs.hour_from, rs.hour_to, self.hour_to) :
				isValid = False
				res = rs

		if not isValid:		
			raise ValidationError({'room': ['Hay una reservacion para la sala '+ res.room.name+' de '+res.hour_from.strftime('%H:%M')+' a '+ res.hour_to.strftime('%H:%M'),]})
		
		if not ((self.hour_from > self.room.hour_from and self.hour_from < self.room.hour_to) and (self.hour_to > self.room.hour_from and self.hour_to < self.room.hour_to)):
			raise ValidationError({'room': ['Sala no disponible.',]})

	def time_in_range(self, start, end, x):
	    """Return true if x is in the range [start, end]"""
	    if start <= end:
	        return start <= x <= end
	    else:
	        return start <= x or x <= end
		
		# if rh:
		# 	if not rh.id == self.id:
		# 		raise ValidationError({'room': ['Hay una reservacion para la sala '+ rh.room.name+' de '+rh.hour_from.strftime('%H:%M')+' a '+ rh.hour_to.strftime('%H:%M'),]})
		
		# if not ((self.hour_from > self.room.hour_from and self.hour_from < self.room.hour_to) and (self.hour_to > self.room.hour_from and self.hour_to < self.room.hour_to)):
		# 	raise ValidationError({'room': ['Sala no disponible.',]})


"""
	field: type_noti
		Define el tipo de notificacion
	___________________________________________________
	tipo 1: Notificar un msj 
	tipo 2: Notificar un msj y tomar una decision (Solicitud de Sala Reservada [solo admins])

"""
class Notification(models.Model):
	user_check = models.ForeignKey(User, default=None,null = True, on_delete=models.CASCADE)
	checked = models.BooleanField(default=False)
	message = models.CharField(max_length=255)	
	type_noti =  models.IntegerField(default=0) 

class Reservation_Request(models.Model):	
	reservation = models.ForeignKey(Reservation, null = True, on_delete=models.CASCADE)
	notification = models.ForeignKey(Notification, null = True, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	aproved = models.BooleanField(default=False)


