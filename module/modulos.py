from os import system
import json
from module.validate import menuNoValid
from module.data import modulo as modulo

def guardarModulo():
    print("""  
      ______________________
     /                     /
     /   GUARDAR   MODULO  /
     /_____________________/
     
    """)
    
   
        
        
    info = { 
            'Modulo': input("Ingrese el nombre de el modulo\n")
       
    }    
    with open ("module/storage/modulo.json", "w") as f:
        data = json.dumps(info, indent=4)
        f.write(data)
        f.close()
    modulo.append(info)

def buscarModulo():
    system ("clear")
    print(f"""  
      ______________________
     /                     /
     /    BUSCAR MODULO    /
     /_____________________/""")

            
    for i,val in enumerate(modulo):
        print(f"""
______________________________________
Codigo: {i}
Nombre: {val.get('Modulo')}
_______________________________________
 """)
    return "The module is available" 
def eliminarModulo(): 
    bandera = True
    while(bandera):
        system("clear")
        print("""
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx
        x  ELIMINAR MODULO         x
        xxxxxxxxxxxxxxxxxxxxxxxxxxxx
        """)
        codigo = int(input("Ingrese el codigo de el modulo que deseas eliminar\n"))
        print(f"""
______________________________________________
Codigo: {codigo}
Nombre De la ruta: {modulo}
______________________________________________
        """)
        print("¿Esta es la ruta que deseas eliminar?")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            modulo.pop(codigo)
            with open("module/storage/modulos.json", "w") as f:
                data = json.dumps(modulo, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif(opc == 3):
            bandera = False
        return "module deleted"

def modulos():
    bandera = True
    while(bandera):
     print("""
        _________________________  
            
            CRUD DE MODULOS
        ________________________  
          
          
          """)
    
    print("\t1.Guardar Modulo")
    print("\t2.Editar modulo")
    print("\t3.Buscar Modulo")
    print("\t4.Eliminar Modulo")
    try: 
        opc = int(input())
    except ValueError:
     system("clear")
    match(opc):
             case 1: print("no")
             case 0: 
                  system("clear")
                  bandera = False
    
    