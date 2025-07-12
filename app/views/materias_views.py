from django.shortcuts import render,redirect, get_object_or_404
from app.models import Materias

def materias_list(request):
    items = Materias.objects.all()
    return render(request, 'materias/list.html', {'items': items})

def materias_create(request):
    if request.method == "POST":
       Materias.objects.create(
           nombre = request.POST["nombre"],
           codigo = request.POST["codigo"]
       )
       return redirect("materias_list")
    return render(request,"materias/form.html");

def materias_update(request, pk):
    materia = get_object_or_404(Materias, pk=pk)
    if request.method == "POST":
        materia.nombre = request.POST['nombre']
        materia.codigo = request.POST['codigo']
        materia.save()
        return redirect("materias_list")
    return render(request, "materias/form.html", {'item': materia, 'title': "Editar Materia", 'btnText': 'Editar'})

def materias_delete(request, pk):
    materia = get_object_or_404(Materias, pk=pk);
    materia.delete();
    return redirect("materias_list")
