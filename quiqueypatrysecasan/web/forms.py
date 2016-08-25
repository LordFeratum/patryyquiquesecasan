from django import forms

from django.contrib.auth.models import User
from web.models import Photo

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UserForm(forms.Form):
    username   = forms.CharField()
    nombre     = forms.CharField()
    apellidos  = forms.CharField()
    email      = forms.EmailField(widget=forms.EmailInput())
    password   = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User


class PhotoForm(forms.ModelForm):
    image = forms.FileField(label=u"Imagen")

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', u'Enviar Imagen'))

    class Meta:
        model = Photo
        fields = '__all__'