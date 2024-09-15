from rest_framework.viewsets import ModelViewSet
from .models import LivroFavoritado
from rest_framework.permissions import IsAuthenticated

# from django.urls import reverse_lazy
 

class LivroFavoritadoViewSet(ModelViewSet):
    model = LivroFavoritado
    fields = [
        'nota', 'notas_pessoais', 'tags'
    ]

    def get_queryset(self):
        return LivroFavoritado.objects.filter(usuario=self.request.user)
    
    permission_classes = [IsAuthenticated]

