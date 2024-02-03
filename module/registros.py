



def menu ():
    bandera = True 
    while (bandera):

       print("\t1.Registro de notas ")
       print("\t2.Registro de areas ")
       print("\t3.Registro de rutas ")
       print("\t4.Registro de modulos ")
       print("\t5.Registro de matricula")
       print("\t0.Salir")
       match(opc):
           case 1: notas()
           case 2: areas()
           case 3: rutas()
           case 4: modulos()
           case 5: matricula()
           case 0:
               system("clear")
               bandera = False
           case _: menuNoValid(opc)
