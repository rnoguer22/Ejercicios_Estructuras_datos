class Naturaleza:
    #Constructor
    def __init__(self):
        self.ALIMENTARIA = 0.055
        self.SERVICIO = 0.20


class Producto(Naturaleza):
    #Constructor
    def __init__(self, tasa_iva):
        self.tasa_iva = tasa_iva
    
class FactoryFactura(Producto):
    #Constructor
    def __init__(self):
        pass

    def crear(self, factura):
        resultado = 100 + self.tasa_iva*100
    
    def facturar(self):
        print(self.crear(self.factura))




producto = Producto(Naturaleza.ALIMENTARIA) # IVA 5,5% 
precio_neto = FactoryFactura.crear(producto).facturar() 
print(precio_neto) 
# 105.5 
 
producto = Producto(Naturaleza.SERVICIO) # IVA 20% 
precio_neto = FactoryFactura.crear(producto).facturar() 
print(precio_neto) 
# 120 