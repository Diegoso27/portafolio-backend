from rest_framework import serializers
from mainapp.models import Propiedad, Infante, Servicios_emergencia


class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = ['id', 'owner', 'address', 'contact_number', 'infantes', 'asistente', 'servicios_emergencia']

class InfanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infante
        fields = '__all__'

class Servicios_emergenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios_emergencia
        fields = '__all__'