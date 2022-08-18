class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def mostrar(self):
        print("Nombre: {} , Nota: {}".format(self.nombre,self.nota))
    def condicion(self):
        #se aprueba con 8 o mas
        estado = "aprobado" if self.nota >= 8 else "desaprobado"
        print("Su nota es: {} por lo que esta {}".format(self.nota,estado))

estudiante = Alumno("john snow",7)
estudiante.mostrar()
estudiante.condicion()
    