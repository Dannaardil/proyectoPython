import json
from os import system 
from module.data import prueba as prueba
from .validate import menuNoValid
import module.camper as camper

def guardarResultados():
    print(""" 
          
          
        ______________________
         
         REGISTRAR RESULTADOS 
        ______________________
        
        
          
          """)
    notaTeorica = float(input("ingrese la nota de la prueba:\n"))
    notaPractica = float(input("ingrese la nota practica:\n"))
    promedio = (notaPractica+notaTeorica)/2
    info = {
        
        'notaTeorica': notaPractica , 
        'notaPractica': notaTeorica,
        'promedio': promedio
    }
    
    
    with open ("module/storage/prueba.json", "w") as f:
        data = json.dumps(info, indent=4)
        f.write(data)
        f.close()
    prueba.append(info) 
    
    
def listarResultados():
    system ("clear")
    print(f"""  
      ____________________________
     /                             /
     /    LISTADO DE RESULTADOS    /
     /____________________ ______ _/
          """)

            
    for i,val in enumerate(prueba):
        print(f"""
______________________________________

Nota practica: {val.get('notaTeorica')}
Nota practica : {val.get('notaPractica')}
promedio: {val.get('promedio')}

_______________________________________
 """)
    return "The camper is available"
   
def editarResultados():
    system ("clear")
    print("""  
      ______________________
     /                     /
     /    EDITAR MODULO    /
     /_____________________/
""")
    codigo = int(input("Ingrese el codigo del camper cuyos reultados desea editar:\n"))
    print(f"""
_____________________________________________
                                                   
codigo: {codigo}    
Nombre: {camper[codigo].get('Nombre')}       |
Apellido: {camper[codigo].get('Apellido')}                          
Nota Teorica: {notaTeorica[codigo].get('notaTeorica')} 
Nota practica: {notaTeorica[codigo].get('notaPractica')}    
   
____________________________________________      
""")
    print("¿Este es el camper que deseas actualizar?")
    print("1. Si")
    print("2. No")
    print("3. Salir")   
    opc = int(input())
    if (opc == 1): 
        info = {
           'notaTeorica': input("Ingrese la nota teorica\n"),
            'notaPractica': input("Ingrese la nota practica\n")       
                           }
        notaTeorica[codigo] = info
        with open("module/storage/prueba.json", "w") as f:
                data = json.dumps(notaTeorica, indent=4)
                f.write(data)
                f.close()
        bandera = False
    elif(opc == 3):
            bandera = False
    return "modulo edited succesfully"

def menuPrueba():
    bandera = True
    while(bandera):
   
        print(""" 
_________________________________________
                
////CRUD DE RESULTADOS
              PRUEBA DE ADMISION////
________________________________________
""")
        print("\t1. Registrar resultado prueba") 
        print("\t2. listar resultados")
        print("\t3. Actualizar resultados")
        print("\t4. Eliminar resultados")
        print("\t0. salir ")
        try: 
          opc = int(input())
        except ValueError:
            system("clear")
            continue
    
        match(opc):
             case 1: guardarResultados()
             case 2: listarResultados()
             case 0: 
                  system("clear")
                  bandera = False
             case _: menuNoValid(opc)
                 