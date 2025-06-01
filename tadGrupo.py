# TAD Grupo de Procesos (Cola)
from tadProceso import *

def crearGrupo():
    """Crea un grupo vacío de procesos"""
    return []

def estaVacio(grupo):
    """Verifica si el grupo está vacío"""
    return len(grupo) == 0

def agregarProceso(grupo, proceso):
    """Agrega un proceso al final del grupo (respeta orden de llegada)"""
    grupo.append(proceso)

def quitarPrimero(grupo):
    """Quita y retorna el primer proceso del grupo"""
    if not estaVacio(grupo):
        return grupo.pop(0)
    return None

def obtenerPrimero(grupo):
    """Obtiene el primer proceso sin quitarlo"""
    if not estaVacio(grupo):
        return grupo[0]
    return None

def tamaño(grupo):
    """Retorna la cantidad de procesos en el grupo"""
    return len(grupo)

def mostrarTodos(grupo):
    """Muestra todos los procesos del grupo"""
    if estaVacio(grupo):
        print("No hay procesos en el grupo")
    else:
        print(f"Total de procesos: {tamaño(grupo)}")
        print("=" * 40)
        for i, proceso in enumerate(grupo):
            print(f"Posición {i+1}:")
            mostrarProceso(proceso)

def buscarPorPID(grupo, pid):
    """Busca un proceso por PID y retorna su índice, -1 si no existe"""
    for i, proceso in enumerate(grupo):
        if obtenerPID(proceso) == pid:
            return i
    return -1

def obtenerProceso(grupo, indice):
    """Obtiene un proceso por su índice"""
    if 0 <= indice < len(grupo):
        return grupo[indice]
    return None