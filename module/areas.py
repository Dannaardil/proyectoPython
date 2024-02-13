from os import system
import json
from .validate import menuNoValid
from .data import areas as areas


def asignarArea():
    with open ("module/storage/camperIns.json", "r") as archivo:
        camperIns=json.load(archivo)
    with open("module/storage/areas.json", "r") as archivo:
        areas = json.load(archivo)
    bandera = True
    while(bandera):
        system("cls")
        print(f"""
        _____________________________________   
              
         ////   ASIGNACION DE AREAS ///
        _____________________________________
              
              
              """)
        for i, val in enumerate(camperIns):
                 print(f"""
        codigo: {i}
        Nombre: {val.get('Nombre')}
        Apellido: {val.get('Apellido')}
        ID: {val.get('ID')}
        Estado: {val.get('Estado')}
        Area de Entrenamiento: {val.get('Area de Entrenamiento')}               
       """)
        codigo = int(input("Ingrese el codigo del camper al que le va a asignar el area"))         
        if codigo>=len(camperIns):
            print("Fuera de rango")
            continue
        camperInfo = camperIns
        print(f"""
              codigo_ {codigo}
              Nombre: {camperIns[codigo].get('Nombre')}
              Apellido: {camperIns[codigo].get('Apellido')}
              ID: {camperIns[codigo].get('ID')}
              Estado: {camperIns[codigo].get('Estado')}
              Area de Entrenamiento: {camperIns[codigo].get('Area de entrenamiento')}
              
              
              """)
        print("Este es el camper al que deseas asignrle  un area de entrenamiento?")
        print("1.si")
        print("2.No")
        print("3.salir")
        opc=int(input())
        if (opc==1):
                    for i, val in enumerate(areas):
                        print(f"""
                    codigo: {i}
                    Area de entrenamiento: {val.get('Area de entrenamiento')}         
                    capacidad: {val.get('capacidad')}          
                              
                              """)
                        codigoArea = int(input("Ingrese el codigo del area de entrenamiento\n"))
                        if codigoArea>=len(areas):
                            print("Codigo fuera de rango")
                            continue
                        areaseleccionada = [codigoArea]
                        print(f"""
                              codigo: {codigo}
                              Nombre: {areas[codigo].get('Nombre')}
                              """)
                        print("Es esta el area que deseas asignar? ")
                        print('1.si')
                        print('2.no')
                        print('3.salir')
                        opc = int(input())
                        if (opc==1):
                            print("El area de entrenamiento fue asignada")
                            camperIns[codigo]['Area de entrenamiento']= areaseleccionada
                            with open ("module/storage/camperIns.json", "w") as archivo:
                                json.dump(camperIns, archivo, indent= 4)
                            bandera = False
                        elif(opc==3):
                            bendera=False
    with open("module/storage/CamperIns.json", "w")as archivo:
        json.dump(camperIns, archivo, indent= 4)
        
def save():           
    system("cls")
    print(""" 
          
          GUARDAR AREA
          
          """)
    info = {
        "Nombre": input("Ingrese el nombre del area para añadir"),
        "capacidad": int(input("Ingrese la capacidad del salon"))
    }    
    areas.append(info)    
    with open ("module/storage/areas.json", "w") as f:
        data = json.dumps(areas, indent=4)
        f.write(data)
        f.close()
        return "areas guardadas"

def search():
    system("cls")
    print("""
          
          BUSCAR AREA 
        
          """)
    for i, val in enumerate (areas):
        print(f""" 
              
_________________________________

codigo: {i}
Nombre: {val.get('Nombre')}
capacidad: {val.get('capacidad')}   
__________________________________           
              
              
              """)
        return "area esta disponible"

def edit():
    bandera = True
    while(bandera):
        system("cls")
        print(f"""
_________________

ACTUALIZAR AREA
_________________
            
              """)
        codigo= int(input("ingrese el codigo de area que va a editar\n"))
        print(f"""
_______________________________________
codigo: {codigo}
Nombres: {areas[codigo].get('Nombre')}
capacidad: {areas[codigo].get('capacidad')}
_________________________________________
 """) 
        print("Esta es el area que deseas actualizar?")
        print("1. si")
        print("2.No")
        print("3.salir")
        opc=int(input())
        if (opc==1):
            info = {
                "Nombre": input("Ingrese el nombre del area\n"),
                "capacidad": int(input("Ingrese la capacidad del area\n"))
                
                
                
            }
            areas[codigo]= info
            with open("module/storage/areas.json", "w") as f:
                data = json.dumps(areas, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif (opc==3):
            bandera= False
        return "area editada"
def delete():
    bandera = True 
    while(bandera):
        system("cls")
        print("""
              
              ELIMINAR AREA
              
              """)
        codigo = int(input("Ingrese el codigo del area que va a eliminar\n"))
        print(F"""
________________________________________
Codigo : {codigo}
Nombre: {areas[codigo].get('Nombre')}
capacidad: {areas[codigo].get('capacidad')}
______________________________________________              
              
              """)
        print("este es el area que quieres eliminar?\n")
        print("1.si")
        print("2.No")
        print("3.salir")
        opc= int(input())
        if (opc==1):
            areas.pop(codigo)
            with open ("module/storage/areas.json", "w")as f:
                data = json.dumps(areas, indent=4)
                f.write(data)
                f.close()
                bandera = False
        elif(opc==3):
            bandera = False
        return "Area eliminada"
    
def menuAreas():
    bandera = True
    while(bandera):
        print("""
              
             CRUD DE AREAS
              
              """)
        print("\t1. Registrar area")
        print("\t2. Buscar area")
        print("\t3. Actualizar area")
        print("\t4. Eliminar area")
        print("\t5. Asignar area a camper")
        print("\t0 salir")
        opc = int(input())
        match(opc):
            case 1: save()
            case 2: search()
            case 3: edit()
            case 4: delete()
            case 5: asignarArea()
            case 0:
                system("cls")
                bandera = False
            case _: menuNoValid(opc)