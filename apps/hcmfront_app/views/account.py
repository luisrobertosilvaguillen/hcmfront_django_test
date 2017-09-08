from django.views.generic import View
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import render
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('hcmfront_app:loginf'))

