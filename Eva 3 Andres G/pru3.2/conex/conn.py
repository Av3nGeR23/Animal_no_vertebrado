#import mysql.connector as conn
import mysql.connector

def conex():
    try:
        myconn = mysql.connector.connect(host="localhost", user="AndresG", passwd="Andres23$%", database="Andres_base")

    except:
        # registrar un log...
        print("Error")
    return myconn


