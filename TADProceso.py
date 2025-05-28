from datetime import datetime

def crear_proceso(pid, nombre, tipo_proceso, tamaño, prioridad):
    """Crea un nuevo proceso"""
    proceso = {
        'pid': pid,
        'nombre': nombre,
        'tipo_proceso': tipo_proceso,
        'tamaño': tamaño,
        'prioridad': prioridad,
        'fecha_modificacion': datetime.now()
    }
    return proceso

def obtener_pid(proceso):
    """Obtiene el PID del proceso"""
    return proceso['pid']

def obtener_nombre(proceso):
    """Obtiene el nombre del proceso"""
    return proceso['nombre']

def obtener_tipo_proceso(proceso):
    """Obtiene el tipo del proceso"""
    return proceso['tipo_proceso']

def obtener_tamaño(proceso):
    """Obtiene el tamaño del proceso"""
    return proceso['tamaño']

def obtener_prioridad(proceso):
    """Obtiene la prioridad del proceso"""
    return proceso['prioridad']

def obtener_fecha_modificacion(proceso):
    """Obtiene la fecha de modificación del proceso"""
    return proceso['fecha_modificacion']

def establecer_prioridad(proceso, nueva_prioridad):
    """Establece una nueva prioridad para el proceso"""
    proceso['prioridad'] = nueva_prioridad
    proceso['fecha_modificacion'] = datetime.now()

def proceso_a_cadena(proceso):
    """Convierte el proceso a cadena"""
    fecha_str = proceso['fecha_modificacion'].strftime('%d/%m/%Y %H:%M:%S')
    return (f"PID: {proceso['pid']} | Nombre: {proceso['nombre']} | "
            f"Tipo: {proceso['tipo_proceso']} | Tamaño: {proceso['tamaño']}KB | "
            f"Prioridad: {proceso['prioridad']} | "
            f"Última modificación: {fecha_str}")


