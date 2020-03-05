from funciones_xml import *
from lxml import etree







while True:

    print("1- Lista el titulo de todos los libros.")
    print("2- Cuenta la cantidad de premios que ha recibido en su carrera.")
    print("3- Introduce por teclado el nombre de un personaje. Muestra los libros que tengan ese personaje.")
    print("4- Di por teclado un año y muestra los titulos de los libros y el titulo de los premios que ha ganado ese año.")
    print("5- Muestra por pantalla el o los personajes que aparecen en más libros y los libros en los cuales aparecen.")
    print("6- Salir del programa")

    eleccion=int(input("Selecciona la opción que quieras:"))

    if eleccion==1:
        for i in listar_libros(libros):
            print("Titulo:",i)
        
        
    elif eleccion==2:

        print(contar_premios(libros))
        
        

    elif eleccion==3:
        nombre=str(input("Introduce el nombre de un personaje:"))

        for i in filtrar_nombre(libros, nombre):
            print("Titulo:",i)
        
     

    elif eleccion==4:
        armadura=str(input("Introduce una armadura:"))
        habilidad=str(input("Introduce una habilidad:"))
        print(filtrar_por_armadura_habilidad(personajes, armadura, habilidad))
        
    elif eleccion==5:
        arma=str(input("Introduce un arma:"))
        nivel=int(input("Introduce un nivel:"))
        print(filtrar_por_arma_nivel(personajes, arma, nivel))

    elif eleccion==6:
        print("Finalizando programa")
        break
