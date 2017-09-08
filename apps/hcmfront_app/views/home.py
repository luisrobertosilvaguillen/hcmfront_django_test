from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.hcmfront_app.models import Reservation, Supply
from django.core.urlresolvers import reverse_lazy
from datetime import datetime
@login_required
def index(request):
	if request.user.groups.filter(pk=1).exists():
		return 	redirect('hcmfront_app:reservas')	

	reservations = Reservation.objects.filter(user = request.user, date__gte = datetime.now())
	context = {'reservations':reservations}
	return render(request, "home/index.html", context)
