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
        fields = ['firstname', 'lastname']  
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'color']


class TaskSerializer(serializers.ModelSerializer):
    assignedTo = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True, allow_null=True
    )

    class Meta:
        model = Task
        fields = "__all__"
        extra_kwargs = {
            'category': {'read_only': True},
        }

    def get_assignedTo(self, obj):
        # Diese Methode gibt die Namen der zugeordneten Kontakte in der gewünschten Form zurück
        return [f"{contact.firstname} {contact.lastname}" for contact in obj.assignedTo.all()]
    
    def get_category(self, obj):
        return obj.category.name if obj.category else None