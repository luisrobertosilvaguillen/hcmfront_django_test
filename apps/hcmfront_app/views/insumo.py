from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from apps.hcmfront_app.forms import SupplyForm
from apps.hcmfront_app.models import Supply
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	if not request.user.groups.filter(pk=1).exists():
		return 	redirect('hcmfront_app:home')

	supplies = Supply.objects.all()
	context = {'supplies':supplies}
	return render(request, "insumo/index.html", context)

@login_required
def supply_new(request):
	if not request.user.groups.filter(pk=1).exists():
		return 	redirect('hcmfront_app:home')

	showerr = False
	if request.method == 'POST':
		form = SupplyForm(request.POST)
		if form.is_valid():
			form.save()
			return 	redirect('hcmfront_app:insumos')
		else:
			showerr = True
	else:
		form = SupplyForm()

	return render(request, "insumo/insumo_form.html", {'form': form, 'showerr': showerr})

@login_required
def supply_edit(request, pk):
	if not request.user.groups.filter(pk=1).exists():
		return 	redirect('hcmfront_app:home')

	supply = get_object_or_404(Supply, pk=pk) 
	if supply.id == 1 or supply.id == 2:
		return 	redirect('hcmfront_app:insumos')
	showerr = False
	if request.method == 'GET':
		form = SupplyForm(instance=supply)
	else:
		form = SupplyForm(request.POST, instance=supply)
		if form.is_valid():
			form.save()
			return 	redirect('hcmfront_app:insumos')
		else:
			showerr = True	
	return render(request, "insumo/insumo_form.html", {'form': form, 'showerr': showerr})	

@login_required
def supply_delete(request, pk):
	if not request.user.groups.filter(pk=1).exists():
		return 	redirect('hcmfront_app:home')
			
	supply = get_object_or_404(Supply, pk=pk) 
	if supply.id == 1 or supply.id == 2:
		return 	redirect('hcmfront_app:insumos')	
	if request.method == 'POST':
		supply.delete()
		return 	redirect('hcmfront_app:insumos')
	return render(request, "insumo/insumo_delete.html", {'supply': supply})	
