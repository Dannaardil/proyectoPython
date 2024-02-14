import json
import os
from os import system
from .data import pruebaModulo as prueba2
from .data import modulo
def pruebaFundamentos():
    print("""
PRUEBA FUNDAMENTOS
""")

    # Cargar campersNuevos desde el archivo JSON
    ruta_completa = os.path.join(os.getcwd(), 'module/storage/camperIns.json')
    with open(ruta_completa, "r") as f:
        camper= json.load(f)

    ID = int(input("ingrese el numero de id de el camper al que va a asignar la nota: "))

    participante = None

    for val in camper:
        if val.get('ID') == ID:
            participante = val

    for i,val in enumerate(camper):
        print(f"""
______________________________________
Codigo: {i}
Nombre: {val.get('Nombre')}
Apellido: {val.get('Apellido')}
______________________________________

""")
        ruta_completa = os.path.join(os.getcwd(), 'module/storage/camperIns.json')
        with open(ruta_completa, "w") as f:
            data = json.dumps(camper, indent=4)
            f.write(data)
        if participante:
        
            practica = int(input("Ingrese la calificacion de la prueba práctica: "))
            teorica = int(input("Ingrese la calificacion de la prueba teórica: "))
            quices_trabajos = int(input("Ingrese la calificacion de quices y trabajos: "))

        
            nota_final = (practica * 0.6) + (teorica * 0.3) + (quices_trabajos * 0.1)
        
            if nota_final >= 60:
             print("!Has sido aprobado¡, tu nota es: {:.2f}".format(nota_final))
            else:
             print("Estás en riesgo  tu nota es: {:.2f}".format(nota_final))
        
            camper['ModuloNotaModulo'] = nota_final
            camper['Estado'] = 'En Riesgo' if nota_final < 60 else 'Aprobado'
            camper['Horario'] = None

            

            print(f"""
            Datos del camper:
            N_Identificacion: {camper.get('ID')}
            Nombre: {camper.get('Nombre')}
            Apellido: {camper.get('Apellido')}
            Estado: {camper.get('Estado')}
            Horario: {camper.get('Horario')}
            """)
            ruta_completa = os.path.join(os.getcwd(), 'module/storage/camperIns.json')
            with open(ruta_completa, "w") as f:
                data = json.dumps(camper, indent=4)
                f.write(data)



        
    

# 
    