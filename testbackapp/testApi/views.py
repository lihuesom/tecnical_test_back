from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Client
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt #Omitiendo CSRF para agilizar desarrollo (esta es una app de pruebas tecnicas)
import json
from datetime import date
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.authtoken.models import Token

# Create your views here.

@method_decorator(csrf_exempt)
def login(request):
        # obtener el username y la contraseña del request.POST
        jd = json.loads(request.body)
        identification =jd['identification']
        password = jd['password']

         # buscar el cliente en la base de datos
        try:
            client = Client.objects.get(identification=identification)
            hashed_password = client.password
        except Client.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'El usuario no existe'}, status=status.HTTP_401_UNAUTHORIZED)

        # comprobar la contraseña
        if not client.check_password(password,hashed_password):
            return JsonResponse({'success': False, 'message': 'Contraseña inválidos.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # token = Token.objects.get_or_create(user=client) pendiente generar token
        return JsonResponse({'success': True, 'message': 'LogIn'}, status=status.HTTP_200_OK
)

def getClient(request):
        clients = list(Client.objects.values())
        if len(clients)> 0:
            response = {"message":'Success','clients':clients}
        else:
            response = {"message":'Clients not found ...'}

        return JsonResponse(response)

@method_decorator(csrf_exempt)
def createClient(request):
     
     jd = json.loads(request.body)
     Client.objects.create(
         name = jd['name'],
         identification = jd['identification'],
         password = make_password(jd['password']),
         created = date.today().strftime("%d/%m/%Y")
         )
     
     return JsonResponse({"message":'Success'})


@method_decorator(csrf_exempt)
def updateClient(request,id):
    response = {"message":'test'}
    return JsonResponse(response)

@method_decorator(csrf_exempt)
def deleteClient(request,id):
    response = {"message":id}
    return JsonResponse(response)

def getOffer(request):
    response = {"message":'test'}
    return JsonResponse(response)

@method_decorator(csrf_exempt)
def updateOffer(request):
    response = {"message":'test'}
    return JsonResponse(response)

@method_decorator(csrf_exempt)
def createOffer(request):
    response = {"message":'test'}
    return JsonResponse(response)

@method_decorator(csrf_exempt)
def deleteOffer(request):
    response = {"message":'test'}
    return JsonResponse(response)

def getAgreement(request):
    response = {"message":'test'}
    return JsonResponse(response)

@method_decorator(csrf_exempt)
def updateAgreement(request):
    response = {"message":'test'}
    return JsonResponse(response)

@method_decorator(csrf_exempt)
def createAgreement(request):
    response = {"message":'test'}
    return JsonResponse(response)

@method_decorator(csrf_exempt)
def deleteAgreement(request):
    response = {"message":'test'}
    return JsonResponse(response)