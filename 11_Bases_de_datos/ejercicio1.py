"""En este ejercicio tendréis que crear una tabla llamada Alumnos que 
constará de tres columnas: la columna id de tipo entero, la columna nombre 
que será de tipo texto y la columna apellido que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis 
que insertar 8 alumnos a la tabla.
Por último, tienes que realizar una búsqueda de un alumno por nombre y 
mostrar los datos por consola."""

import sqlite3
def createDb():
    file = 'alumnos.db'
    con = sqlite3.connect(file)
    cursor = con.cursor()
    query_create = "CREATE TABLE IF NOT EXISTS ALUMNOS(ID INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE TEXT NOT NULL,APELLIDO TEXT NOT NULL);"
    cursor.execute(query_create)
    con.commit()
    cursor.close()
    con.close()

def crear_alumnos():
    file = 'alumnos.db'
    con = sqlite3.connect(file)
    cursor = con.cursor()
    alumnos = [('pedro','huston'),('esteban','quito'),('pedrito','dominguez'),
                ('matias','kann'),('dostin','hurtadillo'),('marta','garcia'),
                ('maria','angeles'),('victoria','honesta')]
    for ID,alumno in enumerate(alumnos):
        #print(f'{ID}-{alumno[0]}-{alumno[1]}')
        query = f"INSERT INTO ALUMNOS (NOMBRE,APELLIDO) VALUES('{alumno[0]}','{alumno[1]}')"
        cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def buscar_alumno_nombre():
    file = 'alumnos.db'
    con = sqlite3.connect(file)
    cursor = con.cursor()
    alumno = input('Ingrese el nombre del alumno: ')
    query = f"SELECT ID,NOMBRE,APELLIDO FROM ALUMNOS WHERE NOMBRE='{alumno}'"
    resultados = cursor.execute(query).fetchall()

    if resultados:
        for resultado in resultados:
            print(resultado)
    else:
        print('No existe el alumno con nombre ',alumno)
    cursor.close()
    con.close()

if __name__=='__main__':
    #Ya se creo la tabla con la funcion
    #createDb()
    #Ya se crearon los alumnos con la funcion
    #crear_alumnos()
    buscar_alumno_nombre()
