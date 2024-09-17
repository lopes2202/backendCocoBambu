from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
    
class Tag(models.Model):
    usuario = models.ForeignKey(
        get_user_model(),  
        on_delete=models.CASCADE,
        null=True
    )
    nome = models.CharField(max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['usuario', 'nome'], name='unique_tag_name_per_user')
        ]


class LivroFavoritado(models.Model):
    usuario = models.ForeignKey(
        get_user_model(),  
        on_delete=models.CASCADE,
        null=True
    )
    id_google = models.CharField(max_length=100)
    nota = models.IntegerField()
    notas_pessoais = models.TextField()
    tags = models.ManyToManyField(
        Tag,
        blank=True
    )

    def __str__ (self):
        return "{} {} {}".format(self.id_google, self.nota, self.notas_pessoais, self.tags)
