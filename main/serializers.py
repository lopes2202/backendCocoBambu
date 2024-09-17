from rest_framework.serializers import ModelSerializer
from .models import LivroFavoritado, Tag



class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['nome']

    def create(self, validated_data):
        return Tag.objects.get_or_create(usuario=validated_data.get('usuario'), nome=validated_data.get('nome'))

    def validate(self, data):
        data['usuario'] = self.context.get('request').user
        return data


class LivroFavoritadoSerializer(ModelSerializer):
    tags = TagSerializer(many=True)

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
        tags = validated_data.pop('tags')
        tags_serializer = TagSerializer(data=tags, many=True, context=self.context)
        tags_serializer.is_valid(raise_exception=True)
        created_tags = tags_serializer.save()

        if instance:
            instance = super().update(instance, validated_data)
        else:
            instance = super().create(validated_data)
        instance.tags.set([tag[0] for tag in created_tags])
        return instance

    def validate(self, data):
        data['usuario'] = self.context.get('request').user
        return data
