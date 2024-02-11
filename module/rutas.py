from os import system
import json
import module.camper as camper
from module.data import resultadoSandbox
from module.validate import menuNoValid
from module.data import ruta as ruta
import module.modulos as modulos
import module.prueba as prueba


path = "module/storage/"
def carga():
    with open(path+"ruta.json", "r") as f:
        return json.loads(f.read())
       

def guardarRuta ():
    system ("clear")
    print("""  
      ______________________
     /                     /
     /   GUARDAR   RUTA    /
     /_____________________/
     
    """)
    
   
        
        
    info = { 
            'Ruta': input("Ingrese el nombre de la ruta\n"),
       
    }    
    with open ("module/storage/ruta.json", "w") as f:
        data = json.dumps(info, indent=4)
        f.write(data)
        f.close()
    ruta.append(info)
   
    return "camper succesfully saved"
    
def buscarRuta():
    system ("clear")
    print(f"""  
      ______________________
     /                     /
     /    BUSCAR RUTA      /
     /_____________________/""")

            
    for i,val in enumerate(ruta):
        print(f"""
______________________________________
Codigo: {i}
Nombre de la ruta : {val.get('Ruta')}
_______________________________________
 """)
    return "The camper is available"
 
def editarRuta():
    system ("clear")
    print("""  
      ______________________
     /                     /
     /    EDITAR RUTA      /
     /_____________________/
""")
    codigo = int(input("Ingrese el codigo de la ruta que desea editar:\n"))
    print(f"""
_____________________________________________
                                            
codigo: {codigo}                             
Nombre: {ruta[codigo].get('Ruta')}           
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
            
        ruta[codigo] = info
        with open("module/storage/ruta.json", "w") as f:
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
        system("clear")
        print("""
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx
        x  ELIMINAR RUTA           x
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx
        """)
        codigo = int(input("Ingrese el codigo de la ruta que deseas eliminar\n"))
        print(f"""
______________________________________________
Codigo: {codigo}
Nombre De la ruta: {ruta[codigo].get('Ruta')}  
______________________________________________
        """)
        print("¿Esta es la ruta que deseas eliminar?")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            ruta.pop(codigo)
            with open("module/storage/ruta.json", "w") as f:
                data = json.dumps(ruta, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif(opc == 3):
            bandera = False
     return "ruta deleted"