from django.contrib import admin
from .models import AlumnoT,Frase # version 1

# Register your models here.
# version 4 
admin.site.site_header="Control escolar"
admin.site.index_title="Sitio control escolar"
admin.site.site_title="Admin Escolar"

# version 3 
class ComentarioInLine(admin.TabularInline):
    model=Frase
    extra=1
    
# version 1  
class AlumnoAdmin(admin.ModelAdmin):
    fields =['Apaterno','Amaterno','nombre','fecha_nacimiento','fecha_ingreso']
    list_display=['Apaterno','Amaterno','nombre']
    # version 3 
    inlines=[ComentarioInLine]
    # version 4
    def actualizar_o(self,request,queryset):
        for obj in queryset:
            if "O" in obj.nombre:
                nombre1= obj.nombre
                obj.nombre=nombre1.replace("O","o")
                obj.save()
        self.message_user(request,"Exitosamente")
    actualizar_o.short_description="Actualizar letras O por o"
            
    actions=["actualizar_o"]
  # version 1   
admin.site.register(AlumnoT,AlumnoAdmin) # version 1 
# version 2
@admin.register(Frase)
class FraseAdmin(admin.ModelAdmin):
    fields=['comentario','Alumno_fk']
    list_display=['comentario']