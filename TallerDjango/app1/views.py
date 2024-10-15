from django.shortcuts import render, get_object_or_404
from .models import AlumnoT,Frase
# Create your views here.

def indexvista(request):
    objeto= AlumnoT.objects.all().order_by('-id')
    return render(request,'index.html',{'objeto':objeto})

# version 2

def Alumno_vista(request,id):
  alumno = get_object_or_404(AlumnoT,id=id)
  return render(request,'alumno.html',{'objeto':alumno})