"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app import views
"""
  frederickpeal.dev
  frederickpeal.dev /about
  frederickpeal.dev /contact
  frederickpeal.dev /blog
  google.com /search?q=django+%20maria 
"""

urlpatterns = [
    path('admin/', admin.site.urls),

    # rutas para materias
    path("materias/", views.materias_list, name="materias_list"),
    path("materias/create", views.materias_create, name="materias_create"),
    path("materias/<int:pk>/edit", views.materias_update, name="materias_edit"),
    path("materias/<int:pk>/delete", views.materias_delete, name="materias_delete")

]
