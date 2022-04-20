class Entrada:
    def __init__(self,linea1,linea2):
        self.linea1 = linea1
        self.linea2 = linea2
class Mayuscula():
    def __init__(self,datos):
        self.datos = Entrada
        self.datos.linea1 = datos.linea1.upper()
        self.datos.linea2 = datos.linea2.upper()

class Lectura():
    def __init__(self,archivo):
        self.archivo = archivo
    def Archivo(self):
        self.archivo = "archivo.txt"
        f = open(self.archivo,"w")
        f.write(self.datos.linea1)
    
    
    
    
linea1 = input("Introduzca la primera linea del archivo:")
linea2 = input("Introduce la segunda linea del archivo:")
datos = Entrada(linea1,linea2)