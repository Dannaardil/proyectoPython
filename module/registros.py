from os import system
import json
import module.camper as camper
from module.data import resultadoSandbox
from module.validate import menuNoValid


def admision ():
    
    print("""  
          
         ______________________________
        |                              |
      |      RESULTADOS PRUEBA DE    |
       |          ADMISION             |
      |_______________________________|
    
    
          """)
    camper.edit()
    # pruebadmision = { 'pruebaLogica':input("ingrese la nota de la prueba de logica\n"), 
                 
    #                'pruebaProgramacion': input('ingrese la nota de la prueba de programacion\n')}
    # promedio =  sum(pruebadmision.values)/2
    # if promedio>=60:
    #         camper.info[5] = "Inscrito"
                
    
def notas():
    print("notas")
    
def areas():
    print("areas")
    
def matricula():
    print("matriculas")

def areas():
    print("areas")

def rutas():
    print("rutas")

def modulos():
    print("modulos")
    

            
         
       
    
    
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
