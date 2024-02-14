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
    ruta_completa = os.path.join(os.getcwd(), 'module/storage/camper.json')
    with open(ruta_completa, "r") as f:
        campersNuevos = json.load(f)

    num_identificacion = int(input("ingrese el numero de id de el camper al que va a asignar la nota: "))

    participante = None

    for val in campersNuevos:
        if val.get('ID') == num_identificacion:
            participante = val
            

    if participante:
        
        practica = int(input("Ingrese la calificacion de la prueba práctica: "))
        teorica = int(input("Ingrese la calificacion de la prueba teórica: "))
        quices_trabajos = int(input("Ingrese la calificacion de quices y trabajos: "))

        
        nota_final = (practica * 0.6) + (teorica * 0.3) + (quices_trabajos * 0.1)
        
        if nota_final >= 60:
            print("!Has sido aprobado¡, tu nota es: {:.2f}".format(nota_final))
        else:
            print("Estás en riesgo :(, tu nota es: {:.2f}".format(nota_final))
        
        participante['NotaModulo'] = nota_final
        participante['Estado'] = 'En Riesgo' if nota_final < 60 else 'Aprobado'
        participante['Horario'] = None

        

        print(f"""
        Datos del participante:
        N_Identificacion: {participante.get('ID')}
        Nombre: {participante.get('Nombre')}
        Apellido: {participante.get('Apellido')}
        Estado: {participante.get('Estado')}
        Horario: {participante.get('Horario')}
        """)
        ruta_completa = os.path.join(os.getcwd(), 'module/storage/camper.json')
        with open(ruta_completa, "w") as f:
            data = json.dumps(campersNuevos, indent=4)
            f.write(data)



        
    

# 
    