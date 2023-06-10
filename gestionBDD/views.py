from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime
from gestor.models import articulo
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .formularios import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate 

def formulario(request):
    return render(request, "formulario.html")

def respuesta(request):
    agnoActual=datetime.now().year
    diaActual=datetime.now().day
    mesActual=datetime.now().month
    agnoNacimiento= int(request.GET["nacimiento"].split("-")[0])
    mesNacimiento= int(request.GET["nacimiento"].split("-")[1])
    diaNacimiento= int(request.GET["nacimiento"].split("-")[2])
    edad=agnoActual - agnoNacimiento
    if mesNacimiento > mesActual:
        edad-=1
    elif mesActual==mesNacimiento:
        if diaActual < diaNacimiento:
            edad-=1
    nombre=request.GET["nombre"]
    genero=request.GET["genero"]
    return render(request, "respuesta.html", {"nombre":nombre, "edad":edad, "genero":genero})

def formularioBusqueda(request):
    arti=[]
    ar=articulo.objects.all()
    for i in ar:
        arti.append(i.seccion)
    arti=sorted(list(set(arti)))
    return render(request, "formuBusqueda.html", {"articulos":arti})

def resultado(request):
    encontrado=True
    if not(request.GET["producto"]=="") and not(request.GET["seccion"]=="todos"):
        nombre=request.GET["producto"]
        seccion=request.GET["seccion"]
        resultado=articulo.objects.filter(nombre__icontains=nombre, seccion=seccion)

    elif not(request.GET["producto"]=="") and (request.GET["seccion"]=="todos"):
        nombre=request.GET["producto"]
        resultado=articulo.objects.filter(nombre__icontains=nombre)

    elif (request.GET["producto"]=="") and not(request.GET["seccion"]=="todos"):
        seccion=request.GET["seccion"]
        resultado=articulo.objects.filter(seccion=seccion)
    
    elif (request.GET["producto"]=="") and (request.GET["seccion"]=="todos"):
        resultado=articulo.objects.all()
    if not resultado:
        encontrado=False

    return render(request, "resulBusqueda.html",{"registro":resultado, "estatus":encontrado})

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            Username=form.cleaned_data["username"]
            form.save()
            messages.success(request, "Usuario %s creado" %Username)
    else:
        form=UserRegisterForm()
    contexto={"formulario":form}
    return render(request, "register.html", contexto)

def ingresar(request):
    if request.method=="POST":
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            nombreUsuario=form.cleaned_data.get("username")
            contraseña=form.cleaned_data.get("password")
            usuario=authenticate(username=nombreUsuario, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, "Bienvenido nuevamente %s" %nombreUsuario)
                return redirect("home")
            else:
                messages.error(request, "El usurio o contraseña son incorrectos")
        else:
            messages.error(request, "El usuario o contraseña son incorrectos")
    else:
        form=AuthenticationForm()
    contexto={"formulario":form}
    return render(request, "login.html", contexto)

def home(request):
    return render(request, "Index.html")

def salir(request):
    logout(request)
    messages.success(request, "Sesion cerrada")
    return redirect("ingresar")
