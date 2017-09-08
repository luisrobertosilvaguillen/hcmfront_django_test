from django import forms
from models import Supply, Room, Reservation
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
	group = forms.ModelChoiceField(label=("Grupo"), queryset=Group.objects.all(), error_messages = {'required': 'Seleccione Grupo', } ,empty_label="--SELECCIONE GRUPO--", widget=forms.Select(attrs={'class':'form_control col-xs-10 col-sm-12'}))
	password1 = forms.CharField(label=("Password"),  error_messages = {'required': 'Ingrese Password', }, widget=forms.PasswordInput(attrs={'class':'form_control col-xs-10 col-sm-12', 'id':'password1', 'placeholder':'Ingrese Password', 'name':'password1'}))
	password2 = forms.CharField(label=("Repetir Password"),  error_messages = {'required': 'Repita Password', }, widget=forms.PasswordInput(attrs={'class':'form_control col-xs-10 col-sm-12', 'id':'password2', 'placeholder':'Repetir Password', 'name':'password2'}))
	class Meta:
		model = User
		exclude = []
		fields =(
			'first_name',
			'last_name',
			'username',
			'email',
			'password1',
			'password2',
			'group',
		)
		labels = {
			'first_name': 'Nombre',
			'last_name': 'Apellido',
			'username': 'Usuario',
			'email': 'Email',
		}		
		widgets = {
			'first_name': forms.TextInput(attrs={'class':'form_control col-xs-10 col-sm-12', 'id':'first_name', 'placeholder':'Ingrese el Nombre', 'name':'first_name'}),
			'last_name': forms.TextInput(attrs={'class':'form_control col-xs-10 col-sm-12', 'id':'last_name', 'placeholder':'Ingrese el Apellido', 'name':'last_name'}),
			'username': forms.TextInput(attrs={'class':'form_control col-xs-10 col-sm-12', 'id':'username', 'placeholder':'Ingrese el Nombre de Usuario', 'name':'username'}),
			'email': forms.EmailInput(attrs={'class':'form_control col-xs-10 col-sm-12', 'id':'email', 'placeholder':'Ingrese el Email', 'name':'email'}),
		}				
		error_messages = {
	        'first_name': {'required': 'Ingrese el Nombre',},
	        'last_name': {'required': 'Ingrese el Apellido',},
	        'username': {'required': 'Ingrese el Nombre de Usuario',},
	        'email': {'invalid': 'Formato Email Invalido', 'required': 'Ingrese Email',},
    	}  

class SupplyForm(forms.ModelForm):
	class Meta:
		model = Supply
		fields =(
			'name',
		)
		labels = {
			'name' : 'Nombre',
		}	
		widgets = {
			'name': forms.TextInput(attrs={'class':'form_control col-xs-10 col-sm-5', 'id':'txtname', 'placeholder':'Ingrese el Nombre del Insumo'}),
		}		
		error_messages = {
	        'name': {'required': 'Ingrese el Nombre del Insumo',}
    	}	

class RoomForm(forms.ModelForm):
	class Meta:
		model = Room
		fields = [
			'name',
			'location',
			'capacity',
			'hour_from',
			'hour_to',
			'supply',
		]
		labels = {
			'name' : 'Nombre',
			'location' : 'Ubicacion',
			'capacity' : 'Capacidad',
			'hour_from' : 'Desde',
			'hour_to' : 'Hasta',
			'supply' : 'Insumos',
		}	
		widgets = {
			'name': forms.TextInput(attrs={'required' : 'required','class':'form_control col-xs-10 col-sm-12', 'id':'txtname', 'placeholder':'Ingrese el Nombre de la Sala'}),
			'location': forms.TextInput(attrs={'required' : 'required','class':'form_control col-xs-10 col-sm-12', 'id':'txtlocation', 'placeholder':'Ingrese Ubicacion de la Sala'}),
			'capacity': forms.NumberInput(attrs={'required' : 'required','class':'form_control col-xs-10 col-sm-12', 'id':'txtcapacity', 'placeholder':'Ingrese Capacidad de la Sala'}),
			'hour_from': forms.TimeInput(format='%H:%M', attrs={'required' : 'required','class':'form_control col-xs-10 col-sm-12', 'id':'txthour_from', 'placeholder':'HH:MM'}),
			'hour_to': forms.TimeInput(attrs={'required' : 'required', 'class':'form_control col-xs-10 col-sm-12', 'id':'txthour_to', 'placeholder':'HH:MM'}),
			'supply': forms.CheckboxSelectMultiple(attrs={'class':'ace chk'}),
		}		
		error_messages = {
	        'name': {'required': 'Ingrese el Nombre de la Sala',},
	        'location': {'required': 'Ingrese Ubicacion de la Sala',},
	        'hour_from': {'invalid': 'Formato Hora de Inicio Invalido', 'required': 'Ingrese Hora de Inicio para la Disponibilidad de la Sala',},
	        'hour_to': {'invalid': 'Formato Hora de Inicio Invalido', 'required': 'Ingrese Hora Tope para la Disponibilidad de la Sala',},
	        'capacity': {'invalid': 'Formato Capacidad Invalido', 'required': 'Ingrese la Capacidad',},
	        'supply': {'required': 'Seleccione al menos un insumo',},
    	}				

class ReservationForm(forms.ModelForm):
	class Meta:
		model = Reservation
		# exclude = ['user','status']
		fields = [
			'date',
			'hour_from',
			'hour_to',
			'quantity',
			'supply',
			'room',
			'priority',
		]
		widgets = {
			'date': forms.HiddenInput(attrs={'id':'tdate'}),
			'hour_from': forms.HiddenInput(attrs={'id':'thour_from'}),
			'hour_to': forms.HiddenInput(attrs={'id':'thour_to'}),
			'quantity': forms.HiddenInput(attrs={'id':'tquantity'}),
			'room': forms.HiddenInput(attrs={'id':'troom'}),
			'priority': forms.Select(attrs={'id':'txthour_to'}),
			'supply': forms.CheckboxSelectMultiple(attrs={'class':'ace chk'}),
		}

class ReservationFormEdit(forms.ModelForm):
	class Meta:
		model = Reservation
		# exclude = ['status','hour_from', 'hour_to']
		fields = [
			'quantity',
			'supply',
			'priority',
			'room',
		]
		widgets = {
			'quantity': forms.TextInput(attrs={'id':'tquantity'}),
			'priority': forms.Select(attrs={'id':'txthour_to'}),
			'supply': forms.CheckboxSelectMultiple(attrs={'class':'ace chk'}),
			'room': forms.HiddenInput(attrs={'id':'troom'}),
		}