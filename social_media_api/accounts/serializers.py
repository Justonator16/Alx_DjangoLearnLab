from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

    def create(self, validated_data):
        # Create the user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        
        # Create token for the user
        Token.objects.create(user=user)
        
        return user