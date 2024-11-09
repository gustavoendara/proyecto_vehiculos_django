# vehiculo/forms.py
from django import forms
from .models import Vehiculo
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
        


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= get_user_model()
        fields= {'username', 'email'}