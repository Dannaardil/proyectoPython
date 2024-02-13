from os import system
import json
import module.camper as camper
from module.data import resultadoSandbox
from module.validate import menuNoValid
from module.data import rutas as rutas1
import module.modulo as modulo
import module.prueba as prueba
from module.data import modulo as modulo


path = "module/storage/"
def carga():
    with open(path+"rutas.json", "r") as f:
        return json.loads(f.read())
       
       


    
    
def buscarRuta():
    system ("cls")
    print(f"""  
      ______________________
     /                     /
     /    BUSCAR RUTA      /
     /_____________________/""")

    with open ("module/storage/rutas.json", "r") as archivo:
        rutas= json.load(archivo)    
    for i,val in enumerate(rutas1):
        print(f"""
______________________________________
codigo: {i}
nombre de la ruta: {val.get('nombre_ruta')}
modulo: {val.get('modulo')}
______________________________________
 """)
    return "The camper is available"
 
def asignacionRuta():
    with open("module/storage/camperIns.json", "r") as archivo:
        camperIns=json.load(archivo)
    with open ("module/storage/rutas.json", "r") as archivo:
        rutas= json.load(archivo)
    bandera = True
    while(bandera):
        system("cls")
        print(f"""
             ______________________
              
              ASIGNACION DE RUTAS
             ______________________
            
            """)
        for i, val in enumerate(camperIns): 
                  print(f"""
        codigo: {i}
        Nombre: {val.get('Nombre')}
        Apellidos: {val.get('Apellido')}
        ID: {val.get('ID')}
        Estado: {val.get('Estados')}
        Ruta: {val.get('Ruta')}
                        
                        
                        """)
        codigo = int(input("Ingrese el codigo del camper al que desea asignar un ruta:  "))
        if codigo>=len(camperIns):
            print("codigo no valido")
            continue
        camperInfo = camperIns
        print(f""" 
              codigo: {codigo}
              Nombre: {camperIns[codigo].get('Nombre')}
              Apellido: {camperIns[codigo].get('Apellido')}
              ID : {camperIns[codigo].get('ID')}
              Estado: {camperIns[codigo].get('Estado')}
              Ruta: {camperIns[codigo].get('Ruta')} 
                           
              """)
        print("este es el camper que al que desea asignerle una ruta??")
        print("1. si")
        print("2. no")
        print("3.salir")
        opc = int(input())
        if(opc==1): 
                 for i, val in enumerate(rutas):
                     print(f"""
                 codigo: {i}
                 Nombre: {val.get('Nombre')}
                """)
                     codigoRuta=int(input("ingrese el codigo de la ruta que desea asignar\n"))
                     if codigoRuta>=len(rutas):
                         print("opcion fuera de rango")
                         continue
                     rutaSeleccionada = rutas[codigoRuta]
                     print(f""" 
                            codigo: {codigo}
                            Nombre: {rutas[codigo].get('Nombre')}
                           """)  
                     print("Esta es la ruta que vas a asignar?")
                     print("1.si")
                     print("2.No")
                     print("3.salir")
                     opc = int(input())
                     if (opc==1):
                         print("La ruta fue asignada\n")
                         rutas[codigo]['Ruta']= rutaSeleccionada
                         with open("module/storage/camperIns.json", "w") as archivo:
                             json.dump(camperIns, archivo, indent=4)
                         bandera = False
                     elif (opc==3):
                         bandera=False
    with open ("module/storage/camperIns.json", "w") as archivo:
        json.dump(rutas, archivo, indent=4)   
                               
def editarRuta():          
    system ("cls")
    print("""  
      ______________________
     /                     /
     /    EDITAR RUTA      /
     /_____________________/
""")
    with open ("module/storage/rutas.json", "r") as archivo:
        rutas= json.load(archivo)
    codigo = int(input("Ingrese el codigo de la ruta que desea editar:\n"))
    print(f"""
_____________________________________________
                                            
codigo: {codigo}                             
Nombre: {rutas[codigo].get('nombre_ruta')}           
_____________________________________________
""")
    print("¿Esta es la ruta que deseas actualizar?")
    print("1. Si")
    print("2. No")
    print("3. Salir")   
    opc = int(input())
    if (opc == 1): 
        info = {
        "Ruta": input("Ingrese el nombre de la ruta\n")}
            
        rutas1[codigo] = info
        with open("module/storage/rutas.json", "w") as f:
                data = json.dumps(info, indent=4)
                f.write(data)
                f.close()
        bandera = False
    elif(opc == 3):
            bandera = False
    return "ruta edited succesfully"

def eliminarRuta():
     bandera = True
     while(bandera):
        system("cls")
        print("""
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx
        x  ELIMINAR RUTA           x
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx
        """)
        codigo = int(input("Ingrese el codigo de la ruta que deseas eliminar\n"))
        print(f"""
______________________________________________
Codigo: {codigo}
Nombre De la ruta: {rutas1[codigo].get('nombre_ruta')}  
______________________________________________
        """)
        print("¿Esta es la ruta que deseas eliminar?")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            rutas1.pop(codigo)
            with open("module/storage/rutas.json", "w") as f:
                data = json.dumps(rutas1, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif(opc == 3):
            bandera = False
     return "ruta deleted"