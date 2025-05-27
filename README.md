# 📄 DOCUMENTACIÓN DEL SISTEMA  
## GESTIÓN DE PROCESOS - TADs

---

## 📚 ÍNDICE
1. [TAD Proceso](#1-tad-proceso)  
2. [TAD Grupo](#2-tad-grupo)  
3. [Programa Principal](#3-programa-principal)  
4. [Reglas Importantes](#4-reglas-importantes)  
5. [Cómo Usar el Sistema](#5-cómo-usar-el-sistema)  

---

## 1. TAD PROCESO

### ¿Qué es?
Un TAD que representa un proceso del sistema con sus datos básicos.

### Datos que guarda:
- `PID`: Número único del proceso  
- `Nombre`: Nombre del proceso (ej: `"navegador.exe"`)  
- `Tipo`: `sistema`, `usuario` o `tiempo_real`  
- `Tamaño`: Cuántos KB ocupa  
- `Prioridad`: `alta`, `media` o `baja`  
- `Fecha`: Cuándo se modificó por última vez  

### Funciones disponibles:
- `crear_proceso()`  
- `obtener_pid()`  
- `obtener_nombre()`  
- `obtener_tipo_proceso()`  
- `obtener_tamaño()`  
- `obtener_prioridad()`  
- `obtener_fecha_modificacion()`  
- `establecer_prioridad()`  
- `proceso_a_cadena()`  

### Cómo funciona por dentro:
- Utiliza un diccionario de Python.  
- Claves: `'pid'`, `'nombre'`, `'tipo_proceso'`, `'tamaño'`, `'prioridad'`, `'fecha_modificacion'`  
- Al cambiar la prioridad, la fecha se actualiza automáticamente.  

---

## 2. TAD GRUPO

### ¿Qué es?
Un TAD que maneja una lista de procesos en orden FIFO (First In, First Out).

### Qué hace:
- Mantiene los procesos en orden de llegada  
- Permite buscar, modificar y eliminar procesos  
- Filtra procesos según criterios específicos  

### Funciones disponibles:
- `crear_grupo()`  
- `agregar_proceso()`  
- `terminar_proceso()`  
- `buscar_proceso_por_pid()`  
- `modificar_prioridad_por_pid()`  
- `modificar_prioridad_por_mes()`  
- `eliminar_procesos_por_tipo()`  
- `filtrar_por_intervalo_horario()`  
- `mostrar_procesos()`  

### Cómo funciona por dentro:
- Utiliza una lista de Python  
- Cada elemento es un proceso (diccionario)  
- `append()` para agregar al final  
- `pop(0)` para sacar el primero  

### Orden FIFO:
`Primero en entrar → [Proceso1] [Proceso2] [Proceso3] → Primero en salir`

---

## 3. PROGRAMA PRINCIPAL

### Estructura:
El programa contiene un menú con 8 opciones, que interactúan con los TADs.

### Funciones del menú:
1. **Agregar Proceso**  
2. **Modificar Prioridad Individual**  
3. **Terminar Proceso**  
4. **Visualizar Procesos**  
5. **Modificar Prioridad por Mes**  
6. **Eliminar por Tipo**  
7. **Filtrar por Horario**  
8. **Salir**  

### Validaciones:
- Verifica entradas numéricas y de texto  
- Rangos válidos: mes (1–12), hora (0–23)  
- Opciones válidas para tipos y prioridades  
- Verifica que el grupo no esté vacío si es necesario  

---

## 4. REGLAS IMPORTANTES

### ❌ NUNCA HAGAS ESTO:
```python
proceso['pid'] = 123  
grupo.append(proceso)  
proceso['prioridad'] = "alta"  
```

### ✅ SIEMPRE HAZ ESTO:
```python
proceso_tad.obtener_pid(proceso)  
grupo_tad.agregar_proceso(grupo, proceso)  
proceso_tad.establecer_prioridad(proceso, "alta")  
```

### ¿Por qué?
- Los TADs encapsulan la lógica de los datos  
- Si accedés directamente, podés romper la estructura  
- Las funciones del TAD mantienen la integridad del sistema  

### Responsabilidades:
- **TAD Proceso**: Maneja **un** proceso  
- **TAD Grupo**: Maneja **muchos** procesos  
- **Main**: Interfaz con el usuario y validaciones  

---

## 5. CÓMO USAR EL SISTEMA

### Para ejecutar:
```bash
python main.py
```

### Datos válidos:

**Tipos de proceso**:  
- `sistema`  
- `usuario`  
- `tiempo_real`  

**Prioridades**:  
- `alta`  
- `media`  
- `baja`  

**Rangos válidos**:  
- `PID`: Números positivos (ej: 1, 2, 3…)  
- `Tamaño`: En KB (número positivo)  
- `Mes`: 1 a 12  
- `Hora`: 0 a 23  

---

### Ejemplos de uso:

**Agregar proceso**:
```
PID: 1005  
Nombre: editor.exe  
Tipo: usuario  
Tamaño: 1024  
Prioridad: media  
```

**Modificar prioridad**:
```
PID del proceso: 1005  
Nueva prioridad: alta  
```

**Filtrar por horario**:
```
Hora inicio: 9  
Hora fin: 17  
```
(Muestra procesos modificados entre 9:00 y 17:59)

---

### Datos de ejemplo:
El sistema incluye 4 procesos precargados para realizar pruebas.

### Mensajes de error:
- `"Error: PID debe ser un número positivo"`  
- `"Error: Tipo debe ser 'sistema', 'usuario' o 'tiempo_real'"`  
- `"Error: No hay procesos en el sistema"`  

---

## ✅ RESUMEN RÁPIDO:
- **TAD Proceso** = maneja 1 proceso  
- **TAD Grupo** = maneja muchos procesos en orden FIFO  
- **Main** = menú + validaciones  
- **Siempre usar las funciones de los TADs**  
- **Nunca acceder directamente a los datos internos**