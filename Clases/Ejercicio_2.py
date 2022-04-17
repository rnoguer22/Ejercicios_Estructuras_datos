from multiprocessing.sharedctypes import Value
import string


class MVC:
    #Constructor
    def __init__(self, linea1, linea2):
        self.linea1 = linea1
        self.linea2 = linea2
        #Convertimos las dos lineas de texto a mayusculas
        #Ademas, nos aseguramos que ambas lineas de texto sean cadenas de texto
        if isinstance(self.linea1 and self.linea2, string):
            self.linea1.upper()
            self.linea2.upper()
        else:
            raise ValueError("Las lineas deben de ser cadenas de texto")
