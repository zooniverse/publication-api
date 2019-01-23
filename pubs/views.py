from rest_framework import viewsets

from .models import Publication
from .serializers import PublicationSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.filter(approved=True)
    serializer_class = PublicationSerializer
    filter_fields = ('type',)
