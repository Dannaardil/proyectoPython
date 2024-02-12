from os import system
import json
import module.camper as camper
from module.data import resultadoSandbox
from module.validate import menuNoValid
from module.data import rutas as ruta
import module.modulo as modulo
import module.prueba as prueba

# def notas():
#     print("notas")
    
    
# def matricula():
#     print("matriculas")

# def areas():
#     print("areas")
def guardarRuta ():
    system ("cls")
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
    system ("cls")
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
    system ("cls")
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
def rutasMenu():
    bandera = True
    while(bandera):
     print("""
       ________________________   
          
        REGISTRO DE RUTAS 
       _____________________---_ 
        
        
        """)
     print ("1.Guardar ruta")
     print ("2.Actualizar ruta")
     print ("3.Eliminar ruta")
     print ("4.buscar rutas")
     print("0.Salir")
     try: 
          opc = int(input())
     except ValueError:
         system("cls")
         continue
         
     
    
     match(opc):
             case 1:guardarRuta()
             case 2: editarRuta()
             case 3: eliminarRuta()
             case 4: buscarRuta()
             case 0: 
                  system("cls")
                  bandera = False
             case _: menuNoValid(opc)
                 


    

            
         
       
    
    

