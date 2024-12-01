# obras_sociales/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import ObraSocial
from django.http import HttpResponse

def listar_obras_sociales(request):
    obras = ObraSocial.objects.all()
    return render(request, 'obras_sociales/listar.html', {'obras': obras})

def registrar_obra_social(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        codigo = request.POST['codigo']
        ObraSocial.objects.create(nombre=nombre, codigo=codigo)
        return redirect('listar_obras_sociales')
    return render(request, 'obras_sociales/registrar.html')

def eliminar_obra_social(request, obra_id):
    obra = get_object_or_404(ObraSocial, id=obra_id)
    obra.delete()
    return redirect('listar_obras_sociales')
