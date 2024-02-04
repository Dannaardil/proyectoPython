import json 
from os import system
import module.camper as camper 
import module.registros as registros
import module.trainer as trainer
from module.validate import menuNoValid


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
    opc = int(input())
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
            with open ("module/storage/registros.json", "r") as f:
                registros.registros = json.loads(f.read())
                f.close
               
                registros.menu()
                       
        case 0:
            system("clear")
            bandera = False
        case _:
            menuNoValid(opc)



