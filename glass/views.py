from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.template.context import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from forms import *
from django.contrib.auth.decorators import login_required

def home(request):
    hola="here"
    nombrep="Esta es otra prueba"
    compania = "Master auto Glass"
    c = {'hola':hola,'nombre':nombrep,'compa':compania,}
    return render_to_response('home.html',c)

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
    
    
