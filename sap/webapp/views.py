from django.shortcuts import render
from django.http import HttpResponse
from personas.models import Persona

def sap(request):
    no_personas_var = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id') #Para ordenar de forma descendente es: persona.objects.order_by('-id')
    return render(request, 'bienvenido.html', {'no_personas':no_personas_var, 'personas': personas})

def inicio(request):
    return HttpResponse('Este es el inicio.')