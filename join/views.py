from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .models import Task, Contact
from .serializers import TaskSerializer, UserRegistrationSerializer, LoginSerializer, ContactSerializer


@api_view(["GET", "POST", "DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def task_list(request):
    if request.method == "GET":
        # Finde den Contact, der dem eingeloggten User zugeordnet ist
        user_contact = Contact.objects.filter(user=request.user)
        tasks = Task.objects.filter(assigned_to__in=user_contact)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = request.data.copy()

        # Hier nimmst du die IDs der Contacts aus den übermittelten Daten
        assigned_to_ids = data.get("assigned_to", [])
        if not isinstance(assigned_to_ids, list):
            assigned_to_ids = [assigned_to_ids]
        
        # Entferne 'assigned_to' aus den Daten, da du es später separat handhabst
        data.pop("assigned_to", None)

        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            task = serializer.save()
            
            # Setze hier die Contacts, basierend auf den übermittelten IDs
            if assigned_to_ids:
                task.assigned_to.set(Contact.objects.filter(id__in=assigned_to_ids))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {"user_id": user.pk, "email": user.email, "token": token.key},
            status=status.HTTP_201_CREATED,
        )
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def contacts_list(request):
    if request.method == "GET":
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def contact_detail(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
