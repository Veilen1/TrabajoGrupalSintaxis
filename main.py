import TADProceso as proceso_tad
import TADGrupo as grupo_tad
from datetime import datetime

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("            SISTEMA DE GESTIÓN DE PROCESOS      ")
    print("="*60)
    print("1. ➕ Agregar nuevo proceso")
    print("2. 🔃 Modificar prioridad individual")
    print("3. ❌ Terminar proceso")
    print("4. 👁️  Visualizar procesos")
    print("5. 🛠️  Modificar prioridad por mes")
    print("6. 🧹 Eliminar procesos por tipo")
    print("7. 🕑 Filtrar por intervalo horario")
    print("8. 🚪 Salir")
    print("="*60)

def agregar_proceso(grupo):
    """Agregar nuevo proceso con validaciones integradas"""
    print("\n--- Agregar Proceso ---")
    
    # Solicitar y validar PID
    try:
        pid = int(input("PID: "))
        if pid <= 0:
            print("Error: El PID debe ser un número positivo")
            return
        
        # Verificar que no exista el PID
        for p in grupo:
            if proceso_tad.obtener_pid(p) == pid:
                print(f"Error: Ya existe un proceso con el PID {pid}")
                return
                
    except ValueError:
        print("Error: El PID debe ser un número entero")
        return
    
    # Solicitar y validar nombre
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío")
        return
    
    # Solicitar y validar tipo
    print("Tipos disponibles: sistema, usuario, tiempo_real")
    tipo_proceso = input("Tipo: ").strip().lower()
    if tipo_proceso not in ['sistema', 'usuario', 'tiempo_real']:
        print("Error: Tipo debe ser 'sistema', 'usuario' o 'tiempo_real'")
        return
    
    # Solicitar y validar tamaño
    try:
        tamaño = int(input("Tamaño (KB): "))
        if tamaño <= 0:
            print("Error: El tamaño debe ser un número positivo")
            return
    except ValueError:
        print("Error: El tamaño debe ser un número entero")
        return
    
    # Solicitar y validar prioridad
    print("Prioridades disponibles: alta, media, baja")
    prioridad = input("Prioridad: ").strip().lower()
    if prioridad not in ['alta', 'media', 'baja']:
        print("Error: Prioridad debe ser 'alta', 'media' o 'baja'")
        return
    
    # Crear y agregar proceso
    nuevo_proceso = proceso_tad.crear_proceso(pid, nombre, tipo_proceso, tamaño, prioridad)
    grupo_tad.agregar_proceso(grupo, nuevo_proceso)
    print(f"\n✅ Proceso {pid} agregado exitosamente.\n" + "-"*60)

def modificar_prioridad_individual(grupo):
    """Modificar prioridad de un proceso específico con validaciones integradas"""
    print("\n--- Modificar Prioridad ---")
    
    # Verificar que hay procesos
    if len(grupo) == 0:
        print("No hay procesos en el sistema")
        return
    
    # Solicitar y validar PID
    try:
        grupo_tad.mostrar_procesos(grupo)
        pid = int(input("Ingrese el PID del proceso a modificar: "))

        if pid <= 0:
            print("Error: El PID debe ser un número positivo")
            return
    except ValueError:
        print("Error: El PID debe ser un número entero")
        return
    
    # Buscar proceso
    proceso_encontrado = False
    for proceso in grupo:
        if proceso_tad.obtener_pid(proceso) == pid:
            proceso_encontrado = True
            break
    
    if not proceso_encontrado:
        print(f"Error: No se encontró el proceso con PID {pid}")
        return
    
    # Solicitar y validar nueva prioridad
    print("Prioridades disponibles: alta, media, baja")
    nueva_prioridad = input("Nueva prioridad: ").strip().lower()
    if nueva_prioridad not in ['alta', 'media', 'baja']:
        print("Error: La prioridad debe ser 'alta', 'media' o 'baja'")
        return
    
    # Modificar prioridad
    modificar_prioridad_por_pid(grupo, pid, nueva_prioridad)
    print(f"Prioridad del proceso {pid} modificada a '{nueva_prioridad}'")

