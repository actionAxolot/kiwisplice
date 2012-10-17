# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from models import *


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        exclude = ("user", "slug")


class UserCreateForm(forms.Form):
	username = forms.CharField(max_length=50, label=u"Nombre de usuario", required=True)
	email = forms.EmailField(label=u"Correo electrónico", required=True)
	first_name = forms.CharField(max_length=50, label=u"Nombres", required=True)
	last_name = forms.CharField(max_length=50, label=u"Apellidos", required=True)
	password1 = forms.CharField(max_length=80, widget=forms.PasswordInput(), label=u"Contraseña", required=True)
	password2 = forms.CharField(max_length=80, widget=forms.PasswordInput(), label=u"Confirmar contraseña", required=True)
	role = forms.ModelChoiceField(queryset=Role.objects.all(), label=u"Rol", required=True, empty_label=None)

	def clean_username(self):
		username = self.cleaned_data["username"]
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username

		raise forms.ValidationError("Nombre de usuario ya existe en el sistema")

	def clean_password2(self, *args, **kwargs):
		password1 = self.cleaned_data["password1"]
		password2 = self.cleaned_data["password2"]

		if password1 != password2:
			raise forms.ValidationError("Contraseñas no coinciden")

		return password2


class UserEditForm(forms.Form):
	username = forms.CharField(max_length=50, label=u"Nombre de usuario", required=True)
	email = forms.EmailField(label=u"Correo electrónico", required=True)
	first_name = forms.CharField(max_length=50, label=u"Nombres", required=True)
	last_name = forms.CharField(max_length=50, label=u"Apellidos", required=True)
	role = forms.ModelChoiceField(queryset=Role.objects.all(), label=u"Rol", required=True, empty_label=None)

	def clean_username(self):
		username = self.cleaned_data["username"]
		try:
			temp = User.objects.get(username=username)
		except User.DoesNotExist:
			return username

		if temp.username == username:
			return username
		else:
			raise forms.ValidationError("Nombre de usuario ya existe en el sistema")