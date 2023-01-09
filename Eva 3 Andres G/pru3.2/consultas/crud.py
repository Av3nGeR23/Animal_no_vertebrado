#from conex import conn
from conex.conn import conex
import traceback

def listar_estrella():
    try:

        conexion = conex()
        cur = conexion.cursor()
        cur.execute("select Color, Tamano from Estrella")
        result = cur.fetchall()
        conexion.close()
    except:

        return None
    return result

def listar_Cienpies():
    try:

        conexion = conex()

        cur = conexion.cursor()
        cur.execute("select Patas, Veneno from cienpies")
        result = cur.fetchall()
        
        conexion.close()
    except:

        return None
    return result


def Insertar_estrella(Color, Tamano):
    sql = "insert into Estrella (Color, Tamano) values (%s,%s)"
    try:
        conexion = conex()
        cursor = conexion.cursor()
        cursor.execute(sql,(Color, Tamano))
        conexion.commit()
        filas = cursor.rowcount
        if filas > 0:
            print("""
            Datos ingresados OK
            """)
        else:
            print("no hubo cambios")
    except:
        print(traceback.print_exc())

def Insertar_Cienpies(Patas, Veneno):
    sql = "insert into cienpies (Patas, Veneno) values (%s,%s)"
    try:
        conexion = conex()
        cursor = conexion.cursor()
        cursor.execute(sql,(Patas, Veneno))
        conexion.commit()
        filas = cursor.rowcount
        if filas > 0:
            print("""
            Datos ingresados OK
            """)
        else:
            print("no hubo cambios")
    except:
        print(traceback.print_exc())

def buscar_estrella(Color):
    sql = "select Color, Tamano from Estrella where Color = %s"
    try:
        conexion = conex()
        cursor = conexion.cursor()
        cursor.execute(sql, (Color,))
        resultado = cursor.fetchone()
        return resultado

    except:
        print(traceback.print_exc())

def buscar_cienpies(Patas):
    sql = "select Patas, Veneno from cienpies where Patas = %s"
    try:
        conexion = conex()
        cursor = conexion.cursor()
        cursor.execute(sql, (Patas,))
        resultado = cursor.fetchone()
        return resultado

    except:
        print(traceback.print_exc())



def Eliminar_cienpies(Patas):
    sql = "select Patas, Veneno from cienpies where Patas = %s"
    conexion = conex()
    cursor = conexion.cursor()
    cursor.execute(sql,(Patas,))
    record = cursor.fetchone()
    print(record)
    sql_Delete_query = "Delete from cienpies where Patas = %s"
    cursor.execute(sql_Delete_query,(Patas,))
    conexion.commit()
    print('Cienpies Eliminado de DB', cursor.rowcount) #rowcount retorna el numero de filas afectadas

def Eliminar_estrella(Color):
    sql = "select Color from estrella where Color = %s"
    conexion = conex()
    cursor = conexion.cursor()
    cursor.execute(sql,(Color,))
    record = cursor.fetchone()
    print(record)
    sql_Delete_query = "Delete from estrella where Color = %s"
    cursor.execute(sql_Delete_query,(Color,))
    conexion.commit()
    print('Estrella Eliminada de DB', cursor.rowcount)




