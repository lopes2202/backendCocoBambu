import django_filters
from .models import LivroFavoritado


class LivroFavoritadoFilter(django_filters.FilterSet):
    tags = django_filters.filters.CharFilter(field_name='tags', method='filter_tags')

    class Meta:
        model = LivroFavoritado
        fields = ['tags']

    def filter_tags(self, queryset, name, value):
        print(value)
        if not value:
            return queryset
        queryset = queryset.filter(tags__nome=value)
        return queryset
