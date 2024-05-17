from .models import Persona

def crear_tarea(descripcion):
    tarea = Tarea.objects.create(descripcion=descripcion)
    imp()

def crear_subtarea(descripcion, tarea):
    SubTarea.objects.create(descripcion=descripcion, tarea=tarea)
    imp()

def eliminar_tarea(tarea_id):
    tarea = Tarea.objects.filter(id=tarea_id).update(eliminada=True)
    Subtarea.objects.filter(tarea_id=tarea_id).update(eliminada=True)
    imp()

def elimina_subtarea(subtarea_id):
    subtarea = Subtarea.objects.filter(id=subtarea_id).update(eliminada=True)
    imp()

def imp():
    print('Tarea: ', Tarea.objects.all())
    print('Subtarea: ', Subtarea.objects.all())
    print('Persona: ', Persona.objects.all())
    print('----------------------')
