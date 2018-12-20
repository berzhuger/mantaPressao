import datetime

from manta.models import *

from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paciente
        fields = '__all__'
    
class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avaliacao
        fields = '__all__'
    
class DadosSensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = DadosSensor
        fields = '__all__'
    