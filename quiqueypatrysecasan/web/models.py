from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField


class Comment(models.Model):
    texto         = models.TextField(max_length=140)
    invitado      = models.ForeignKey(User)

    def __unicode__(self):
        return self.texto


class Photo(models.Model):
    image =  CloudinaryField('image')
