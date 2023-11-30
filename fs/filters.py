# filters.py
import django_filters
from .models import FileInfo

class FileInfoFilter(django_filters.FilterSet):
    class Meta:
        model = FileInfo
        fields = ['FileType', 'ActiveStatus', 'RelatedOffice']
