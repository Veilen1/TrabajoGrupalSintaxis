from tadProceso import *
from tadGrupo import *
from datetime import datetime

grupo = crearGrupo()

while True:
    print("    SISTEMA GESTION DE PROCESOS")
    print("1. Agregar nuevo proceso")
    print("2. Modificar prioridad individual")
    print("3. Terminar proceso (atender primero)")
    print("4. Visualizar todos los procesos")
    print("5. Modificar prioridad masiva por mes")
    print("6. Eliminar procesos por tipo")
    print("7. Filtrar por intervalo horario")
    print("0. Salir")
    
    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Error, debe ingresar un numero del menu")
        continue

    if opcion == 0:
        print("Saliendo del sistema...")
        break

    if opcion == 1:
        while True:
            print("\n--- AGREGAR NUEVO PROCESO ---")
            p = crearProceso()
            
            while True:
                try: #AGREGA UN PROCESO, EN CASO DE ERROR VUELVE A INGRESAR EL PID
                    pid = int(input("Ingrese PID: "))
                    break
                except ValueError:
                    print("El PID debe ser un numero entero")
                    
            while True:
                try:
                    nombre = input("Ingrese nombre: ").strip()
                    break
                except ValueError:
                    if not nombre:
                        print("Error, el nombre no puede estar vacio")

            while True:
                tipo = input("Ingrese tipo: Sistema / Usuario / Monitoreo\n").lower()
                if tipo in ["usuario", "sistema", "monitoreo"]:
                    break
                else:
                    print("Error, debe ingresar sistema / usuario / Monitoreo")

            while True:
                try:
                    tamaño = int(input("Ingrese tamaño del proceso: "))
                    break
                except ValueError:
                    print(" Error, debes ingresar un numero para el tamaño")

            while True:
                prioridad = input("Ingrese prioridad (alta/media/baja): ").lower()
                if prioridad in ["alta", "media", "baja"]:
                    break
                else:
                    print("Error, debes ingresar una opcion valida(alta,media o baja)")

            while True:
                print("Ingrese fecha y hora (formato: YYYY-MM-DD HH:MM)")
                fecha_str = input("Fecha y hora: ")
                try:
                    fecha_hora = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
                    break
                except ValueError:
                    print(" Error , debes ingresar la fecha correctamente")

            cargarProceso(p, pid, nombre, tipo, tamaño, prioridad, fecha_hora)
            agregarProceso(grupo, p)
            print("\nProceso agregado con exito \n")
            break
    
    elif opcion == 2:
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
                print("Prioridad modificada")
            else:
                print("Proceso no encontrado")
    
    elif opcion == 3:
        print("\n--- TERMINAR PROCESO ---")
        if estaVacio(grupo):
            print("No hay procesos para atender")
        else:
            proceso_atendido = quitarPrimero(grupo)
            print("Proceso atendido:")
            mostrarProceso(proceso_atendido)
            print("Proceso terminado con exito")
    
    elif opcion == 4:
        print("\n--- TODOS LOS PROCESOS ---")
        mostrarTodos(grupo)
    
    elif opcion == 5:
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
        print("\n---ELIMINAR PROCESOS POR TIPO ---")
        if estaVacio(grupo):
            print("No hay procesos en el sistema")
        else:
            tipo_eliminar = input("Ingrese tipo de proceso a eliminar: ")
            nuevo_grupo = crearGrupo()
            contador = 0
            for i in range(tamaño(grupo)):
                proceso = obtenerProceso(grupo, i)
                if obtenerTipo(proceso) != tipo_eliminar:
                    agregarProceso(nuevo_grupo, proceso)
                else:
                    contador += 1
            grupo.clear()
            for i in range(tamaño(nuevo_grupo)):
                proceso = obtenerProceso(nuevo_grupo, i)
                agregarProceso(grupo, proceso)
            print(f"Se eliminaron {contador} procesos del tipo '{tipo_eliminar}'")
    
    elif opcion == 7:
        print("\n--- FILTRAR POR INTERVALO HORARIO ---")
        if estaVacio(grupo):
            print("No hay procesos en el sistema")
        else:
            print("Ingrese hora inicial (formato HH:MM)")
            hora_inicio = input("Hora inicio: ")
            print("Ingrese hora final (formato HH:MM)")
            hora_fin = input("Hora fin: ")
            
            from datetime import time
            inicio = datetime.strptime(hora_inicio, "%H:%M").time()
            fin = datetime.strptime(hora_fin, "%H:%M").time()
            
            cola_filtrada = crearGrupo()
            for i in range(tamaño(grupo)):
                proceso = obtenerProceso(grupo, i)
                fecha_hora = obtenerFechaHora(proceso)
                hora_proceso = fecha_hora.time()
                if inicio <= hora_proceso <= fin:
                    agregarProceso(cola_filtrada, proceso)
            
            print(f"\nProcesos en el intervalo {hora_inicio} - {hora_fin}:")
            mostrarTodos(cola_filtrada)

    else:
        print("Opcion no valida")

print("Sistema finalizado")