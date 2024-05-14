from rest_framework import serializers
from django.contrib.auth.models import User
import re

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True,'required': True}
        }

    def save(self):
        password = self.validated_data.get('password')
        password2 = self.validated_data.get('password2')
        if password!= password2:
            raise serializers.ValidationError('Las contraseñas no coinciden')
        
        if User.objects.filter(username=self.validated_data.get('username')).exists():
            raise serializers.ValidationError('El correo electronico ya está registrado')
        
        account = User(email=self.validated_data["email"], username=self.validated_data["username"])
        account.set_password(password)
        account.save()
        return account