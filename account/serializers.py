from rest_framework import serializers
from .models import CustomUser,Review
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
        
class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email','user_type', 'password', 'confirm_password','country']
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        email = self.validated_data['email']
        country = self.validated_data['country']
        user_type = self.validated_data['user_type']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        
        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Mactched"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists"})
        account = User(username = username, email=email, first_name = first_name, country = country, user_type = user_type )
        account.set_password(password)
        account.is_active = False
        account.save()
        return account

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','email','user_type','country','image','about_me']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'country', 'image', 'about_me']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['reviewer','freelancer','body','rating']
        
   