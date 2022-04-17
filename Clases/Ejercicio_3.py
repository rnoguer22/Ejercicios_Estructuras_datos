class Naturaleza:
    #Constructor
    def __init__(self):
        self.ALIMENTARIA = 0.055
        self.SERVICIO = 0.20


class Producto(Naturaleza):
    #Constructor
    def __init__(self, tasa_iva):
        self.tasa_iva = tasa_iva

    #Metodo que devuelve el precio del producto con el iva aplicado
    def facturar(self):
        return 100 + 100*self.tasa_iva


class FactoryFactura(Producto):
    #Constructor
    def __init__(self):
        pass

    #Metodo el cual devuelve la clase Producto con su iva correspondiente
    def crear(self):
        clase = Producto(self.tasa_iva)
        return clase