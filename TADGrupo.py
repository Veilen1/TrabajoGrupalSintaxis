import TADProceso as proceso_tad

def crear_grupo():
    """Crea un nuevo grupo vacío de procesos"""
    return []

def agregar_proceso(grupo, proceso):
    """Agrega un proceso al final del grupo (FIFO)"""
    # Verificar que no exista el mismo PID
    for p in grupo:
        if proceso_tad.obtener_pid(p) == proceso_tad.obtener_pid(proceso):
            return False
    grupo.append(proceso)
    return True

def terminar_proceso(grupo):
    """Retira el primer proceso del grupo (FIFO)"""
    if len(grupo) == 0:
        return None
    return grupo.pop(0)

def buscar_proceso_por_pid(grupo, pid):
    """Busca un proceso por su PID"""
    for proceso in grupo:
        if proceso_tad.obtener_pid(proceso) == pid:
            return proceso
    return None

def modificar_prioridad_por_pid(grupo, pid, nueva_prioridad):
    """Modifica la prioridad de un proceso específico"""
    proceso = buscar_proceso_por_pid(grupo, pid)
    if proceso is not None:
        proceso_tad.establecer_prioridad(proceso, nueva_prioridad)
        return True
    return False

def modificar_prioridad_por_mes(grupo, mes):
    """Modifica la prioridad a 'baja' para procesos del mes especificado"""
    modificados = 0
    for proceso in grupo:
        fecha_mod = proceso_tad.obtener_fecha_modificacion(proceso)
        if fecha_mod.month == mes:
            proceso_tad.establecer_prioridad(proceso, "baja")
            modificados += 1
    return modificados

def eliminar_procesos_por_tipo(grupo, tipo_proceso):
    """Elimina todos los procesos del tipo especificado"""
    eliminados = 0
    i = 0
    while i < len(grupo):
        if proceso_tad.obtener_tipo_proceso(grupo[i]) == tipo_proceso:
            grupo.pop(i)
            eliminados += 1
        else:
            i += 1
    return eliminados

def filtrar_por_intervalo_horario(grupo, hora_inicio, hora_fin):
    """Crea una cola con procesos del intervalo horario especificado"""
    cola_filtrada = []
    for proceso in grupo:
        fecha_mod = proceso_tad.obtener_fecha_modificacion(proceso)
        hora_proceso = fecha_mod.hour
        if hora_inicio <= hora_proceso <= hora_fin:
            cola_filtrada.append(proceso)
    return cola_filtrada

def mostrar_procesos(grupo):
    """Muestra todos los procesos del grupo"""
    if len(grupo) == 0:
        print("No hay procesos en el grupo.")
        return
    
    print(f"\nTotal de procesos: {len(grupo)}")
    print("-" * 80)
    for i, proceso in enumerate(grupo, 1):
        print(f"{i}. {proceso_tad.proceso_a_cadena(proceso)}")
    print("-" * 80)

# Ejemplo de uso
if __name__ == "__main__":
    grupo = crear_grupo()
    proceso1 = proceso_tad.crear_proceso(1001, "navegador.exe", "usuario", 2048, "alta")
    agregar_proceso(grupo, proceso1)
    mostrar_procesos(grupo)
