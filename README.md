# Ejercicios_Estructuras_datos

[Pinche aqui para acceder al link del repositorio](https://github.com/rnoguer22/Ejercicios_Estructuras_datos.git)

---

*Queda resuelta la tarea Ejercicios de Estructuras de datos. Para ello he utilizado la programacion orientada a objetos de python.
Aclaro que, ya que el uso de la filosofia MVC es bastante complejo, he simplificado el ejercicio adaptando dicha filosofia a la programacion orientada a objetos de python.*

---

## Indice
* [main](#1)
* [Ejercicio 1](#2)
* [Ejercicio 2](#3)
* [Ejercicio 3](#4)

---

## main<a name="1"></a>
```python3
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
```

---

## Ejercicio 1<a name="2"></a>
```python3
class Bloque: 
    # Un bloque es un conjunto de instrucciones ejecutadas 
    # unas detrás de otras. 
    def __init__(self): 
        # Por defecto, un bloque no contiene ninguna instrucción. 
        self.instrucciones = [] 
 
    def agregarInstruction(self, instruccion): 
        self.instrucciones.append(instruccion) 
 
class Si: 
    # Representa una instrucción 'if'. 'condicion' es una cadena 
    # de caracteres que contiene la evaluación de la condición, 
    # 'entonces' es el bloque de instrucciones ejecutadas si la condición 
    # se verifica, 'si_no' es el bloque de instrucciones ejecutadas 
    # si no se verifica. 
 
    def __init__(self, condicion, entonces, si_no): 
        self.condicion = condicion 
        self.entonces = entonces 
        self.si_no = si_no 
 
class MientrasQue: 
    # Representa una instrucción 'while'. 
    # 'condicion' es una cadena que contiene el valor evaluado 
    # para decidir si el bucle continúa o no, 
    # 'bloque' es la secuencia de instrucciones ejecutadas en bucle. 
    def __init__(self, condicion, bloque): 
        self.condicion = condicion 
        self.bloque = bloque 
 
class Mostrar: 
    # Una instrucción para mostrar un mensaje 
    # en salida estándar. 
    def __init__(self, mensaje): 
        self.mensaje = mensaje 
```

---

## Ejercicio 2<a name="3"></a>
```python3
import time

class MVC:
    #Constructor
    def __init__(self, linea1, linea2):
        self.__linea1 = linea1
        self.__linea2 = linea2
        #Convertimos las dos lineas de texto a mayusculas
        #Ademas, nos aseguramos que ambas lineas de texto sean cadenas de texto
        if isinstance(self.__linea1, str):
            self.__linea1.upper()
        elif isinstance(self.__linea2, str):
            self.__linea2.upper()
        else:
            raise TypeError("Las lineas deben de ser cadenas de texto")
        
    def escribir(self):
        file = open("Ejercicio2.txt", "w")
        file.write(self.__linea1)
        file.write("\n")
        file.write(self.__linea2)
        #Dentro de 10 segundos el archivo se cierra
        time.sleep(3)
        file.close()
```

---

## Ejercicio 3<a name="4"></a>
```python3
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
```
