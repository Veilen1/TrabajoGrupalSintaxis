# TAD Grupo de Procesos
# Grupo de procesos: lista de procesos

def crearGrupo():
    return []

def agregarProceso(grupo, proceso):
    grupo.append(proceso.copy())
""" 
def eliminarProcesoPorPID(grupo, indice):
    if 0 <= indice < len(grupo):
        return grupo.pop(indice)
    return 0
"""
def eliminarProcesoPorPID(grupo, pid):
    if ( pid != 0 ):
        grupo.remove(pid)
    else:
        return 0

def verProcesoPorPID(grupo, indice):
    if 0 <= indice < len(grupo):
        return grupo[indice].copy()
    return 0

def cantidadProcesos(grupo):
    return len(grupo)
