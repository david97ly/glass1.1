from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.template.context import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from models import *
from forms import *
from django.contrib.auth.decorators import login_required

def home(request):
    titulo = "Master AutoGlass"
    template = "cofiguraciones.html"
    slider = Slide.objects.all()
    primera =""
    segunda = ""
    tercera = ""
    contador = 0 
    
    for s in slider:
        if s.valida:
            if s.orden.orden == "Primero":
                primera = s
                contador=contador + 1
            elif s.orden.orden =="Segundo":
                segundo = s
                contador=contador + 1
            else:
                tercera = s
                contador=contador + 1
        
    return render_to_response(template,context_instance=RequestContext(request,locals()))

def servicios(request):
    titulo = "SERVICIOS"
    c = {'titulo':titulo}
    return render_to_response('servicios.html',c)


def detalleservice(request):
    titulo = "Detalle de los servicios"
    c = {'titulo': titulo}
    return render_to_response('detalleservices.html',c)


def contacto(request):
    titulo = "Contactenos"
    c = {'titulo': titulo}
    return render_to_response('contacto.html',c)
    
    
def fotos(request):
    titulo = "Galeria de fotos"
    c = {'titulo': titulo}
    return render_to_response('fotos.html',c)
    
    
def quienes(request):
    titulo = "Quienes somos"
    c = {'titulo': titulo}
    return render_to_response('quienes.html',c)



def ubicacion(request):
    titulo = "Nuestra Ubicacion"
    c = {'titulo': titulo}
    return render_to_response('ubicacion.html',c)
    
def login(request):
    titulo = "Login"
    c = {'titulo': titulo}
    return render_to_response('login.html',c)
    
    
@login_required
def conf(request):
    if request.POST:
        form = SlideForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/conf")
    else:
        form = SlideForm()

    sl = Slide.objects.all()    
    template = "cofiguraciones.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))