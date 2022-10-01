from rest_framework import viewsets, parsers
from .models import Storage
from .serializers import StorageSerializer

class StorageViewset(viewsets.ModelViewSet):

    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']