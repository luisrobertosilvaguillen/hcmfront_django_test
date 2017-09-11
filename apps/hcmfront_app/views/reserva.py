from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from apps.hcmfront_app.models import Reservation_Request, Reservation, Notification, Supply, Room, Reservation_Priority,Reservation_Status
from apps.hcmfront_app.forms import ReservationForm, ReservationFormEdit
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, View
from django.core.urlresolvers import reverse_lazy
from django.template.loader import render_to_string
from apps.hcmfront_app.rooms_reservation import Rooms_Reservation
import json, datetime

@login_required
def index(request):
	context = {}
	if request.user.groups.filter(pk=1).exists():
		context["eventos"] = Reservation.objects.filter(date__gte = datetime.datetime.now())
	return render(request, "reserva/index.html", context)

class ReservaCreate(LoginRequiredMixin, CreateView):
	model= Reservation
	form_class = ReservationForm
	success_url = reverse_lazy('hcmfront_app:home')

	def dispatch(self, *args, **kwargs):
		if self.request.user.groups.filter(pk=1).exists():
			return 	redirect('hcmfront_app:reservas')
		return super(ReservaCreate, self).dispatch(*args, **kwargs)		

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if not request.POST["rsv"] == "0":
		 	reservation = Reservation.objects.get(pk=request.POST["rsv"])
			dat = reservation.date.strftime('%d/%m/%Y')
			t1 = reservation.hour_from.strftime('%H:%M')
			t2 = reservation.hour_to.strftime('%H:%M')
			priority = Reservation_Priority.objects.get(id = request.POST["priority"])
			msj = ("El usuario "+ request.user.username +" ha solicitado la asignacion de la Reservacion: Sala " + reservation.room.name + ", con fecha " + dat +" de " + t1 + " a " + t2 +". Prioridad: " + priority.name + ".")
			noti = Notification(message=msj, type_noti=2 )
			noti.save()	
		 	rr = Reservation_Request(reservation = reservation, user = request.user, notification=noti)
		 	rr.save()
		else:
			if form.is_valid():
				obj = form.save(commit=False)
				obj.user = request.user
				obj.status = Reservation_Status(id=3)
				obj.save()
				form.save_m2m()						
				
		return HttpResponseRedirect(self.get_success_url())		

@login_required
def reservar(request):
	if request.user.groups.filter(pk=1).exists():
		return 	redirect('hcmfront_app:reservas')

	html = render_to_string('reserva/reserva_form.html')
	return HttpResponse(html)	

