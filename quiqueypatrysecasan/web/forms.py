from django import forms

from django.contrib.auth.models import User


class UserForm(forms.Form):
    nombre     = forms.CharField()
    apellidos  = forms.CharField()
    email      = forms.EmailField(widget=forms.EmailInput())
    password   = forms.CharField(widget=forms.PasswordInput())
    invitados  = forms.IntegerField(min_value=0, max_value=5)

    class Meta:
        model = User