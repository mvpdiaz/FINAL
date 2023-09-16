from django.db import models
from users.models import UserAccount
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class ListaTareas(models.Model):
    nombreTarea=models.CharField(max_length=255)
    fechaCreacionTarea=models.DateField(auto_now_add=True) #2023-09-05
    idUsuario=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #hay que hacer una foranea al Usuario

class Tarea(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion