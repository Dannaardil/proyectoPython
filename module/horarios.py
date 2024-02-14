from os import system 
import json
from .data import horario
from .validate import menuNoValid

def asirgnarHorario():
    with open("module/storage/camperIns.json", "r") as archivo:
        camperIns= json.load(archivo)
    with open("module/storage/horarios.json", "r")as archivo:
        horario = json.load(archivo)
    bandera=True
    while (bandera):
        system("cls")
        print("""
            ______________________
              
               ASIGNAR HORARIO
            ______________________  
            
              """)
        for i, val in enumerate(camperIns):
                print(f"""
                      
         codigo: {i}
         Nombre:{val.get('Nombre')}
         Apellido: {val.get('Apellido')} 
         ID: {val.get('ID')}
         Estado: {val.get('Estado')}
         Ruta: {val.get('Ruta')}                  
                      
                      """)
        
        codigo= int(input("Ingrese el codigo del camper al que le va a asignar el horario:\n"))
        if codigo>=len(camperIns):
            print("FUERA DE RANGO")
            continue
        camperInfo = camperIns
        print(f"""
              
            codigo: {codigo}
            Nombre{camperIns[codigo].get('Nombre')}
            Apellido: {camperIns[codigo].get('Apellido')}
            ID: {camperIns[codigo].get('ID')}
            Estado: {camperIns[codigo].get('Estado')}
            Ruta: {camperIns[codigo].get('Ruta')}
              
              """)
        print("¿Este es el camper al que deseas asignarle horario?")
        print("1.Si")
        print("2.No")
        print("3.salir")
        opc= int(input())
        if(opc==1):
                    for i, val in enumerate(horario):
                      print(f"""
                            
                     codigo: {i}
                     Horario: {val.get('horario')}
   
                            """)
                    codigoHorario=int(input("Ingrese el codigo del horario que deseas asignar:\n"))
                    if codigoHorario>=len(horario):
                        print("FUERA RANGO")
                        continue
                    horaSelect= horario[codigoHorario]
                    print(f"""
                          
                          
                          codigo: {codigo}
                          horario: {horario[codigo].get('Horario')}
                          
                          
                          """)
                    print("¿Es este el horario que quieres asignar?")
                    print("1.si")
                    print("2.no")
                    print("3.salir")
                    opc=int(input())
                    if (opc==1):
                        print("El horario se asigno exitosamente!!")
                        camperIns[codigo]['horario']= horaSelect
                        with open("module/storage/camperIns.json", "w")as archivo:
                            json.dump(camperIns,archivo, indent=4)
                        bandera= False
                    elif(opc==3):
                        bandera=False  
    with open("module/storage/camperIns.json", "w")as archivo:
          json.dump(camperIns, archivo, indent=4)                    
def save():
    
    system("cls")
    print("""
          
        REGISTRO HORARIO  
          
          """)
    info = {
        "Horario": input("Ingrese el horario que deseas registrar.\n")   
    }
    horario.append(info)
    with open("module/storage/horarios.json", "w" )as f: 
        data = json.dumps(horario, indent=4)
        f.write(data)
        f.close()
    return " camper guardado"

def edit():
    bandera = True
    while(bandera):
        system("cls")
        print(""" 
            ________________________  
              
              ACTUALIZAR HORARIOS
            _________________________ 
              
              """)
        codigo = int(input("Ingrese el codigo del horario que desea actualizar:\n"))
        print(f"""
              
___________________________________________
codigo: {codigo}     
Horario: {horario[codigo].get('Horario')}
____________________________________________
      """)
        print("¿Este es el horario que quieres editar? ")
        print("1.si")
        print("2.No")
        print("3.Salir")
        opc= int(input())
        if (opc==1):
            info = {
                "Horario": input("Ingrese el horario nuevo:\n")
                
            }
            horario[codigo]=info
            with open("module/storage/horarios.json", "w") as f:
                data = json.dumps(horario, indent=4)
                f.write(data)
                f.close()
            bandera=False
        elif(opc==3):
            bandera=False
    return "horario actualizado"
        
def search():
    
   
    horarios_disponibles = []
    print("""
          TODOS LOS HORARIOS -->
          """)
    for i, val in enumerate(horario):
        horario_texto = val.get('Horario')
        print(f"""
    ______________________________
    codigo: {i}
    Horario: {horario_texto}
    ______________________________
              """)
        horarios_disponibles.append(horario_texto)
    return horarios_disponibles


def delete():
    bandera= True
    while(bandera):
        system("cls")
        print("""
            ///////////////////  
             ELIMINAR HORARIO 
            //////////////////
              """)
        codigo= int(input("Ingrese el codigo de el horario que desea eliminar\n"))
        print(f"""
__________________________________________  
            
codigo: {codigo}
Horario: {horario[codigo].get('Horario')}            
__________________________________________   
              """)
        print("¿Este es el horario que desea eliminar?")
        print("1.Si")
        print("2.No")
        print("3.salir")
        opc= int(input())
        if(opc==1):
            horario.pop(codigo)
            with open ("module/storage/horarios.json", "w") as archivo:
                data= json.dumps(horario, indent=4)
                archivo.write(data)
                archivo.close()
            bandera = False
        elif(opc==3):
            bandera=False
    return "se elimino el horario"                

def menu():
    bandera = True
    while(bandera):
        system("cls")
        print("""
     
    _________________________ 
            
    /////CRUD DE HORARIOS///
    __________________________
              """)
        print("\t1. Registrar horario")
        print("\t2. listar horarios")
        print("\t3. Actualizar horarios")
        print("\t4. Eliminar horario")
        print("\t5. Asignar horario")
        print("\t0. salor")
        opc= int(input())
        match(opc):
            case 1: save()
            case 2: 
                horarios = search()
                for horario in horarios:
                    print(horario)
            case 3: edit()
            case 4: delete()
            case 5: asirgnarHorario()
            case 0: 
                 system("cls")
                 bandera= False
            case _ : menuNoValid(opc)