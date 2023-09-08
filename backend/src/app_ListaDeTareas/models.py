from django.db import models
from users.models import UserAccount

# Create your models here.
class ListaTareas(models.Model):
    nombreTarea=models.CharField(max_length=255)
    fechaCreacionTarea=models.DateField(auto_now_add=True) #2023-09-05
    idUsario=models.ForeignKey(UserAccount, on_delete=models.CASCADE) #hay que hacer una foranea al Usuario