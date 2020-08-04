from django.shortcuts import render
from django.http import	 HttpResponse
from gestion_fechas.models import Fechas
from datetime import datetime

# Create your views here.

def inicio(request):

    return render(request, 'crud.html')


def create(request):

    return render(request, 'crear.html')

def c(request):

    if request.GET['nombre'] and request.GET['fecha']:

        nombre = request.GET['nombre']
        fecha = request.GET['fecha']
        try:
            datetime.strptime(fecha, '%Y-%m-%d')
        except ValueError:
            mensaje = '<h2>Ingrese formato de fecha valido</h2>'
            return HttpResponse(mensaje)
        new = Fechas(nombre = nombre, fecha_nacimiento = fecha)
        new.save()

        return render(request,'c.html') 
    
    else:
        mensaje = '<h2>Por favor complete ambos campos</h2>'

        return HttpResponse(mensaje)

    
def leer(request):  

    return render(request,'leer.html')

def l(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']
        nombre = Fechas.objects.filter(nombre__contains = nombre).values('nombre') 
        fecha = Fechas.objects.filter(nombre__contains = nombre).values('fecha_nacimiento')    
        if Fechas.objects.filter(nombre__contains = nombre):

            return render(request,'l.html', {'fecha_nacimiento':fecha,'nombre':nombre,'cod':1})
        
        else: 

            mensaje = '<h2>No existe el dato, por favor ingrese uno válido</h2>'

            return HttpResponse(mensaje)

        return render(request,'l.html', {'fecha_nacimiento':fecha,'nombre':nombre,'cod':0}) 
    
    elif request.GET['id']:

        id = request.GET['id']
        fecha = Fechas.objects.filter(id__contains = id).values('fecha_nacimiento')
        nombre = Fechas.objects.filter(id__contains = id).values('nombre')
        if Fechas.objects.filter(id__contains = id):

            return render(request,'l.html', {'fecha_nacimiento':fecha,'nombre':nombre,'cod':1})
        
        else: 

            mensaje = '<h2>No existe el dato, por favor ingrese uno válido</h2>'

            return HttpResponse(mensaje)

        return render(request,'l.html', {'fecha_nacimiento':fecha,'nombre':nombre,'cod':1})

    elif request.GET['fecha']:

        fecha = request.GET['fecha']
        try:
            datetime.strptime(fecha, '%Y-%m-%d')
        except ValueError:
            mensaje = 'Ingrese formato de fecha valido'
            return HttpResponse(mensaje)
        nombre = Fechas.objects.filter(fecha_nacimiento__contains = fecha).values('nombre')

        if Fechas.objects.filter(fecha_nacimiento__contains = fecha):

            return render(request,'l.html', {'fecha_nacimiento':fecha,'nombre':nombre,'cod':2})
        
        else: 

            mensaje = '<h2>No existe el dato, por favor ingrese uno válido</h2>'

            return HttpResponse(mensaje)

    else:
        mensaje = '<h2>Por favor complete al menos un campo</h2>'

        return HttpResponse(mensaje)
    
    return render(request,'l.html', {'fecha_nacimiento':fecha,'nombre':nombre,'cod':2})

def actualizar(request):  

    return render(request,'actualizar.html')

def a(request): 

    if request.GET['id']:

        id = request.GET['id']
        if request.GET['fecha'] and request.GET['nombre']:
            fecha = request.GET['fecha']
            try:
                datetime.strptime(fecha, '%Y-%m-%d')
            except ValueError:
                mensaje = '<h2>Ingrese formato de fecha valido</h2>'
            nombre = request.GET['nombre']
        else:
            mensaje = '<h2>Por favor ingrese todos los capos</h2>'
            return HttpResponse(mensaje)
        if Fechas.objects.filter(fecha_nacimiento__contains = fecha):
            Fechas.objects.filter(id=id).update(nombre = nombre, fecha_nacimiento = fecha)

            return render(request,'a.html', {'fecha_nacimiento':fecha,'nombre':nombre})
        else:
            mensaje = '<h2>Campo id no existe</h2>'
            return HttpResponse(mensaje)

    else:
        mensaje = '<h2>Por favor ingrese un id</h2>'

        return HttpResponse(mensaje)
    
def eliminar(request):  

    return render(request, 'eliminar.html')

def e(request):

    
    if request.GET['id']:

        id = request.GET['id']
        if Fechas.objects.filter(id__contains = id):
            Fechas.objects.filter(id=id).delete()
            return render(request,'e.html')
        else:
            mensaje = '<h2>No existe el id, por favor ingrese uno válido</h2>'
            return HttpResponse(mensaje)

    else:
        mensaje = '<h2>Por favor ingrese un id</h2>'

        return HttpResponse(mensaje)

