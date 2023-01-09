from consultas import crud
from Animal_No_Vertebrado import *


class MMenu():
    def __init__(self, patas, veneno, color, tamano, columna_vertebral):
        self.columna_vertebral = columna_vertebral
        self.color = color
        self.tamano = tamano
        self.patas = patas
        self.veneno = veneno 
        def __str__(self):
            return '''
        Este es un animal no Vertebrado   ...
        '''.format(self.columna_vertebral, self.patas, self.veneno, self.color, self.tamano)
        


    def menu(): # menu principal- ingresa un valor y lo almacena en opc
        print("""
            1. Agregar Animal NO Vertebrado
            2. Listar 
            3. Buscar
            4. Eliminar
            5. Salir
            
            """)
        opc = int(input("Ingrese una opción : "))
        return opc

    def listarView(lista):
        for x in lista:
            print(x)

    """
    Un submenú que le permite insertar una estrella o un ciempiés.
    """
    def insertar(): # submenu para ingresar estrella o cienpies 
        op= int(input('''Quiere agregar:
                     1- Estrella
                     2- Cienpies 
                      '''))
        if op == 1:
            def Insertar_estrella():#se ingresa y almacena 2 valores y se insertan en la DB
                Color = input("Ingrese Color : ")
                Tamano = input("Ingrese Tamano : ")
                crud.Insertar_estrella(Color, Tamano)
            Insertar_estrella()

        if op == 2:
            def Insertar_Cienpies():#se ingresa y almacena 2 valores y se insertan en la DB
                Patas = input("Ingrese Cantidad de Patas : ")
                Veneno = input(" Es venenoso? : ")
                crud.Insertar_Cienpies(Patas, Veneno)
            Insertar_Cienpies()
        

    def buscar():  #submenu para buscar estrella o cienpies, se ingresa 1 valor y se compara con DB, 
                   #si hay igualdad se muestra el valor en pantalla
        op= int(input('''Quiere Buscar :
                     1- Estrella
                     2- Cienpies 
                      '''))
        if op == 1:
            def buscar_estrella():
                Color = input("Ingrese color a buscar: ")
                user = crud.buscar_estrella(Color)
                #print(crud.buscar(Color))
                if user is not None:
                    print("Color //  Tamano    ")
                    print("{0}    {1:}  ".format(user[0], user[1]))
                else:
                    print("No hay datos que mostrar")
            buscar_estrella()

        if op == 2:
            def buscar_cienpies():
                Patas = input("Ingrese Cantidad patas a buscar: ")
                user = crud.buscar_cienpies(Patas)
                #print(crud.buscar(Color))
                if user is not None:
                    print("Patas //  Veneno    ")
                    print("{0}    {1:}  ".format(user[0], user[1]))
                else:
                    print("No hay datos que mostrar")
            buscar_cienpies()

    
    def Eliminar(): # submenu para eliminar estrella o cienpies, se ingresa un valor, se compara con DB, si hay igualdad se elimina
        
        op= int(input('''Quiere Eliminar  :
                     1- Estrella
                     2- Cienpies 
                      '''))
        if op == 1:
            def eliminar_estrella():
                Color = input("Ingrese color a Eliminar : ")
                user = crud.Eliminar_estrella(Color)
                #print(crud.buscar(Color))
                if user is not None:
                    print("Color //  Tamano    ")
                    print("{0}    {1:}  ".format(user[0], user[1]))
                else:
                    print("No hay datos que mostrar")
            eliminar_estrella()

        if op == 2:
            def eliminar_cienpies():
                Patas = input("Ingrese Cantidad patas a Eliminar: ")
                user = crud.Eliminar_cienpies(Patas)
                #print(crud.buscar(Color))
                if user is not None:
                    print("Patas //  Veneno    ")
                    print("{0}    {1:}  ".format(user[0], user[1]))
                else:
                    print("No hay datos que mostrar")
            eliminar_cienpies()


    while True:
        opc = menu()
        if opc == 1:
            insertar()
        elif opc == 2:
            op= int(input('''Quiere Listar :
                     1- Estrella
                     2- Cienpies 
                      '''))
            if op == 1:
                print("Listar Estrella")
                l = crud.listar_estrella()
                if l is not None:
                    listarView(l)
                else:
                    print("Error")
            elif op == 2:
                print("Listar Cienpies")
                l = crud.listar_Cienpies()
                if l is not None:
                    listarView(l)
                else:
                    print("Error")    
        elif opc == 3:
            buscar()
        elif opc == 4:
            Eliminar()
        elif opc == 5:
            break
        else:
            print('Vuelva Pronto')



