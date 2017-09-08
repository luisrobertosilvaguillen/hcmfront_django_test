from models import Room, Reservation, Reservation_Status
from datetime import datetime
from django.db.models import Q
from django.core.serializers import serialize
class Rooms_Reservation():
	"""
		Analiza las salas de reuniones con respecto a una fecha, hora de inicio, hora fin y cantidad de personas
		para una reservacion, con el fin de ordenarlas segun la disponibilidad y capacidad requerida 
		para la reserva 
	"""
	def __init__(self, date, _from, to, quantity = 0):
		self.date = datetime.strptime(date, '%Y-%m-%d')
		self._from = _from
		self.to = to
		self.quantity = quantity
		self.unavailable = []
		self.available = []
		self.reservated = []

	def get_rooms_ordered(self):
		#Obteniendo salas que cumplen con la cantidad de personas requeridas
		scr = Room.objects.filter(capacity=self.quantity)
		#Obteniendo salas que no cumlen con la cantidad de personas requeridas ordenadas de mayor a menor
		sncr = Room.objects.exclude(capacity=self.quantity).order_by('-capacity')
		self.assign(scr)
		self.assign(sncr)

		return self.get_final()
		
	def get_final(self):
		result_list = []
		for ob in self.available:
			result_list.append(ob)
		for ob in self.reservated:
			result_list.append(ob)
		for ob in self.unavailable:
			result_list.append(ob)
		return result_list

	def assign(self, rooms):
		#Definiendo estatus para cada sala segun los parametros recibidos
		for _room in rooms:
			#Verificando reservaciones hechas para esta sala en la fecha y rango de horas recibidos 
			rh = Reservation.objects.filter(date = self.date).filter(room=_room).filter(Q(hour_from__range=(self._from, self.to)) | Q(hour_to__range=(self._from, self.to))).first()
			#Generando Listado Final segun Estatus
			if rh:		
				obj = {'room':_room, 'status':rh.status, 'reservation':rh}
				if rh.status.id == 4:
					self.unavailable.append(obj)
				else:
					self.reservated.append(obj)
			else:
				hour_from = datetime.strptime(self._from, '%H:%M').time()
				hour_to = datetime.strptime(self.to, '%H:%M').time()
				if (hour_from > _room.hour_from and hour_from < _room.hour_to) and (hour_to > _room.hour_from and hour_to < _room.hour_to):
					status = Reservation_Status.objects.get(pk=2)
					obj = {'room':_room, 'status':status, 'reservation':0}
					self.available.append(obj)
				else:
					status = Reservation_Status.objects.get(pk=1)
					obj = {'room':_room, 'status':status, 'reservation':0}
					self.unavailable.append(obj)	