@login_required
def reservaformedit(request, pk):
	if not request.user.groups.filter(pk=1).exists():
		return 	redirect('hcmfront_app:home')

	reservation = Reservation.objects.get(pk=pk)

	if request.method == 'POST':
		form = ReservationFormEdit(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = reservation.user
			obj.id = reservation.id
			obj.status = reservation.status
			obj.hour_from = reservation.hour_from
			obj.hour_to = reservation.hour_to
			obj.date = reservation.date
			obj.save()
			form.save_m2m()
		return redirect('hcmfront_app:reservas')	

	priorities = Reservation_Priority.objects.all()
	supplies = Supply.objects.filter(room__id=reservation.room.id)
	context = {'reservation': reservation, 'supplies' : supplies, 'priorities':priorities}
	html = render_to_string('reserva/reserva_formedit.html', request=request, context=context)
	return HttpResponse(html)		

@login_required
def get_salas_reserva(request):	
	if request.user.groups.filter(pk=1).exists():
		return 	HttpResponse()

	rooms_reservation = Rooms_Reservation(request.GET["date"], request.GET["from"], request.GET["to"], request.GET["quantity"]) 
	rooms = rooms_reservation.get_rooms_ordered()
	html = render_to_string('reserva/sala_select.html', {'rooms':rooms}, request=request)
	return HttpResponse(html)

@login_required
def reserva_resume(request):
	if request.user.groups.filter(pk=1).exists():
		return 	HttpResponse('hcmfront_app:reservas')	
	room = Room.objects.get(id=request.GET["room_id"])
	supplies = Supply.objects.filter(room__id=request.GET["room_id"])
	priorities = Reservation_Priority.objects.all()
	reservation = Reservation.objects.filter(pk=request.GET["rsv"]).first()
	if reservation:
		dat = reservation.date.strftime('%Y-%m-%d')
		t1 = reservation.hour_from.strftime('%H:%M')
		t2 = reservation.hour_to.strftime('%H:%M')
		html = render_to_string('reserva/reserva_resume.html', request=request, context= {'rsv':reservation.id,'date':dat,'supplies': supplies,'from': t1,'to': t2,'quantity': request.GET["quantity"], 'room' : room,'priorities':priorities })
	else:
		html = render_to_string('reserva/reserva_resume.html', request=request, context= {'rsv':0,'date':request.GET["date"],'supplies': supplies,'from': request.GET["from"],'to': request.GET["to"],'quantity': request.GET["quantity"], 'room' : room,'priorities':priorities })
	return HttpResponse(html)	

@login_required
def confirm_reservation(request, pk):
	reservation = get_object_or_404(Reservation, pk=pk)
	if not reservation.status.id == 3 or not (reservation.user == request.user or request.user.groups.filter(pk=1).exists()):
		return 	redirect('hcmfront_app:home')

	if request.method == 'POST':
		reservation.status = Reservation_Status(id=4)
		reservation.save()
		return 	redirect('hcmfront_app:home')
	return render(request, "reserva/confirmar.html", {'reservation': reservation})		

@login_required
def reservation_notification(request, pk):
	noti = get_object_or_404(Notification, pk=pk)
	if noti.checked:
		return 	redirect('hcmfront_app:home')
	noti.checked = True
	noti.save()
	return render(request, "reserva/reserva_notification.html", {'notification': noti})	
		

@login_required
def confirm_reservation_request(request, pk):
	reservation_req = Reservation_Request.objects.get(notification__id=pk)
	if not request.user.groups.filter(pk=1).exists():
		return 	redirect('hcmfront_app:home')
	print reservation_req.notification.checked
	if reservation_req.notification.checked:
		return 	redirect('hcmfront_app:reservas')		
		
	if request.method == 'POST':
		noti = Notification.objects.get(id=pk)
		noti.checked = True
		noti.user_check = request.user
		noti.save()

		if request.POST["th"] == "1":
			reservation = Reservation.objects.get(id=reservation_req.reservation.id)
			dat = reservation.date.strftime('%d/%m/%Y')
			t1 = reservation.hour_from.strftime('%H:%M')
			t2 = reservation.hour_to.strftime('%H:%M')
			msj = ("Su Reservacion de la Sala " + reservation.room.name + ", con fecha " + dat +" de " + t1 + " a " + t2 +" ha sido asignada a otro usuario.")
			noti = Notification(user_check=reservation.user, message=msj, type_noti=1 )

			reservation.user = reservation_req.user
			reservation.save()
			noti.save()

		return 	redirect('hcmfront_app:reservas')
	return render(request, "reserva/reserva_request_confirm.html", {'notification': reservation_req.notification})	


@login_required
def reservadelete(request, pk):
	if not request.user.groups.filter(pk=1).exists():
		return 	redirect('hcmfront_app:home')
	reservation = get_object_or_404(Reservation, pk=pk)
	if request.method == 'POST':
		dat = reservation.date.strftime('%d/%m/%Y')
		t1 = reservation.hour_from.strftime('%H:%M')
		t2 = reservation.hour_to.strftime('%H:%M')
		msj = ("Su Reservacion de la Sala " + reservation.room.name + ", con fecha " + dat +" de " + t1 + " a " + t2 +" ha sido eliminada.")
		noti = Notification(user_check=reservation.user, message=msj, type_noti=1 )
		noti.save()
		reservation.delete()
		return 	redirect('hcmfront_app:reservas')
	return render(request, "reserva/reserva_delete.html", {'reservation': reservation})			