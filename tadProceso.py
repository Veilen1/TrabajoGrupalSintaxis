# TAD Proceso
from datetime import datetime

def crearProceso():
    """Crea un proceso vacío"""
    return {
        'pid': 0,
        'nombre': '',
        'tipo': '',
        'tamaño': 0,
        'prioridad': '',
        'fecha_hora': None
    }

def cargarProceso(proceso, pid, nombre, tipo, tamaño, prioridad, fecha_hora):
    """Carga los datos en un proceso"""
    proceso['pid'] = pid
    proceso['nombre'] = nombre
    proceso['tipo'] = tipo
    proceso['tamaño'] = tamaño
    proceso['prioridad'] = prioridad
    proceso['fecha_hora'] = fecha_hora

def obtenerPID(proceso):
    """Obtiene el PID del proceso"""
    return proceso['pid']

def obtenerNombre(proceso):
    """Obtiene el nombre del proceso"""
    return proceso['nombre']

def obtenerTipo(proceso):
    """Obtiene el tipo del proceso"""
    return proceso['tipo']

def obtenerTamaño(proceso):
    """Obtiene el tamaño del proceso"""
    return proceso['tamaño']

def obtenerPrioridad(proceso):
    """Obtiene la prioridad del proceso"""
    return proceso['prioridad']

def obtenerFechaHora(proceso):
    """Obtiene la fecha y hora del proceso"""
    return proceso['fecha_hora']

def modificarPrioridad(proceso, nueva_prioridad):
    """Modifica la prioridad del proceso"""
    proceso['prioridad'] = nueva_prioridad

def mostrarProceso(proceso):
    """Muestra los datos del proceso"""
    print(f"PID: {proceso['pid']}")
    print(f"Nombre: {proceso['nombre']}")
    print(f"Tipo: {proceso['tipo']}")
    print(f"Tamaño: {proceso['tamaño']}")
    print(f"Prioridad: {proceso['prioridad']}")
    print(f"Fecha/Hora: {proceso['fecha_hora']}")
    print("-" * 30)