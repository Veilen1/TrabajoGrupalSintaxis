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

