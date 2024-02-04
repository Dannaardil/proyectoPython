import json 
from os import system
from module.data import resultadoSandbox
from module.validate import menuNoValid


def admision (): 
    
    pruebaLogica = int(input("ingrese la nota de la prueba en el area de Logica\n"))
    pruebaProgramacion = int(input("Ingrese la nota de la prueba em el area de programacion\n"))
    promedioSandbox = pruebaLogica + pruebaProgramacion/2
    if promedioSandbox >= 60:
        Estado = "Inscrito"
         
       
    
    
def menu ():
    bandera = True 
    while (bandera):
    
       print("\t1.Registro de notas ")
       print("\t2.Registro resultados de admision")
       print("\t3.Registro de areas ")
       print("\t4.Registro de rutas ")
       print("\t5.Registro de modulos ")
       print("\t6.Registro de matricula")
       print("\t0.Salir")
       opc = int(input())
       match(opc):
           case 1: notas()
           case 2: admision()
           case 3: areas()
           case 4: rutas()
           case 5: modulos()
           case 6: matricula()
           case 0:
               system("clear")
               bandera = False
           case _: menuNoValid(opc)
