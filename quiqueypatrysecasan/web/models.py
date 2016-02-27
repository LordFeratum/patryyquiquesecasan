from django.db import models
from django.contrib.auth.models import User


class Comentario(models.Model):
    texto    = models.TextField(max_length=140)
    invitado = models.ForeignKey(User)

    def __str__(self):
        return self.texto


class Photos(models.Model):
    imagen   = models.ImageField(upload_to='images/user_img', null=False)
    invitado = models.ForeignKey(User)