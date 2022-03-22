from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Units
from .serializers import UnitsSerializer
import django_filters



class UnitViewSet(viewsets.ModelViewSet):
    queryset = Units.objects.all()
    serializer_class = UnitsSerializer
