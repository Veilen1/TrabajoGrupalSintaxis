
proceso = ["","",0,0,0,""]
#Identrificador (PID), nombre, tipo de proceso, tamaño, prioridad, fecha y hora

def crearProceso():
    proceso = ["","",0,0,0,""]
    return proceso

def cargarProceso(proceso,pid,nom,tproc,tam,pri,fh):
    proceso[0]=pid
    proceso[1]=nom
    proceso[2]=tproc
    proceso[3]=tam
    proceso[4]=pri
    proceso[5]=fh

def verPID(proceso):
    return proceso[0]

def verNombre(proceso):
    return proceso[1]

def verTipo(proceso):
    return proceso[2]

def verTamaño(proceso):
    return proceso[3]

def verPrioridad(proceso):
    return proceso[4]

def verFechayHora(proceso):
    return proceso[5]

def modPID(proceso, nuevoPID):
    proceso[0] = nuevoPID

def modNombre(proceso, nuevoNom):
    proceso[1] = nuevoNom

def modTipo(proceso, nuevoTipo):
    proceso[2] = nuevoTipo

def modTamaño(proceso, nuevoTamaño):
    proceso[3] = nuevoTamaño

def modPrioridad(proceso, nuevoPrioridad):
    proceso[4] = nuevoPrioridad

def modFYH(proceso, nuevoFYH):
    proceso[5] = nuevoFYH

def asignarProceso(proceso1,proceso2):
    proceso2[0]=proceso1[0]
    proceso2[1]=proceso1[1]
    proceso2[2]=proceso1[2]
    proceso2[3]=proceso1[3]
    proceso2[4]=proceso1[4]
    proceso2[5]=proceso1[5]
