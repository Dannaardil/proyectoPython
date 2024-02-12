from os import system 
import json
from .validate import menuNoValid
from .data import camper
from .data import estados as estados



  
def save (): 
   
    system ("cls")
    print("""  
      ______________________
     /                     /
     /   GUARDAR  CAMPER   /
     /_____________________/
     
    """)
    Edad=  int(input("ingrese la edad del camper\n"))
    acudiente  = ''
    if Edad<16:
        return print("""
                     
    X -----------------------------X
    X  NO PUEDE INGRESAR, NO TIENE X
    X      LA EDAD SUFICIENTE      X
    X -----------------------------X
                     
                     
                     """)
    elif Edad> 28:
        return print(" Exedes el limite de edad ")
    
    elif Edad >=16 and Edad<18:
        acudiente= input("Ingrese el nombre completo de su acudiente\n")
    elif Edad>=18:
        exit
  
        
        
    info = {
        "Nombre": input("Ingrese el nombre del camper\n"),
        "Apellido": input("Ingrese el apellido del camper\n")
        ,"Direccion": input("ingrese la direccion\n")
        , "Telefono": [
          {
            f"{'fijo' if (int(input('1. Fijo 2.Celular: '))==1) else 'Celular'}":   
               int(input(f'Numero de contacto {x+1}: '))
        }
           for x in range(int(input("ingrese la cantidad de telefonos que tiene: ")))
         ], 'Acudiente': acudiente,
             'Notaprueba': 'no hay notas de prueba',
             'Ruta': 'no hay ruta asignada',
             "Trainer":'no hay trainer',
             "Area de entrenamiento": 'aun no hay area',
             "fechaInicio": 'fechaInicio',
         'Estado': input("Elija el estado del camper:\n\t"+"\t".join([f"{estados.index(i)+1}. {i}\n" for i in (estados)]))
         ,"ID": input("ingrese el numero de identificacion del camper\n")
    }    
    
  
    
    
    if Edad<16:
        print()
    camper.append(info)
    with open ("module/storage/camper.json", "w") as f:
        data = json.dumps(camper, indent=4)
        f.write(data)
        f.close()
    return "camper succesfully saved"
def search ():
    system ("cls")
    print(f"""  
      ______________________
     /                     /
     /    BUSCAR CAMPER    /
     /_____________________/""")
 
    for i, val in enumerate(camper):
        telefonos = " "
        for valor in val.get('Telefono'):
            for key, value in valor.items():
                telefonos += f" {key} = {value}"
         
            
    for i,val in enumerate(camper):
        print(f"""
______________________________________
Codigo: {i}
Nombre: {val.get('Nombre')}
Apellido: {val.get('Apellido')}
Telefono : {telefonos}
Acudiente: {val.get('Acudiente')}
Estado: {val.get('Estado')}
numero de id: {val.get('ID')}
_______________________________________
 """)
    return "The camper is available"
 

def edit(): 
   
    
    system ("cls")
    print("""  
      ______________________
     /                     /
     /    EDITAR CAMPER    /
     /_____________________/
""")
    for i, val in enumerate(camper):
        telefonos = " "
        for valor in val.get('Telefono'):
            for key, value in valor.items():
                telefonos += f" {key} = {value}"
    codigo = int(input("Ingrese el codigo del camper que desea editar:\n"))
    print(f"""
_____________________________________________
                                             |
codigo: {codigo}                             |
Nombre: {camper[codigo].get('Nombre')}       |
Apellido: {camper[codigo].get('Apellido')}   |
Direccion: {camper[codigo].get('Direccion')} |
Telefono: {telefonos}                        |
Estado:   {camper[codigo].get('Estado ')} 
Acudiente: {camper[codigo].get('Acudiente')}
                                             |                  
Numero de id: {camper[codigo].get ('ID')}  
Notaprueba: no hay nota
Ruta: no hay ruta                 
Trainer: sin trainer
Area de entrenamiento: sin area              |
_____________________________________________|
""")
    print("¿Este es el camper que deseas actualizar?")
    print("1. Si")
    print("2. No")
    print("3. Salir")   
    opc = int(input())
    if (opc == 1): 
          Edad=  int(input("ingrese la edad del camper\n"))
    acudiente  = ''
    if Edad<16:
        return print("""
                     
    X -----------------------------X
    X  NO PUEDE INGRESAR, NO TIENE X
    X      LA EDAD SUFICIENTE      X
    X -----------------------------X
                     
                     
                     """)
    elif Edad> 28:
        return print(" Exedes el limite de edad ")
    
    elif Edad >=16 and Edad<18:
        acudiente= input("Ingrese el nombre completo de su acudiente\n")
    elif Edad>=18:
     exit
  
        
        
    info = {
        "Nombre": input("Ingrese el nombre del camper\n"),
        "Apellido": input("Ingrese el apellido del camper\n")
        ,"Direccion": input("ingrese la direccion\n")
        , "Telefono": [
          {
            f"{'fijo' if (int(input('1. Fijo 2.Celular: '))==1) else 'Celular'}":   
               int(input(f'Numero de contacto {x+1}: '))
        }
           for x in range(int(input("ingrese la cantidad de telefonos que tiene: ")))
         ], 'Acudiente': acudiente,
          
         
         "Estado": input("Elija el estado del camper:\n\t"+"\t".join([f"{estados.index(i)+1}. {i}\n" for i in (estados)]))
         ,"ID": input("ingrese el numero de identificacion del camper\n"), 
         "Notaprueba": 'no haynota',
         "Ruta": 'no hay ruta',
         "Trainer": 'no hay trainer',
         "Area de entrenamiento": "no hay area"
         
         
         }
      
            
    camper[codigo] = info
    with open("module/storage/camper.json", "w") as f:
                data = json.dumps(camper, indent=4)
                f.write(data)
                f.close()
                
    return "camper edited succesfully"

def delete():
    
    system("cls")
    print("""
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx
        x  ELIMINACION DEL CAMPER  x
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx
        """)
        
    for i, val in enumerate(camper):
        telefonos = " "
        for valor in val.get('Telefono'):
            for key, value in valor.items():
                telefonos += f" {key} = {value}"
        codigo = int(input("Ingrese el codigo del camper que deseas eliminar: "))
        print(f"""
______________________________________________
Codigo: {codigo}
Nombre: {camper[codigo].get('Nombre')}
Apellido: {camper[codigo].get('Apellido')}
Direccion: {camper[codigo].get('Direccion')}
Aduciente: {camper[codigo].get('Acudiente')}
Telefono: {telefonos}
Numero de id: {camper[codigo].get('ID')}
NAcudiente: {camper[codigo].get('NAcudiente')}
Estado: {camper[codigo].get('Estado')}
NotaPrueba: no hay nota
Ruta: no hay ruta
Trainer: no hay trainer
Area de entrenamiento: no hay area
______________________________________________
        """)
        print("¿Este es el camper que deseas eliminar?")
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
        else:
            delete()
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
        try: 
          opc = int(input())
        except ValueError:
            system("cls")
            continue
    
        match(opc):
             case 1: save()
             case 2: search()
             case 3: edit()
             case 4: delete()
             case 0: 
                  system("cls")
                  bandera = False
             case _: menuNoValid(opc)
                 