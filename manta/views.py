from django.shortcuts import render
from manta.models import *
from manta.serializers import *
from rest_framework import generics, status, viewsets, permissions, serializers
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class PacienteList(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class AvaliacaoList(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

class AvaliacaoDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Avaliacao.objects.all()
    serializer_class = PacienteSerializer


class SensorList(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = DadosSensor.objects.all()
    serializer_class = DadosSensorSerializer

class SensorDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = DadosSensor.objects.all()
    serializer_class = DadosSensorSerializer