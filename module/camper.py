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
        , "Telefono": [
          {
            f"{'fijo' if (int(input('1. Fijo 0.Celular: '))==1) else 'Celular'}":   
               int(input(f'Numero de contacto {x+1}: '))
        }
           for x in range(int(input("ingrese la cantidad de telefonos que tiene: ")))
         ]
         ,'Edad': input("ingrese la edad del camper\n"), 
         'Estado': "Preinscrito"
         ,"ID": input("ingrese el numero de identifiacion del camper\n")
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
______________________________________
Codigo: {i}
Nombre: {val.get('Nombre')}
Apellido: {val.get('Apellido')}
Telefono : {val.get('Telefono')}
Estado: {val.get('Estado')}
numero de id: {val.get('ID')}
_______________________________________
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
Telefono: {camper[codigo].get('Telefono')}
Estado:   {camper[codigo].get('Estado ')}          |                   |
Numero de id: {camper[codigo].get ('ID')}    |
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
            "Telefono": [{
            f"{'fijo' if (int(input('1. Fijo 0.Celular: '))==1) else 'Celular'}":   
               int(input(f'Numero de contacto {x+1}: '))
        }
           for x in range(int(input("ingrese la cantidad de telefonos que tiene: ")))
         ]
            ,"Direccion": input("ingrese la direccion\n")
            ,"Acudiente": input("acudiente (opcional)????")
            ,"Estado" : input("Ingrese el estado del camper\n") #v?
             ,"ID" : input("ingrese el numero de identificacion\n")
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

def delete():
     bandera = True
     while(bandera):
        system("clear")
        print("""
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx
        x  ELIMINACION DEL CAMPER  x
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx
        """)
        codigo = int(input("Ingrese el codigo del camper que deseas eliminar: "))
        print(f"""
______________________________________________
Codigo: {codigo}
Nombre: {camper[codigo].get('Nombre')}
Apellido: {camper[codigo].get('Apellido')}
Direccion: {camper[codigo].get('Direccion')}
Telefono: {camper[codigo].get('Telefono')}
Numero de id: {camper[codigo].get('ID')}
______________________________________________
        """)
        print("¿Este es el camper que deseas actualizar?")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            camper.pop(codigo)
            with open("module/storage/camper.json", "w") as f:
                data = json.dumps(camper, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif(opc == 3):
            bandera = False
     return "Camper deleted"

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
        print("\t4. Eliminar camper")
        print("\t0. salir ")
        opc = int(input())
        match(opc):
             case 1: save()
             case 2: search()
             case 3: edit()
             case 4: delete()
             case 0: 
                  system("clear")
                  bandera = False
             case _: menuNoValid(opc)
                 