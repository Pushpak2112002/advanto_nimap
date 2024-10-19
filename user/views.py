from django.shortcuts import render
from rest_framework import viewsets
from user.models import user
from user.serializers import companySerializer
from user.models import clients
from user.serializers import companyclints
from user.models import project
from user.serializers import companyproject


###############################################
class compnyViewset(viewsets.ModelViewSet):
    queryset=user.objects.all()
    serializer_class=companySerializer

class clientsViewset(viewsets.ModelViewSet):
    queryset=clients.objects.all()
    serializer_class=companyclints

class projectViewset(viewsets.ModelViewSet):
    queryset=project.objects.all()
    serializer_class=companyproject


