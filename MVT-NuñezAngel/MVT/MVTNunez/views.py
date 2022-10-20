from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiar
# Create your views here.

def familiar(request, nombre, edad, nacimiento):
    familiar = Familiar(nombre=nombre, edad=edad, nacimiento=nacimiento)
    familiar.save()

    return HttpResponse(f"""
        <p>Familiar: {familiar.nombre} - Edad: {familiar.edad} -Fecha de nacimiento: {familiar.nacimiento} agregado! <p>
        """)

def familiares(request):
    lista=Familiar.objects.all()
    return render(request, "familiares.html", {"familiares": lista})