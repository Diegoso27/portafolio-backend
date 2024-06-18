from rest_framework import serializers
from mainapp.models import Propiedad, Infante


class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = ['id', 'owner', 'address', 'contact_number', 'infantes', 'asistente']

class InfanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infante
        fields = '__all__'