def terminar_proceso(grupo):
    """Terminar el primer proceso con validaciones integradas"""
    print("\n--- Terminar Proceso ---")
    
    # Verificar que hay procesos
    if len(grupo) == 0:
        print("No hay procesos para terminar")
        return
    
    # Terminar primer proceso
    proceso_terminado = grupo_tad.terminar_proceso(grupo)
    if proceso_terminado:
        print("Proceso terminado:")
        print(proceso_tad.proceso_a_cadena(proceso_terminado))
    else:
        print("Error al terminar el proceso")

def visualizar_procesos(grupo):
    """Mostrar todos los procesos"""
    print("\n--- Procesos ---")
    grupo_tad.mostrar_procesos(grupo)

def modificar_prioridad_por_mes(grupo):
    """Modificar prioridad por mes con validaciones integradas"""
    print("\n--- Modificar por Mes ---")
    
    # Verificar que hay procesos
    if len(grupo) == 0:
        print("No hay procesos en el sistema")
        return
    
    # Solicitar y validar mes
    try:
        mes = int(input("Mes (1-12): "))
        if mes < 1 or mes > 12:
            print("Error: El mes debe estar entre 1 y 12")
            return
    except ValueError:
        print("Error: El mes debe ser un número entero")
        return
    
    # Modificar prioridad
    modificados = modificar_prioridad_por_mes(grupo, mes)
    
    # Mostrar resultado
    meses_nombres = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                     "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    print(f"Se modificaron {modificados} procesos del mes de {meses_nombres[mes]}")

def eliminar_procesos_por_tipo(grupo):
    """Eliminar procesos por tipo con validaciones integradas"""
    print("\n--- Eliminar por Tipo ---")
    
    # Verificar que hay procesos
    if len(grupo) == 0:
        print("No hay procesos en el sistema")
        return
    
    # Solicitar y validar tipo
    print("Tipos disponibles: sistema, usuario, tiempo_real")
    tipo_proceso = input("Tipo a eliminar: ").strip().lower()
    if tipo_proceso not in ['sistema', 'usuario', 'tiempo_real']:
        print("Error: Tipo debe ser 'sistema', 'usuario' o 'tiempo_real'")
        return
    
    # Eliminar procesos
    eliminados = eliminar_procesos_por_tipo(grupo, tipo_proceso)
    print(f"Se eliminaron {eliminados} procesos de tipo '{tipo_proceso}'")

def cargar_datos_ejemplo(grupo):
    """Carga datos de ejemplo"""
    procesos = [
        (1001, "navegador.exe", "usuario", 2048, "alta"),
        (1002, "sistema.exe", "sistema", 1024, "media"),
        (1003, "juego.exe", "usuario", 4096, "baja"),
        (1004, "antivirus.exe", "sistema", 512, "alta")
    ]
    
    for pid, nombre, tipo, tamaño, prioridad in procesos:
        proceso = proceso_tad.crear_proceso(pid, nombre, tipo, tamaño, prioridad)
        grupo_tad.agregar_proceso(grupo, proceso)

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



def modificar_prioridad_por_mes(grupo):
    """Solicita al usuario un mes y modifica la prioridad a 'baja' para procesos de ese mes"""
    mes = int(input("Ingrese el número del mes que desea modificar (1-12): "))
    modificados = 0
    for proceso in grupo:
        fecha_mod = proceso_tad.obtener_fecha_modificacion(proceso)
        if fecha_mod.month == mes and proceso_tad.obtener_prioridad(proceso) != "baja":
            # Solo modificar si la prioridad no es ya 'baja'
            proceso_tad.establecer_prioridad(proceso, "baja")
            modificados += 1
    print(f"La cantidad de procesos modificados fueron: {modificados}")

