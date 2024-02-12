import json
from os import system 
from module.data import prueba as prueba
from .validate import menuNoValid
import module.camper as camper

def guardarResultados():
    print(""" 
          
          
        ______________________
         
         REGISTRAR RESULTADOS 
        ______________________
        
        
          
          """)
    notaTeorica = float(input("ingrese la nota de la prueba:\n"))
    notaPractica = float(input("ingrese la nota practica:\n"))
    promedio = (notaPractica+notaTeorica)/2
    info = {
        
        'notaTeorica': notaPractica , 
        'notaPractica': notaTeorica,
        'promedio': promedio
    }
    
    
    with open ("module/storage/prueba.json", "w") as f:
        data = json.dumps(info, indent=4)
        f.write(data)
        f.close()
    prueba.append(info) 
    
    

def menuPrueba():
    with open("module/storage/camper.json", "r") as archivo:
        camper = json.load(archivo)
        
    bandera = True
    while(bandera):
        system("cls")
        print(f""" 
_________________________________________
                
////CRUD DE RESULTADOS
              PRUEBA DE ADMISION////
________________________________________
        """)
        for i, val in enumerate (camper):
            print(f"""
    ____________________________
    codigo: {i}
    nombre: {val.get('Nombre')}  
    Apellido: {val.get('Apellido')}
    ID: {val.get('ID')}
    Estado: {val.get('Estado')}            
                  
                  
                  """)
        codigo = int(input("Ingrese el codigo del camper al que deseas asignarle la nota\n"))
        camperInfo = camper[codigo]
        print(f"""
              codigo : {codigo}
              Nombre : {camper[codigo].get('Nombre')}
              Apellido: {camper[codigo].get('Apellido')}
              ID : {camper[codigo].get('ID')}
              Estado: {camper[codigo].get('Estado')}
               """)
        print("Este es el cmaper que va a editar? ")
        print("1.si")
        print("2.No")
        print("3.salir")
        opc = int(input())        
        if (opc==1):
            nota= int(input("ingres el resultado de la prueba de sandbox\n "))
            if nota>= 60:
                print("El camper supero la prueba")
                camper[codigo]['Estado']= 'Inscrito'
                camper[codigo]['Notaprueba']= nota
                with open ("module/storage/camperIns.json", "a") as E_archivos:
                    json.dump(camperInfo,E_archivos,indent=4 ) 
                    E_archivos.write('\n')
                camper.pop(codigo)
                bandera = False
            elif nota<60:
                print("El camper no ha superado la prueba de sandbox") 
                camper[codigo]['Estado']= 'No inscrito'
                with open ("module/storage/camperNI.json", "a") as NI_archivos:
                    json.dump(camperInfo, NI_archivos, indent=4)
                    NI_archivos.write('\n')
                camper.pop(codigo)
                bandera = False
        elif (opc==3):
            bandera = False
    with open ("module/storage/camper.json", "w") as archivo:
        json.dump(camper, archivo, indent= 4)
        
        
        # print("\t1. Registrar resultado prueba") 
        # print("\t2. listar resultados")
        # print("\t3. Actualizar resultados")
        # print("\t4. Eliminar resultados")
        # print("\t0. salir ")
        # try: 
        #   opc = int(input())
        # except ValueError:
        #     system("cls")
        #     continue
    
        # match(opc):
        #      case 1: guardarResultados()
        #      case 2: listarResultados()
        #      case 0: 
        #           system("cls")
        #           bandera = False
        #      case _: menuNoValid(opc)
                 