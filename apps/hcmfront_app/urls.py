from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import RedirectView
from views.account import LogoutView  
from views.reserva import index as  ireserva, reservation_notification, confirm_reservation_request,reservadelete, reservaformedit, reservar, get_salas_reserva, reserva_resume, ReservaCreate, confirm_reservation
from django.contrib.auth.decorators import permission_required
from views.home import index as ihome
from views.sala import RoomList, RoomCreate, RoomEdit, RoomDelete
from views.insumo import index as iinsumo, supply_new, supply_edit, supply_delete
from views.usuario import UserList, UserCreate, UserDelete
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^accounts/login/$', login, {'template_name' : 'accounts/login.html'}, name='loginf'),
    url(r'^accounts/logout/$', LogoutView.as_view(), name="logout"),
    url(r'^reserva$', ireserva, name="reservas"),
    url(r'^reserva/confirm/(?P<pk>\d+)$', confirm_reservation, name="confirm_reservation"),
    url(r'^reserva/request/(?P<pk>\d+)$', confirm_reservation_request, name="confirm_reservation_request"),
    url(r'^reserva/delete/(?P<pk>\d+)$', reservadelete, name="reservadelete"),
    url(r'^reserva/reservaformedit/(?P<pk>\d+)$', reservaformedit, name="reservaformedit"),
    url(r'^reserva/reservation_notification/(?P<pk>\d+)$', reservation_notification, name="reservation_notification"),
    url(r'^reservaform$', reservar, name="reservaform"),
    url(r'^reservasave$', ReservaCreate.as_view(), name="reservasave"),
    url(r'^get_salas_reserva$', get_salas_reserva, name="get_salas_reserva"),
    url(r'^reserva_resume$', reserva_resume, name="reserva_resume"),
    url(r'^$',  ihome, name="home"),
    url(r'^sala$', RoomList.as_view(), name="salas"),
    url(r'^sala/administrar$', RoomCreate.as_view(), name="sala_administrar"),
    url(r'^sala/administrar/(?P<pk>\d+)$', RoomEdit.as_view(), name="sala_administrar_edit"),
    url(r'^sala/eliminar/(?P<pk>\d+)$', RoomDelete.as_view(), name="sala_administrar_delete"),    
    url(r'^insumo$', iinsumo, name="insumos"),
    url(r'^insumo/administrar$', supply_new, name="insumos_administrar"),
    url(r'^insumo/administrar/(?P<pk>\d+)$', supply_edit, name="insumos_administrar_edit"),
    url(r'^insumo/eliminar/(?P<pk>\d+)$', supply_delete, name="insumos_administrar_delete"),
    url(r'^usuario$', UserList.as_view(), name="usuarios"),
    url(r'^usuario/administrar$', UserCreate.as_view(), name="usuario_administrar"),
    url(r'^usuario/eliminar/(?P<pk>\d+)$', UserDelete.as_view(), name="usuario_administrar_delete"),
]
