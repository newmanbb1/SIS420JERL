condicion = True
def imprimirDatos():
    
    datosPersonales =["Jhon Erick","Ramirez Leaños","12993994","111-69"]
    return datosPersonales

while condicion:
      print("***MENU***")
      print("1: IMPRIMIR DATOS")
      print("2: SALIR")
      opc = input("ingrese una opcion\n")
      if opc == "1":
          print ("Mi nombre es jhon erick\ny este es mi programa con biografia corta\nEn la siguiente lista muestro mis datos personales :\n",imprimirDatos())
      elif opc =="2":
         condicion=False        
         print ("Gracias por usar Mi Programa")
