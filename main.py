import json 
from os import system
import module.camper as camper 
import module.trainer as trainer
from module.validate import menuNoValid
import module.rutas as RUTA

def menuRegistros ():
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
           case 1: print("no")
           case 2:print("no")
           case 3: print("no")
           case 4: 
               with open("module/storage/ruta.json", "r") as f:
                RUTA.RUTA= json.loads(f.read())
                f.close()
                
               system("clear")
               
               RUTA.rutasMenu()
           case 5:print("no")
           case 0:
               system("clear")
               bandera = False
           case _: menuNoValid(opc)


def menu():
      
    print("""
          BIENVENIDO A... 
          

           _____________________________________
          |                                     |
          |>>Seguimiento Academico CampusLands<<|
          |_____________________________________|
          
          """)
    print("\t1. Info CAMPER ")
    print("\t2. Info TRAINER ")
    print("\t3. Registros ")
    print("\t4. Modulo de reportes")
    print("\t0.Salir")
bandera=True
while (bandera):
    menu()
    try: 
      opc = int(input())
    except ValueError:
        continue
   
    match(opc):
        case 1:
            
            with open("module/storage/camper.json", "r") as f:
                camper.camper = json.loads(f.read())
                f.close()
                system("clear")
                camper.menu()
        case 2:
            with open("module/storage/trainer.json", "r") as f:
              trainer.trainer = json.loads(f.read())
              f.close()
              system("clear")
              trainer.menu()
        case 3:
            menuRegistros()
                       
        case 0:
            system("clear")
            bandera = False
        case _:
            menuNoValid(opc)




