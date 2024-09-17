from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


    
class LivroFavoritado(models.Model):
    usuario = models.ForeignKey(
        get_user_model(),  
        on_delete=models.CASCADE,
        null=True
    )
    id_google = models.CharField(max_length=100)
    nota = models.IntegerField()
    notas_pessoais = models.TextField()
    tags = models.JSONField()

    

    def __str__ (self):
        return "{} {} {}".format(self.id_google, self.nota, self.notas_pessoais, self.tags)
