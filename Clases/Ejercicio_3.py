class Naturaleza:
    #Constructor
    def __init__(self):
        self.ALIMENTARIA = 0.055
        self.SERVICIO = 0.20


class Producto:
    #Constructor
    def __init__(self, tasa_iva):
        self.tasa_iva = tasa_iva
    





producto = Producto(Naturaleza.ALIMENTARIA) # IVA 5,5% 
precio_neto = FactoryFactura.crear(producto).facturar() 
print(precio_neto) 
# 105.5 
 
producto = Producto(Naturaleza.SERVICIO) # IVA 20% 
precio_neto = FactoryFactura.crear(producto).facturar() 
print(precio_neto) 
# 120 