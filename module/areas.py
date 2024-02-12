from os import system
import json
from .validate import menuNoValid
from .data import areas

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
        print("\t0 salir")
        opc = int(input())
        match(opc):
            case 1: save()
            case 2: search()
            case 3: edit()
            case 4: delete()
            case 0:
                system("cls")
                bandera = False
            case _: menuNoValid(opc)