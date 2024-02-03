from os import system 
import json
from .validate import menuNoValid
from .data import camper

def save (): 
    system ("clear")
    print("""  
      ______________________
     /                     /
     /   GUARDAR  CAMPER   /
     /_____________________/
    """)
    info = {
        "Nombre": input("Ingrese el nombre del camper\n"),
        "Apellido": input("Ingrese el apellido del camper\n")
        ,"Direccion": input("ingrese la direccion\n")
        ,"Acudiente": input("acudiente (opcional)????")
         ,"Estado" : input("Ingrese el estado del camper\n") #v?
    }
    
    camper.append(info)
    with open ("module/storage/camper.json", "w") as f:
        data = json.dumps(camper, indent=4)
        f.write(data)
        f.close()
    return "camper succesfully saved"



def search ():
    system ("clear")
    print(f"""  
      ______________________
     /                     /
     /    BUSCAR CAMPER    /
     /_____________________/""")
    
    for i,val in enumerate(camper):
        print(f"""
________________________
Codigo: {i}
Nombre: {val.get('Nombre')}
Apellido: {val.get('Apellido')}
Edad: {val.get('Edad')}
Genero: {val.get('Genero')}
________________________
 """)
    return "The camper is available"

   
def edit():
    system ("clear")
    print("""  
      ______________________
     /                     /
     /    EDITAR CAMPER    /
     /_____________________/
""")
    codigo = int(input("Ingrese el codigo del camper que desea editar:\n"))
    print(f"""
_____________________________________________
                                             |
codigo: {codigo}                             |
Nombre: {camper[codigo].get('Nombre')}       |
Apellido: {camper[codigo].get('Apellido')}   |
Direccion: {camper[codigo].get('Direccion')} |      
Estado: {camper[codigo].get('Estado')}       |
_____________________________________________|
""")
    print("¿Este es el camper que deseas actualizar?")
    print("1. Si")
    print("2. No")
    print("3. Salir")   
    opc = int(input())
    if (opc == 1): 
        info = {
            "Nombre": input("Ingrese el nombre del camper\n"),
            "Apellido": input("Ingrese el apellido del camper\n"),
            "Direccion": input("ingrese la direccion\n")
            ,"Acudiente": input("acudiente (opcional)????")
            ,"Estado" : input("Ingrese el estado del camper\n") #v?
        }
        camper[codigo] = info
        with open("module/storage/camper.json", "w") as f:
                data = json.dumps(camper, indent=4)
                f.write(data)
                f.close()
        bandera = False
    elif(opc == 3):
            bandera = False
    return "camper edited succesfully"

def menu():
     bandera = True
     while(bandera):
        print(""" 
_______________________
                
////CRUD DEL CAMPER////
_______________________
""")
        print("\t1. Registrar camper") 
        print("\t2. Buscar camper")
        print("\t3. Actualizar camper")
        opc = int(input())
        match(opc):
             case 1: save()
             case 2: search()
             case 3: edit()
             case 0: 
                  system("clear")
                  bandera = False
             case _: menuNoValid(opc)
                 