def eliminar_procesos_por_tipo(grupo, tipo_proceso):
    """Elimina todos los procesos del tipo especificado"""
    num_tipo = int(input("Ingrese el tipo de proceso a eliminar (1: sistema, 2: usuario, 3: tiempo_real): "))
    if num_tipo == 1:
        tipo_proceso = "sistema"
    elif num_tipo == 2:
        tipo_proceso = "usuario"
    elif num_tipo == 3:
        tipo_proceso = "tiempo_real"
    else:
        print("Tipo de proceso inválido")
    eliminados = 0
    i = 0
    while i < len(grupo):
        if proceso_tad.obtener_tipo_proceso(grupo[i]) == tipo_proceso:
            grupo.pop(i)
            eliminados += 1
        else:
            i += 1
    return eliminados

def visualizar_procesoscola(lista_procesos):
    """Muestra en pantalla la información de cada proceso en la lista"""
    if not lista_procesos:
        print("No hay procesos para mostrar.")
        return

    for i, proceso in enumerate(lista_procesos, start=1):
        nombre = proceso_tad.obtener_nombre(proceso)
        tipo = proceso_tad.obtener_tipo_proceso(proceso)
        prioridad = proceso_tad.obtener_prioridad(proceso)
        fecha = proceso_tad.obtener_fecha_modificacion(proceso)

        print(f"Proceso {i}:")
        print(f"  Nombre     : {nombre}")
        print(f"  Tipo       : {tipo}")
        print(f"  Prioridad  : {prioridad}")
        print(f"  Modificado : {fecha.strftime('%Y-%m-%d %H:%M')}")
        print("-" * 30)

def filtrar_por_intervalo_horario(grupo, hora_inicio, hora_fin):
    """Crea una cola con procesos del intervalo horario especificado"""
    cola_filtrada = []
    print(f"Filtrando procesos entre {hora_inicio} y {hora_fin}")
    for proceso in grupo:
        fecha_mod = proceso_tad.obtener_fecha_modificacion(proceso)
        hora_proceso = fecha_mod.time()
        if hora_inicio <= hora_fin:
            if hora_inicio <= hora_proceso <= hora_fin:
                cola_filtrada.append(proceso)
        else:
            # Intervalo que cruza medianoche
            if hora_proceso >= hora_inicio or hora_proceso <= hora_fin:
                cola_filtrada.append(proceso)
    return cola_filtrada

def main():
    """Función principal del programa"""
    grupo_procesos = grupo_tad.crear_grupo()
    cargar_datos_ejemplo(grupo_procesos)
    
    while True:
        mostrar_menu()
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            agregar_proceso(grupo_procesos)
        elif opcion == "2":
            modificar_prioridad_individual(grupo_procesos)
        elif opcion == "3":
            terminar_proceso(grupo_procesos)
        elif opcion == "4":
            visualizar_procesos(grupo_procesos)
        elif opcion == "5":
            modificar_prioridad_por_mes(grupo_procesos)
        elif opcion == "6":
            eliminar_procesos_por_tipo(grupo_procesos, proceso_tad.obtener_tipo_proceso)
        elif opcion == "7":
            horario_inicio_str = input("Ingrese el horario de inicio del intervalo: (HH:MM): ")
            horario_fin_str = input("Ingrese el horario de fin del intervalo: (HH:MM): ")
            formato_hora = "%H:%M"
            inicio = datetime.strptime(horario_inicio_str, formato_hora).time()
            fin = datetime.strptime(horario_fin_str, formato_hora).time()
            # hora_inicio = inicio.hour
            # hora_fin = fin.hour
            cola_resultado = filtrar_por_intervalo_horario(grupo_procesos, inicio, fin)
            print(f"Se encontraron {len(cola_resultado)} procesos en el intervalo.")
            visualizar_procesoscola(cola_resultado)
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Seleccione 1-8")

main()