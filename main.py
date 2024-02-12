import json 
from os import system
import module.camper as camper 
import module.trainer as trainer
from module.validate import menuNoValid
import module.ruta as RUTA
import module.modulo as modulo
import module.prueba as Prueba
from module.data import modulos as modulos1
from module.data import rutas as rutas2
import module.data as data
import module.areas as areas

rutas= RUTA.carga()
modulos = modulo.carga()

def plantilla(data):
    lista = []
    for i,val in enumerate(data):
        lista.append(f"\n\t\t{i+1} - {val}")
    return "".join(lista)

def menuRutas():
    bandera = True
    while(bandera):
     print("""
       ________________________   
          
        REGISTRO DE RUTAS 
       _____________________---_ 
        
        
        """)
     print ("1.Crear una ruta y Asignar modulo a ruta")
     print ("2.Actualizar ruta")
     print ("3.Eliminar ruta")
     print ("4.buscar rutas")
     print("5.asignar ruta a camper")
     
     
     print("0.Salir")
     try: 
          opc = int(input())
     except ValueError:
         system("cls")
         continue
         
     
    
     match(opc):
             case 1:
                print("""  
                        ______________________
                        /                     /
                        /   CREAR   RUTA      /
                        /_____________________/
                        
                        """)
                
                info = { 
                                
                                "nombre_ruta": input("Ingrese el nombre de la ruta: "),
                                "modulo": asignarModulos()
                        
                        }    
                rutas2.append(info)
                with open ("module/storage/rutas.json", "w") as f:
                            data = json.dumps(info, indent=4)
                            f.write(data)
                            f.close()
                            
                return ("ruta saved")
   
             case 2:RUTA.editarRuta()
                
                
                
             case 3: RUTA.eliminarRuta()
             case 4: RUTA.buscarRuta()
             case 5: 
                 RUTA.asignacionRuta()
                    
             case 0: 
                  system("cls")
                  bandera = False
             case _: menuNoValid(opc)
           
def asignarModulos():
    # Temario: {"".join([f"{i} - {val}" for i,val in enumerate(val.get("temario"))])}
    selecion = set()
    
    while(True):
        for val in modulos1:
            print(f"""
            ________________
            Codigo: {val.get("codigo")}
            Nombre: {val.get("nombre_modulo")}
            Prioridad: {val.get("prioridad")}
            Temario: {plantilla(val.get("temario"))}
            ________________
            """)

        selecion.add(input("¿Selecione el modulo que deseas ingresando el codigo?\n"))
        if(not int(input("¿Deseas agregar otro modulo?\n1.SI\n0.NO\n"))):
            for i in selecion:
                for val in modulos1:
                   if(val.get("codigo") == i):
                        modulos1.append(val)
            break
    return modulos1
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
           case 1: print("EN PROCESO")
           case 2:Prueba.menuPrueba()
           case 3:areas.menuAreas()
           case 4:menuRutas()
           case 5:
               modulo.modulos()
           case 0:
               system("cls")
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
    print("\t1. Opciones de camper")
    print("\t2. Opciones de trainer ")
    print("\t3. Asignaciones/registros ")
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
                system("cls")
                camper.menu()
        case 2:
            with open("module/storage/trainer.json", "r") as f:
              trainer.trainer = json.loads(f.read())
              f.close()
              system("cls")
              trainer.menu()
        case 3:
            menuRegistros()
                       
        case 0:
            system("cls")
            bandera = False
        case _:
            menuNoValid(opc)




