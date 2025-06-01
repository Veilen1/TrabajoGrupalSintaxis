from tadProceso import *
from tadGrupo import *
from datetime import datetime

# Crear el grupo de procesos
grupo = crearGrupo()

# Menú principal
opcion = 1
while opcion != 0:
    print("\n" + "="*50)
    print("    SISTEMA DE GESTIÓN DE PROCESOS")
    print("="*50)
    print("1. Agregar nuevo proceso")
    print("2. Modificar prioridad individual")
    print("3. Terminar proceso (atender primero)")
    print("4. Visualizar todos los procesos")
    print("5. Modificar prioridad masiva por mes")
    print("6. Eliminar procesos por tipo")
    print("7. Filtrar por intervalo horario")
    print("0. Salir")
    print("-"*50)
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        # Agregar nuevo proceso
        print("\n--- AGREGAR NUEVO PROCESO ---")
        p = crearProceso()
        pid = int(input("Ingrese PID: "))
        nombre = input("Ingrese nombre: ")
        tipo = input("Ingrese tipo: ")
        tamaño = int(input("Ingrese tamaño: "))
        prioridad = input("Ingrese prioridad (alta/media/baja): ")
        
        print("Ingrese fecha y hora (formato: YYYY-MM-DD HH:MM)")
        fecha_str = input("Fecha y hora: ")
        fecha_hora = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
        
        cargarProceso(p, pid, nombre, tipo, tamaño, prioridad, fecha_hora)
        agregarProceso(grupo, p)
        print("Proceso agregado exitosamente!")
    
    elif opcion == 2:
        # Modificar prioridad individual
        print("\n--- MODIFICAR PRIORIDAD INDIVIDUAL ---")
        if estaVacio(grupo):
            print("No hay procesos en el sistema")
        else:
            pid_buscar = int(input("Ingrese PID del proceso: "))
            indice = buscarPorPID(grupo, pid_buscar)
            if indice != -1:
                proceso = obtenerProceso(grupo, indice)
                print(f"Proceso encontrado: {obtenerNombre(proceso)}")
                print(f"Prioridad actual: {obtenerPrioridad(proceso)}")
                nueva_prioridad = input("Ingrese nueva prioridad: ")
                modificarPrioridad(proceso, nueva_prioridad)
                print("Prioridad modificada exitosamente!")
            else:
                print("Proceso no encontrado")
    
    elif opcion == 3:
        # Terminar proceso (atender primero)
        print("\n--- TERMINAR PROCESO ---")
        if estaVacio(grupo):
            print("No hay procesos para atender")
        else:
            proceso_atendido = quitarPrimero(grupo)
            print("Proceso atendido:")
            mostrarProceso(proceso_atendido)
            print("Proceso terminado exitosamente!")
    
    elif opcion == 4:
        # Visualizar todos los procesos
        print("\n--- TODOS LOS PROCESOS ---")
        mostrarTodos(grupo)
    
    elif opcion == 5:
        # Modificar prioridad masiva por mes
        print("\n--- MODIFICAR PRIORIDAD POR MES ---")
        if estaVacio(grupo):
            print("No hay procesos en el sistema")
        else:
            mes = int(input("Ingrese mes (1-12): "))
            contador = 0
            for i in range(tamaño(grupo)):
                proceso = obtenerProceso(grupo, i)
                fecha = obtenerFechaHora(proceso)
                if fecha.month == mes:
                    modificarPrioridad(proceso, "baja")
                    contador += 1
            print(f"Se modificaron {contador} procesos a prioridad baja")
    
    elif opcion == 6:
        # Eliminar procesos por tipo
        print("\n--- ELIMINAR PROCESOS POR TIPO ---")
        if estaVacio(grupo):
            print("No hay procesos en el sistema")
        else:
            tipo_eliminar = input("Ingrese tipo de proceso a eliminar: ")
            # Crear nuevo grupo sin los procesos del tipo especificado
            nuevo_grupo = crearGrupo()
            contador = 0
            for i in range(tamaño(grupo)):
                proceso = obtenerProceso(grupo, i)
                if obtenerTipo(proceso) != tipo_eliminar:
                    agregarProceso(nuevo_grupo, proceso)
                else:
                    contador += 1
            # Reemplazar el grupo original
            grupo.clear()
            for i in range(tamaño(nuevo_grupo)):
                proceso = obtenerProceso(nuevo_grupo, i)
                agregarProceso(grupo, proceso)
            print(f"Se eliminaron {contador} procesos del tipo '{tipo_eliminar}'")
    
    elif opcion == 7:
        # Filtrar por intervalo horario
        print("\n--- FILTRAR POR INTERVALO HORARIO ---")
        if estaVacio(grupo):
            print("No hay procesos en el sistema")
        else:
            print("Ingrese hora inicial (formato HH:MM)")
            hora_inicio = input("Hora inicio: ")
            print("Ingrese hora final (formato HH:MM)")
            hora_fin = input("Hora fin: ")
            
            # Convertir a objetos time para comparar
            from datetime import time
            inicio = datetime.strptime(hora_inicio, "%H:%M").time()
            fin = datetime.strptime(hora_fin, "%H:%M").time()
            
            # Crear cola con procesos en el intervalo
            cola_filtrada = crearGrupo()
            for i in range(tamaño(grupo)):
                proceso = obtenerProceso(grupo, i)
                fecha_hora = obtenerFechaHora(proceso)
                hora_proceso = fecha_hora.time()
                if inicio <= hora_proceso <= fin:
                    agregarProceso(cola_filtrada, proceso)
            
            print(f"\nProcesos en el intervalo {hora_inicio} - {hora_fin}:")
            mostrarTodos(cola_filtrada)
    
    elif opcion == 0:
        print("\n¡Gracias por usar el sistema!")
    
    else:
        print("\nOpción inválida. Intente nuevamente.")

print("Sistema finalizado.")