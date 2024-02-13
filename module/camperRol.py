from os import system
import json
path = "module/storage/"
def verNotaPrueba():
    with open (path+"camperIns.json", "r") as archivo:
        camperIns = json.load (archivo)
    bandera = True
    while (bandera):
        system('cls')
        print("""
              
          /// Visualizar notas de admision ///
              
              
        """)
        for i, val in enumerate(camperIns):
            print(f"""
        codigo: {i}
        Nombre: {val.get('Nombre')}
        Apellido: {val.get('Apellido')}
        ID: {val.get('ID')}
        Estado: {val.get('ID')}  
             
                  
                  
                  """)
        codigo = int(input( "ingrese el codigo del camper para ver su prueba de admision\n"))
        camperInfo = camperIns[codigo]
        print(f"""
              
            codigo: {codigo}
            Nombre: {camperIns[codigo].get('Nombre')}
            Apellido: {camperIns[codigo].get('Apellido')}
            ID: {camperIns[codigo].get('ID')}
            Estado: {camperIns[codigo].get('Estado')}
              
              
              
              
              """)
        print("Este eres tú?")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc=int(input())
        if (opc==1): 
            print(f"""
                  
            codigo: {codigo}
            Nombre: {camperIns[codigo].get('Nombre')}
            Apellido: {camperIns[codigo].get('Apellido')}
            notaPrueba: {camperIns[codigo].get('Notaprueba')}
            
                  
                  
                  
                  """)        
        elif (opc==3):
            bandera = False