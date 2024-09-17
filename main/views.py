from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework

from .models import LivroFavoritado
from .serializers import LivroFavoritadoSerializer
from .filter import LivroFavoritadoFilter

# from django.urls import reverse_lazy
 

class LivroFavoritadoViewSet(ModelViewSet):
    model = LivroFavoritado
    fields = [
        'nota', 'notas_pessoais', 'tags'
    ]
    serializer_class = LivroFavoritadoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = LivroFavoritadoFilter

    def get_queryset(self):
        return LivroFavoritado.objects.filter(usuario=self.request.user)
