from django import forms
from django.contrib.admin import widgets

class ContactForm(forms.Form):
	Email	= forms.EmailField(widget=forms.TextInput())
	Titulo	= forms.CharField(widget=forms.TextInput())
	Texto	= forms.CharField(widget=forms.Textarea())

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class definirFechaForm(forms.Form):
	fecha_llegada = forms.CharField(widget=forms.TextInput())
	fecha_salida = forms.CharField(widget=forms.TextInput())	

	def __init__(self, *args, **kwargs):
		super(definirFechaForm, self).__init__(*args, **kwargs)
		self.fields['fecha_llegada'].widget = widgets.AdminDateWidget()
		self.fields['fecha_salida'].widget = widgets.AdminDateWidget()
	