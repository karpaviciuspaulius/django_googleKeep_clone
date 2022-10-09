import django_filters
from django_filters import DateFilter, CharFilter
from .models import Note

class NoteFilter(django_filters.FilterSet):
    class Meta:
        model = Note
        fields = '__all__'
        exclude = ['content','image','author', 'title', 'date_created', 'categories']
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    start_date = DateFilter(field_name="date_created", lookup_expr='lte')
    content = CharFilter(field_name="content", lookup_expr='icontains')
    