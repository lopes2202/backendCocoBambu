from rest_framework.serializers import ModelSerializer
from .models import LivroFavoritado


class LivroFavoritadoSerializer(ModelSerializer):

    class Meta:
        model = LivroFavoritado
        fields = [
            'id',
            'id_google',
            'nota',
            'notas_pessoais',
            'tags'
        ]

    def create(self, validated_data):
        instance = LivroFavoritado.objects.filter(id_google = validated_data.get('id_google'), usuario=validated_data.get('usuario')).first()
        if instance:
            instance = self.update(instance, validated_data)
        else:
            instance = super().create(validated_data)
        return instance

    def validate(self, data):
        data['usuario'] = self.context.get('request').user
        return data
