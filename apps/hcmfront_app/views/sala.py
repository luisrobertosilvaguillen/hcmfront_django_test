from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.hcmfront_app.models import Room
from apps.hcmfront_app.forms import RoomForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class RoomList(LoginRequiredMixin, ListView):
	model= Room
	template_name= "sala/index.html"

	def dispatch(self, *args, **kwargs):
		if not self.request.user.groups.filter(pk=1).exists():
			return 	redirect('hcmfront_app:home')
		return super(RoomList, self).dispatch(*args, **kwargs)	

class RoomCreate(LoginRequiredMixin, CreateView):
	model= Room
	form_class = RoomForm
	template_name= "sala/sala_form.html"
	success_url = reverse_lazy('hcmfront_app:salas')

	def dispatch(self, *args, **kwargs):
		if not self.request.user.groups.filter(pk=1).exists():
			return 	redirect('hcmfront_app:home')
		return super(RoomCreate, self).dispatch(*args, **kwargs)	

	def form_invalid(self, form):
		return render(self.request, "sala/sala_form.html", {'form': form, 'showerr': True})

class RoomEdit(LoginRequiredMixin, UpdateView):
	model= Room
	form_class = RoomForm
	template_name= "sala/sala_form.html"
	success_url = reverse_lazy('hcmfront_app:salas')	

	def dispatch(self, *args, **kwargs):
		if not self.request.user.groups.filter(pk=1).exists():
			return 	redirect('hcmfront_app:home')
		return super(RoomEdit, self).dispatch(*args, **kwargs)	

	def form_invalid(self, form):
		return render(self.request, "sala/sala_form.html", {'form': form, 'showerr': True})	

class RoomDelete(LoginRequiredMixin, DeleteView):
	model= Room
	template_name= "sala/sala_delete.html"
	success_url = reverse_lazy('hcmfront_app:salas')	

	def dispatch(self, *args, **kwargs):
		if not self.request.user.groups.filter(pk=1).exists():
			return 	redirect('hcmfront_app:home')
		return super(RoomDelete, self).dispatch(*args, **kwargs)	