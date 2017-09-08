from django import template
from django.contrib.auth.models import Group 
from apps.hcmfront_app.models import Reservation, Supply, Notification
from datetime import date,datetime
register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name):
    group =  Group.objects.get(name=group_name) 
    return group in user.groups.all() 

@register.filter(name='can_confirm') 
def can_confirm(reservation_id):
	reservation = Reservation.objects.get(pk=reservation_id)
	if reservation.status.id == 4:
		return False	
	if reservation.priority.id == 1:
		return True
	else:
		_date = datetime.combine(reservation.date, reservation.hour_from)
		_datenow =  datetime.now()
		if _date > _datenow:
			rango = _date - _datenow
			if rango.seconds > (3600 * 8):
				return False
			else:
				return True	
		else:
			return False

@register.filter(name='has_supply') 
def has_supply(reservation, supply_id):
	supplies = Supply.objects.filter(reservation__id=reservation.id)
	for sup in supplies:
		if sup.id == supply_id:
			return True
	return False
   
@register.inclusion_tag("base/noti.html", takes_context=True) 
def noti(context):
	if context.request.user.groups.filter(pk=1).exists():
		va = Notification.objects.filter(checked = False).filter(user_check__isnull=True)
		print va
		return {'notis': va }
	else:
		va = Notification.objects.filter(checked = False, user_check = context.request.user)
		print va
		return {'notis': va }

@register.simple_tag(name='noticount',takes_context=True) 
def noticount(context):
	if context.request.user.groups.filter(pk=1).exists():
		return Notification.objects.filter(checked = False).filter(user_check__isnull=True).count()
	else:
		return Notification.objects.filter(checked = False, user_check = context.request.user).count()


    