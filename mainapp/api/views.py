from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from mainapp.models import Propiedad, Infante
from rest_framework import status
from rest_framework.response import Response
from .serializers import InfanteSerializer, PropiedadSerializer






@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detalle_infante(request, infante_id):

    infante = get_object_or_404(Infante, id=infante_id)
    serializer = InfanteSerializer(infante)
    return Response(serializer.data, status=status.HTTP_200_OK)






@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registrar_infante(request, propiedad_id):

    if request.method == 'POST':
        child_name = request.data.get('childName')
        age = request.data.get('age')
        rut = request.data.get('rut')
        diagnostic = request.data.get('diagnostic')
        blood_type = request.data.get('bloodType')
        prevision = request.data.get('prevision')
        alergias = request.data.get('alergias')
        antecendetes_medicos = request.data.get('antecendetesMedicos')

        nuevo_infante = Infante.objects.create(
            child_name = child_name,
            age = age,
            rut = rut,
            diagnostic = diagnostic,
            blood_type = blood_type,
            prevision = prevision,
            alergias = alergias,
            antecendetes_medicos = antecendetes_medicos
        )
        propiedad = get_object_or_404(Propiedad, id=propiedad_id)
        propiedad.infantes.add(nuevo_infante)

    return Response(status=status.HTTP_201_CREATED)





@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registrar_propiedad(request):
    

    if request.method == 'POST':
        owner = request.data.get('owner')
        address = request.data.get('address')
        contact_number = request.data.get('contactNumber')
        asistente = request.user
        print(asistente)

        print(request.user)

        propiedad_creada = Propiedad.objects.create(
            owner = owner,
            address = address,
            contact_number = contact_number
        )

        propiedad_creada.asistente.add(asistente)

        return Response(status=status.HTTP_201_CREATED)

    
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_infantes(request, propiedad_id):
    propiedad = get_object_or_404(Propiedad, id=propiedad_id)
    infantes = propiedad.infantes.all() 
    serializer = InfanteSerializer(infantes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_propiedades(request):
    user = request.user
    propiedades = Propiedad.objects.filter(asistente=user)
    serializer = PropiedadSerializer(propiedades, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def datos_user(request):
    user = request.user.username
    return Response(user, status=status.HTTP_200_OK)
