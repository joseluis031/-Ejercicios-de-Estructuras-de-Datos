class Entrada:
    def __init__(self,linea1,linea2):
        self.linea1 = linea1
        self.linea2 = linea2
class Mayuscula():
    def __init__(self,datos):
        self.datos = Entrada
        self.datos.linea1 = datos.linea1
        self.datos.linea2 = datos.linea2
    
    
        
        f = open("archivo.txt","w")
        f.write(datos.linea1.upper() + "\n" + datos.linea2.upper())
        f.close
    
    
    
    

