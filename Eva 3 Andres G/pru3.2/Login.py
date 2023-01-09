import hashlib  # permite el uso de MD5 y otros tipos de codificacion
import traceback
import pwinput  # hace que la clave o el valor ingresado figure en pantalla solo con ****
from conex.conn import conex


class Menu_login():
    def __init__(self):
        print('Wellcome to my world')

    def signup():  # registro de usuario, guarda nombre y clave codificada en base de datos
        try:
            Nombre = input(' Ingrese Nombre:  ')
            pwd = pwinput.pwinput('Ingrese password: ')
            conf_pwd = pwinput.pwinput('Confirme password: ')
            if conf_pwd == pwd:
                hash1 = hashlib.md5(conf_pwd.encode()).hexdigest()
            else:
                print('Password no coincide \n')

            sql = "insert into usuarios (Username, Password) values (%s,%s)"

            conexion = conex()
            cursor = conexion.cursor()
            cursor.execute(sql, (Nombre, hash1))
            conexion.commit()
            filas = cursor.rowcount
            if filas > 0:
                print("""
                            ***********************
                            * Datos ingresados OK *
                            ***********************
                            """)
        except:
            print(traceback.print_exc())

    def login():  # Ingreso de datos y realiza comparacion con datos almacenados en base de datos,
        # si son correctos da acceso a programa, de lo contrario te indica que clave o pass erroneos
        try:
            Nombre = input('Ingrese Nombre: ')
            passw = pwinput.pwinput('Ingrese password: ')
            resultado = hashlib.md5(passw.encode()).hexdigest()
            sql = "select * from usuarios where  username = %s AND password = %s"
            conexion = conex()
            cursor = conexion.cursor()
            cursor.execute(sql, (Nombre, resultado))
            # El método devuelve un solo registro o Ninguno si no hay más filas disponibles
            valida = cursor.fetchone()

            # si valores ingresados son = a los almacenados en DB te redirige al MENU de animales
            if valida == (Nombre, resultado):
                print('Estas dentro del programa')
                print(f'Bienvenido {Nombre}')
                from menu import menu
                menu()

            else:
                print('Usuario o Password Invalida')
        except:
            # Imprime el rastreo de la excepción.
            print(traceback.print_exc())
            print('Usuario o Password Invalida')

    # Menu inicial para registro o login
    while 1:
        print("********** Login System **********")
        print("1.Registro")
        print("2.Login")
        print("3.Exit")
        ch = int(input("Ingrese opcion:  "))
        if ch == 1:
            signup()
        elif ch == 2:
            login()
        elif ch == 3:
            break
        else:
            print("Adios!")
