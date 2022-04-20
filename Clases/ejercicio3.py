class Naturaleza:
    def __init__(self):
        self.ALIMENTARIA = 5.5
        self.SERVICIO = 20

class Producto(Naturaleza):
    def __init__(self,iva):
        self.iva = iva
    def facturar(self):
        return 100 +self.iva

class Factory(Producto):
    def __init__(self):
        pass
    def crear(self):
        clase = Producto(self.iva)
        return clase
    

