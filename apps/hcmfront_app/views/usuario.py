from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User, Group
from apps.hcmfront_app.forms import UserForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class UserList(LoginRequiredMixin, ListView):
	model= User
	template_name= "usuario/index.html"	

	def dispatch(self, *args, **kwargs):
		if not self.request.user.groups.filter(pk=1).exists():
			return 	redirect('hcmfront_app:home')
		return super(UserList, self).dispatch(*args, **kwargs)	

class UserCreate(LoginRequiredMixin, CreateView):
	model= User
	template_name= "usuario/user_form.html"	
	form_class = UserForm
	success_url = reverse_lazy('hcmfront_app:usuarios')

	def dispatch(self, *args, **kwargs):
		if not self.request.user.groups.filter(pk=1).exists():
			return 	redirect('hcmfront_app:home')
		return super(UserCreate, self).dispatch(*args, **kwargs)	

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			g = Group.objects.get(pk = request.POST["group"])
			user = form.save()
			if g.id == 1:
				user.is_staff =True
				user.is_superuser =True		
				user.save()	
			g.user_set.add(user.id)	
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, context= {'showerr': True}))

	def form_invalid(self, form):
		return render(self.request, "usuario/user_form.html", {'form': form, 'showerr': True})	

class UserDelete(LoginRequiredMixin, DeleteView):
	model= User
	template_name= "usuario/user_delete.html"
	success_url = reverse_lazy('hcmfront_app:usuarios')
	
	def dispatch(self, *args, **kwargs):
		if not self.request.user.groups.filter(pk=1).exists():
			return 	redirect('hcmfront_app:home')
		return super(UserDelete, self).dispatch(*args, **kwargs)	