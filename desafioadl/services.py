from .models import Tarea, SubTarea

def recupera_tareas_y_subtareas():
    tareas = Tarea.objects.all()
    tareas_list = []
    for tarea in tareas:
        subtareas = SubTarea.objects.filter(tarea=tarea)
        tareas_list.append({
            "tarea": tarea,
            "subtarea": subtareas
        })
    return tareas_list

def crear_nueva_tarea(nombre, descripcion):
    tarea = Tarea.objects.create(
        nombre = nombre,
        descripcion = descripcion
    )

    return tarea

def crear_nueva_subtarea(tarea, nombre, descripcion):
    if isinstance(tarea, int):
        tarea = Tarea.objects.get(id=tarea)
    subtarea = SubTarea.objects.create(
        tarea = tarea,
        nombre = nombre,
        descripcion = descripcion
    )
    return subtarea

def eliminar_tarea(tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()

def eliminar_subtarea(subtarea_id):
    subtarea = SubTarea.objects.get(id=subtarea_id)
    subtarea.delete()

def imprimir_en_pantalla():
    tareas = recupera_tareas_y_subtareas()
    tarea_numero = 0
    subtarea_numero = 0
    print('Tareas y subtareas:')
    for tarea in tareas:
        tarea_numero += 1
        print(f'[{tarea_numero}] {tarea["tarea"].name}')
        for subtarea in tarea["subtarea"]:
            subtarea_numero += 1
            print(f'....[{subtarea_numero}]{subtarea.name}')
    return tareas
