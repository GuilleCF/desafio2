from django.db import models

# Create your models here.
class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    is_active = models.BooleanField(default=False)
    creado_en = models.DataTimeField(auto_now_add=True)
    actualizado_en = models.DataTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
class SubTarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    is_active = models.BooleanField(default=False)
    creado_en = models.DataTimeField(auto_now_add=True)
    actualizado_en = models.DataTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    @property
    def main_task(self):
        return self.tarea.nombre