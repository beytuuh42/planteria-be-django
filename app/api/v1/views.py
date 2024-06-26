import os
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ...models import Plant, User
from .serializers import PlantSerializer, UserSerializer
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

@api_view(['GET', 'POST'])
def plant_list(request):
    if request.method == 'GET':
        queryset = Plant.objects.all()
        serializer = PlantSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PlantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def plant_detail(request, id):
    plant = get_object_or_404(Plant, pk=id)
    if request.method == 'GET':
        serializer = PlantSerializer(plant)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PlantSerializer(plant, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'DELETE':
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
   
   
@api_view(['POST'])
def login(request):
    email = request.data['email']
    password = request.data['password']
    
    user = User.objects.filter(email=email).first()
    
    if user is None or not user.check_password(password):
        raise AuthenticationFailed('Wrong credentials!', status.HTTP_401_UNAUTHORIZED)
    
    now = datetime.datetime.now(datetime.timezone.utc)
    
    data = {
        'id': user.id,
        'exp': now + datetime.timedelta(minutes=60),
        'iat': now
    }
    
    token = jwt.encode(data, os.getenv('DJANGO_JWT_SECRET'), algorithm='HS256')
    
    res = Response()
    res.data = {
        'jwt': token
    }
    res.set_cookie(key='jwt', value=token, httponly=True)
    res.status_code = status.HTTP_200_OK
    

    return res


@api_view(['GET'])
def user(request):
    token = request.COOKIES.get('jwt')
    
    if not token:
        raise AuthenticationFailed('Unauthenticated!')
    
    try:
        data = jwt.decode(token, os.getenv('DJANGO_JWT_SECRET'), algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Expired token!')
    
    user = User.objects.filter(id=data['id']).first()
    
    serializer = UserSerializer(user)
    
    res = Response(serializer.data, status=status.HTTP_200_OK)

    return res

@api_view(['POST'])
def logout(request):
    res = Response()
    res.delete_cookie('jwt')
    res.data = {
        'message': 'success'
    }
    return res