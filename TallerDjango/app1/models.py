from django.db import models

# Create your models here.
# version 1  
class AlumnoT(models.Model):
    Apaterno=models.CharField(max_length=50,verbose_name="Apellido paterno")
    Amaterno=models.CharField(max_length=50,verbose_name="Apellido materno")
    nombre=models.CharField(max_length=50,verbose_name="Nombre")
    fecha_nacimiento=models.DateField(verbose_name='Fecha Nacimiento',null=False,blank=False)
    fecha_ingreso=models.DateField(verbose_name='Fecha Ingreso',null=False,blank=False)
    
    # ver 2 makemigrations y migrate
    class Meta:
        db_table="Alumnos"
        verbose_name="Alumno"
        verbose_name_plural="Alumnos"
         #minuto 1:11:53 , 1:31:42 https://youtu.be/P-6AioZhfMc?si=izqKmPXeNvRtod2_
    
    def __str__(self) -> str:
        return self.nombre   #puedo modificar
 # version 1      
class Frase(models.Model):
    comentario=models.TextField(verbose_name='Comentario',max_length=400)
    Alumno_fk=models.ForeignKey(AlumnoT,on_delete=models.CASCADE)
    # ver 3 
    class Meta:
        verbose_name="Frase"
        verbose_name_plural="frases"