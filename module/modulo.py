from os import system
import json
from module.validate import menuNoValid
from module.data import modulo as modulo
from module.data import temario as temario

path = "module/storage/"
def carga():
    with open(path+"modulos.json", "r") as f:
        return json.loads(f.read())
       

def guardarModulo():
    print("""  
      ______________________
     /                     /
     /   GUARDAR   MODULO  /
     /_____________________/
     
    """)
    
   
        
        
    info = { 
            "codigo": input("Elija Un codigo para el modulo\n"),
        "nombre_modulo": input("Elija un nombre para el modulo\n"),
        "temario": [{
f"{'fijo' if (str(input('Ingrese los temarios')))else 'Temario'}":   
               (input(f'temario{x+1}: '))
        }
           for x in range(int(input("ingrese la cantidad de temas que va a ingresar:")))
         ],
        "prioridad": input("ingrese la prioridad")
        }    
    with open ("module/storage/modulos.json", "w") as f:
        data = json.dumps(info, indent=4)
        f.write(data)
        f.close()
    modulo.append(info)

def buscarModulo():

    system ("cls")
    print(f"""  
      ______________________
     /                     /
     /    BUSCAR MODULO    /
     /_____________________/""")
    for i, val in enumerate(modulo):
        temario = " "
        for valor in val.get('temario'):
            for key, value in valor.items():
                temario += f" {key} = {value}"

            
    for i,val in enumerate(modulo):
        print(f"""
______________________________________
Codigo: {val.get('codigo')}
Modulo: {val.get('nombre_modulo')}
temario: {temario}
prioridad:{val.get('prioridad')}
_______________________________________
 """)
    return "The module is available" 

def editarModulo():
    system ("cls")
    print("""  
      ______________________
     /                     /
     /    EDITAR MODULO    /
     /_____________________/
""")
    codigo = int(input("Ingrese el codigo del modulo que desea editar:\n"))
    print(f"""
_____________________________________________
                                             |
codigo: {codigo}                             |
Nombre: {modulo[codigo].get('modulo')} 
temario: {modulo[codigo].get('temario')}     |
   |
_____________________________________________|
""")
    print("¿Este es el camper que deseas actualizar?")
    print("1. Si")
    print("2. No")
    print("3. Salir")   
    opc = int(input())
    if (opc == 1): 
        info = {
           'Modulo': input("Ingrese el nombre dle modulo\n"),
            'Temario': input("Ingrese el temario\n")       
                           }
        modulo[codigo] = info
        with open("module/storage/modulos.json", "w") as f:
                data = json.dumps(modulo, indent=4)
                f.write(data)
                f.close()
        bandera = False
    elif(opc == 3):
            bandera = False
    return "modulo edited succesfully"
def eliminarModulo(): 
    bandera = True
    while(bandera):
        system("cls")
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
Temario: {temario}
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
     print("\t0.Salir")
     try: 
        opc = int(input())
     except ValueError:
      system("cls")
     match(opc):
             case 1: guardarModulo()
             case 2: editarModulo()
             case 3: buscarModulo()
             case 4 : eliminarModulo()
             case 0: 
                  system("cls")
                  bandera = False
    
    
    