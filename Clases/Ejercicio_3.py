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


#Declaramos Naturaleza como instancia de la clase Naturaleza, para poder aplicar el iva correspondiente
Naturaleza = Naturaleza()

producto = Producto(Naturaleza.ALIMENTARIA) # IVA 5,5% 
precio_neto = FactoryFactura.crear(producto).facturar()
print(precio_neto) 
# 105.5 

producto = Producto(Naturaleza.SERVICIO) # IVA 20% 
precio_neto = FactoryFactura.crear(producto).facturar() 
print(precio_neto) 
# 120 