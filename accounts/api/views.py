from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.api.serializers import RegisterSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def session_view(request):
    if request.method == 'GET':
        user = request.user
        account = User.objects.get(username=user.username)
        
        data = {}
        
        if account is not None:
            data['response'] = 'El usuario ha sido iniciado'
            data['username'] = account.username
            data['email'] = account.email
            refresh = RefreshToken.for_user(account)
            data['token'] = {
               'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            return Response(data)
        
        else:   
            return Response(status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializers = RegisterSerializer(data = request.data.get('user', None))
        data = {}
        if serializers.is_valid():
            account = serializers.save()
            data['response'] = 'El registro del usuario ha sido exitoso'
            data['username'] = account.username
            data['email'] = account.email
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializers.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


