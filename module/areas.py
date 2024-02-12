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
        opc=(int(input))
        if (opc==1):
            info = {
                "Nombre": input("Ingrese el nombre del area\n"),
                "capacidad": int(input("Ingrese la capacidad del area\n"))
                
                
                
            }
    