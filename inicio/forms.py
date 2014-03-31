# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
#    pass
#cap11 - Si se extiendió el modelo User, se pueden agregar
#        los campos aquí
    telefono = forms.IntegerField()
