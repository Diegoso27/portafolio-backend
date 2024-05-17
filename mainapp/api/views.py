from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from mainapp.models import Propiedad
from rest_framework import status
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registrar_propiedad(request):
    

    if request.method == 'POST':
        owner = request.data.get('owner')
        address = request.data.get('address')
        contact_number = request.data.get('contactNumber')

        print(request.user)

        propiedad_creada = Propiedad.objects.create(
            owner = owner,
            address = address,
            contact_number = contact_number
        )
        return Response(status=status.HTTP_201_CREATED)

    
    return Response(status=status.HTTP_401_UNAUTHORIZED)
