from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    texto         = models.TextField(max_length=140)
    invitado      = models.ForeignKey(User)
    acompaniantes = models.IntegerField()

    def __unicode__(self):
        return self.texto


class Photo(models.Model):
    imagen   = models.ImageField(upload_to='images/user_img', null=False)
    invitado = models.ForeignKey(User)