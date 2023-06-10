"""gestionBDD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestionBDD.views import formulario, respuesta, formularioBusqueda, resultado, register, ingresar, salir, home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("formulario/", formulario, name="Formulario"),
    path("respuesta/", respuesta),
    path("buscar/", formularioBusqueda, name="Busqueda"),
    path("resultado/", resultado),
    path("register/", register, name="registrar"),
    path("login/", ingresar, name="ingresar"),
    path("salir/", salir, name="salir"),
    path("", home, name="home"),
]
