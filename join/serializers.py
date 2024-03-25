from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Task, Contact, Category




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        required=True, style={"input_type": "password"}, write_only=True
    )

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid login credentials")
        return user


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}
        
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Invalid register. Email exists already.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
class ContactNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['firstname', 'lastname']  # Anzeigen von Vor- und Nachnamen

class CategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']  # Anzeigen des Kategorienamens


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = ContactNameSerializer(many=True, read_only=True)
    category = CategoryNameSerializer(read_only=True)
    class Meta:
        model = Task
        fields = "__all__"
