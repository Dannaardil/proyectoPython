import json 
from os import system
import module.camper as camper 
import module.trainer as trainer
from module.validate import menuNoValid
import module.ruta as RUTA
import module.modulo as modulos
import module.prueba as Prueba
from module.data import modulo as modulo
from module.data import rutas as rutas2
import module.data as data
import module.areas as areas
import module.horarios as horarios
import module.notas as notas

rutas= RUTA.carga()
modulos1 = modulos.carga()

def ListarCampersIns():
    with open("module/storage/camperIns.json", "r") as archivo:
        camper = json.load(archivo)
    system("cls")
    print("""
            ______________________
              
               CAMPERS INSCRITOS
            ______________________  
            
              """)
    for i, val in enumerate (camper):
            print(f"""
    ____________________________
    codigo: {i}
    nombre: {val.get('Nombre')}  
    Apellido: {val.get('Apellido')}
    ID: {val.get('ID')}
    Estado: {val.get('Estado')}  
    ________________________________          
                  
                  
                  """)

def ListarCampersAprobados():
    with open("module/storage/camperIns.json", "r") as archivo:
        camper = json.load(archivo)
    system("cls")
    print("""
            ______________________
              
               CAMPERS INSCRITOS
            ______________________  
            
              """)
    for i, val in enumerate (camper):
            print(f"""
    ____________________________
    codigo: {i}
    nombre: {val.get('Nombre')}  
    Apellido: {val.get('Apellido')}
    ID: {val.get('ID')}
    Estado: {val.get('Estado')}  
    Nota con la que aprobo: {val.get('Notaprueba')}
    ________________________________          
                  
                  
                  """)
            
def ListarTrainers():
    with open("module/storage/trainer.json", "r") as archivo:
        trainer = json.load(archivo)
    system("cls")
    print("""
            ______________________
              
                  TRAINERS 
            ______________________  
            
              """)
    for i, val in enumerate (trainer):
            print(f"""
    ____________________________
    codigo: {i}
    nombre: {val.get('Nombre')}  
    Apellido: {val.get('Apellido')}
    _____________________________
    """)
            

def menuReportes():
   bandera= True
   while(bandera):
    print("""
       ///////////////////   
        MODULO DE REPORTES  
       ///////////////////   
          """)
    print("\t1.Listar campers inscritos.")
    print("\t2.Listar campers aprobados.")
    print("\t3.Listar trainers.")
    print("\t0.salir.")
    try: 
        opc = int(input())
    except ValueError:
      system("cls")
    match(opc):
             case 1: ListarCampersIns()
             case 2: ListarCampersAprobados()
             case 3: ListarTrainers()
             case 0: 
                  system("cls")
                  bandera = False


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
     print ("1.Crear una ruta y Asignar modulo a ruta ✨")
     print ("2.Actualizar ruta")
     print ("3.Eliminar ruta")
     print ("4.buscar rutas")
     print("5.asignar ruta a CAMPER")
     print("5.asignar ruta a TRAINER")
     
     
     
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
                            f.write(json.dumps(rutas2, indent=4))
                            f.close()
                            
                return ("ruta saved")
   
             case 2:RUTA.editarRuta()
                
                
                
             case 3: RUTA.eliminarRuta()
             case 4: RUTA.buscarRuta()
             case 5: 
                 RUTA.asignacionRuta()
             case 6: 
                 RUTA.asignacionRutaTrainer()
                    
             case 0: 
                  system("cls")
                  bandera = False
             case _: menuNoValid(opc)
           
def asignarModulos():
    # Temario: {"".join([f"{i} - {val}" for i,val in enumerate(val.get("temario"))])}
    selecion = set()
    nuevaLista= []
    while(True):
        
        selecion = set()
        nuevaLista = []
        for val in modulo:
            print(f"""
            _________________________________
            
            Codigo: {val.get("codigo")}
            Nombre: {val.get("nombre_modulo")}
            Prioridad: {val.get("prioridad")}
            Temario: {(val.get("temario"))}
            ___________________________________
            """)

        selecion.add(input("¿Selecione el modulo que deseas ingresando el codigo?\n"))
        if(not int(input("¿Deseas agregar otro modulo?\n1.SI\n0.NO\n"))):
            for i in selecion:
                for val in modulo:
                   if(val.get("codigo") == i):
                        modulo.append(val)
            break
    return modulo
def menuRegistros ():
    bandera = True 
    while (bandera):
        print("""
           ______--------_-----______------__
           
             BIENVENIDO A <<< REGISTROS Y 
                   ASIGNACIONES >>>>>
                   
           ___----____---_---_-_---_---___-- _
              """)
    
        print("\t1.Notas de modulos")
        print("\t2.Prueba de admision")
        print("\t3.Areas(crud/asignaciones) ")
        print("\t4.Rutas(crud/asignaciones)")
        print("\t5.Modulos(crud/asignaciones) ")
        print("\t6.Horario(crud/asignaciones)")
        print("\t7.Matricula")
        print("\t0.Salir")
        opc = int(input())
        match(opc):
           case 1: notas.pruebaFundamentos()
           case 2:Prueba.menuPrueba()
           case 3:areas.menuAreas()
           case 4:menuRutas()
           case 5:
               modulos.modulos()
           case 6:
                horarios.menu()
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
    print("\t3. Asignaciones/registros/cruds ")
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
              trainer.trainer2 = json.loads(f.read())
              f.close()
              system("cls")
              trainer.menu()
        case 3:
            menuRegistros()
        case 4: 
            menuReportes()
            
                       
        case 0:
            system("cls")
            bandera = False
        case _:
            menuNoValid(opc)




