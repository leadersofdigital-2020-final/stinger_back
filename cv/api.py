from .models import CV
from rest_framework import viewsets, permissions
from .serializers import CVSerializer


class CVViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CVSerializer
