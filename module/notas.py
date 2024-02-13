import json
from os import system

def pruebaModulo():
    with open("module/storage/camperIns.json", "r")as archivo:
        camperIns = json.load(archivo)
    with open ("module/storage/notas.json", "r")as archivo:
        notas = json.load(archivo)
    bandera = True 
    while(bandera):
        system("cls")
        print("""
            ______________________
              
               ASIGNAR NOTAS
            ______________________  
            
              """)
      

        for i, val in enumerate(camperIns):
                print(f"""
                      """)

        
        codigo= int("Ingrese el codigo del camper al que le va a asignar la nota:\n")
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
        print("¿Este es el camper al que deseas asignarle la nota?")
        print("1.Si")
        print("2.No")
        print("3.salir")
        opc= int(input())
        if(opc==1):
                    for i, val in enumerate(notas):
                      print(f"""
                            
                     codigo: {i}
                     Horario: {val.get('horario')}
   
                            """)
                    codigoNota=int(input("Ingrese el codigo del horario que deseas asignar:\n"))
                    if codigoNota>=len(notas):
                        print("FUERA RANGO")
                        continue
                    notaSelect= notas[codigoNota]
                    print(f"""
                          
                          
                          codigo: {codigo}
                          Nota modulo: {notas[codigo].get('notaPrueba')}
                          
                          
                          """)
                    print("¿Es este el horario que quieres asignar?")
                    print("1.si")
                    print("2.no")
                    print("3.salir")
                    opc=int(input())
                    if (opc==1):
                        print("El horario se asigno exitosamente!!")
                        camperIns[codigo]['notaPrueba']= notaSelect
                        with open("module/storage/camperIns.json", "w")as archivo:
                            json.dump(camperIns,archivo, indent=4)
                        bandera= False
                    elif(opc==3):
                        bandera=False  
    with open("module/storage/camperIns.json", "w")as archivo:
          json.dump(camperIns, archivo, ident=4)