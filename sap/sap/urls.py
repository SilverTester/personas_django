"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from webapp.views import inicio, sap
from personas.views import detallePersona, nuevaPersona, editarPersona, eliminarPersona

urlpatterns = (
    path('', inicio, name='index'),
    path('admin/', admin.site.urls),
    path('sap/', sap, name='sap'),
    path('sap/detalle_persona/<int:id>', detallePersona),
    path('sap/nueva_persona', nuevaPersona),
    path('sap/editar_persona/<int:id>', editarPersona),
    path('sap/eliminar_persona/<int:id>', eliminarPersona),
)
