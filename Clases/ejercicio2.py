class Entrada:
    def __init__(self,linea1,linea2):
        self.linea1 = linea1
        self.linea2 = linea2
class Mayuscula():
    def __init__(self,datos):
        self.datos = Entrada
        self.datos.l1 = datos.linea1.upper()
        self.datos.l2 = datos.linea2.upper()

class Lectura():
    def __init__(self,archivo,datosMy):
        self.datosMy = datosMy
        self.archivo = archivo
    def Archivo(self):
        self.archivo = "archivo.txt"
        f = open(self.archivo,"w")
        f.write(self.datosMy)
    
    
    
    
linea1 = input("Introduzca la primera linea del archivo:")
linea2 = input("Introduce la segunda linea del archivo:")
datos = Entrada(linea1,linea2)
datosMy = Mayuscula(datos)
Lectura("archivo.txt",datosMy)