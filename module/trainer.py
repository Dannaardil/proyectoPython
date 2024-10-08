from os import system
import json
from .validate import menuNoValid
from .data import trainer as trainer2
from .data import camperIns, rutas, trainer as camperIns2, rutas

def asignarTrainer():
    with open("module/storage/camperIns.json", "r")as archivo:
        camperIns = json.load(archivo)
    with open ("module/storage/trainer.json", "r")as archivo:
        trainer = json.load(archivo)
    bandera = True
    while(bandera):
        system("cls")
        print(f"""
             ____________________________
              
              ASIGNAR TRAINER A CAMPER
             _______________________________
              
             ## (PARA ESTO EL CAMPER YA DEBE FIGURAR COMO INCRITO
              PRIMERO REGISTRAR PRUEBAS DE SANBOX)##
              
              """)
        for i , val in enumerate(camperIns2):
                   print(f"""
        codigo : {i}
        Nombre : {val.get('Apellido')}
        ID: {val.get('ID')}
        Estado: {val.get('Estado')}
        Ruta: {val.get('Ruta')}
                         """)
        codigo = int(input("ingrese el codigo del camper al que va a asignar un Trainer\n"))
        if codigo>=len(camperIns2):
            print("fuera de rango")
            continue
        camperInfo = camperIns
        print(f"""
              codigo: {codigo}
              Nombre: {camperIns2[codigo].get('Nombre')}
               Apellido: {camperIns2[codigo].get('Apellido')}
              ID: {camperIns2[codigo].get('ID')}
               Estado: {camperIns2[codigo].get('Estado')}
               Ruta: {camperIns2[codigo].get('Ruta')}
                        
              
              """)
        print("este es el camper al que desea asignar el trainer?")
        print("1. si")
        print("2.No")
        print("3.salir")
        opc= int (input())
        if(opc==1):
                  for i, val in enumerate(trainer):
                      print(f"""
                  codigo: {i}
                  Nombre: {val.get('Nombre')}
                  
                            
                  """)
                      codigoTrainer = int(input("Ingrese el codigo del trainer que vas a asignar\n"))
                      if codigoTrainer>=len(trainer2):
                          print("codigo de ruta")
                          continue
                      trainerSelect= trainer2[codigoTrainer]
                      print(f"""
                            codigo: {codigo}
                            Nombre: {trainer2[codigo].get('Nombre')}
                            Apellido: {trainer2[codigo].get('Apellido')}
                            Ruta: {trainer2[codigo].get('Ruta')}
                            """)
                      print("Esta es el trainer que deseas asignar?")
                      print("1. si")
                      print("2. no")
                      print("3. salir")
                      opc=int(input())
                      if (opc==1):
                            print("El trainer ha sido asignada.")
                            camperIns2[codigo]['Trainer']= trainerSelect
                            with open("module/storage/camperIns.json", "w") as file:
                                 json.dump(camperIns2, file, indent=4)
                            bandera=False
                      elif (opc==3):
                             bandera=False
    with open("module/storage/camperIns.json", "w") as file:
        json.dump(camperIns2, archivo, indent=4)
def save():
    system("cls")
    print("""
    ____________________________
          
    *  Formulario del trainer  *
    ____________________________
    """)
    info = {
        "Nombre": input("Ingrese el nombre del trainer\n"),
        "Apellido": input("Ingrese el apellido del trainer\n"),
       "numero de id": input("Ingrese el numero de id del trainer\n")
       ,"Ruta": 'No  hay ruta asignada'
       
    }
    trainer2.append(info)
    with open("module/storage/trainer.json", "w") as f:
        data = json.dumps(trainer2, indent=4)
        f.write(data)
        f.close()
    return "Sucessfully Trainer "
def edit():
    bandera=True
    while (bandera):
        system("cls")
        print("""
        ***************************
        * Acualizacion del trainer *
        ***************************
        """)
        codigo = int(input("Ingrese el codigo del trainer que deseas actualizar"))
        print(f"""
____________________________________________
Codigo: {codigo}
Nombre: {trainer2[codigo].get('Nombre')}
Apellido: {trainer2[codigo].get('Apellido')}
numero id: {trainer2[codigo].get('numero de id')}
Ruta: {trainer2[codigo].get('Ruta')}
_____________________________________________
""")
        print("¿Este es el trainer que deseas actualizar?")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            info = {
                "Nombre": input("Ingrese el nombre del trainer\n"),
                "Apellido": input("Ingrese el apellido del trainer\n"),
                 "numero de id": input("ingrese el numero de id\n")
                                 }
            trainer2[codigo]= info
            with open ("module/storage/trainer.json", "w") as f:
                 data = json.dumps(trainer2, indent= 4)
                 f.write(data)
                 f.close()
            bandera = False
        elif(opc == 3):
            bandera = False
        return  "Edit to trainer"


def search():
    system("cls")
    print("""
    ********************
    * Lista de trainers *
    ********************
    """)
    for i,val in enumerate(trainer2):
        print(f"""
_________________________________________
Codigo: {i}
Nombre: {val.get('Nombre')}
Apellido: {val.get('Apellido')}
Numero de id: {val.get('numero de id')}
Ruta: {val.get('Ruta')}
__________________________________________
        """)
    return "The trainer is available"
                
def delete():

    bandera = True
    while(bandera):
        system("cls")
        print("""
        ***************************
        * Eliminacion del trainer  *
        ***************************
        """)
        codigo = int(input("Ingrese el codigo del trainer que deseas eliminar: "))
        print(f"""
__________________________________________
              
Codigo: {codigo}
Nombre: {trainer2[codigo].get('Nombre')}
Apellido: {trainer2[codigo].get('Apellido')}
Numero de id: {trainer2[codigo].get ('numero de id')}
Ruta: {trainer2[codigo].get('Ruta')}
__________________________________________
        """)
        print("¿Este es el trainer que deseas actualizar?")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            trainer2.pop(codigo)
            with open("module/storage/trainer.json", "w") as f:
                data = json.dumps(trainer2, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif(opc == 3):
            bandera = False
    return "Trainer deleted"
def menu():
    bandera=True
    while (bandera):
        print("""
              
           __________________________
          |                         |
         |     CRUD del trainer   |
        |________________________|         
              
              """)
        print("\t1. Guardar trainer")
        print("\t2. Buscar trainer")
        print("\t3. Actualizar trainer")
        print("\t4. Eliminar trainer")
        print("\t5. Asignar trainer a camper")
        print("\t0. Atras")
        opc = int(input())
        match(opc):
            case 1: save()
            case 2: search()
            case 3: edit()
            case 4: delete()
            case 5: asignarTrainer()
            case 0:
                system("cls")
                bandera = False
            case _: menuNoValid(opc)