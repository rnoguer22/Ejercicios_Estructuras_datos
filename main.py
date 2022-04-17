from Clases.Ejercicio_1 import *
from Clases.Ejercicio_2 import *
from Clases.Ejercicio_3 import *


print ("Ejercicio 1:\n")

mostrar_ok = Mostrar('"OK"') 
mostrar_ko = Mostrar('"KO"') 
alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko) 
bloque_alternativa = Bloque() 
bloque_alternativa.agregarInstruction(alternativa) 
bucle = MientrasQue(True, bloque_alternativa) 


print ("Ejercicio 2:\n")

linea_1 = "Yo vivia con mi tio Sam"
linea_2 = "Y un dia me mando a comprar el pan"

#Declaramos la variable cosa_guapa como instancia de la clase MVC
cosa_guapa = MVC(linea_1, linea_2)
#Escribimos las dos lineas de texto separadas por un salto de linea
cosa_guapa.escribir()


print ("Ejercicio 3:")

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