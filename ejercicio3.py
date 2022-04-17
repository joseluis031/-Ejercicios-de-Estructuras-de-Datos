class Naturaleza:
    def __init__(self):
        self.ALIMENTARIA = 5.5
        self.SERVICIO = 20

class Producto(Naturaleza):
    def __init__(self,iva):
        self.iva = iva
        self.producto = 100