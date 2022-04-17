import string


class MVC:
    #Constructor
    def __init__(self, linea1, linea2):
        self.__linea1 = linea1
        self.__linea2 = linea2
        #Convertimos las dos lineas de texto a mayusculas
        #Ademas, nos aseguramos que ambas lineas de texto sean cadenas de texto
        if isinstance(self.linea1 and self.linea2, string):
            self.__linea1.upper()
            self.__linea2.upper()
        else:
            raise ValueError("Las lineas deben de ser cadenas de texto")
        
    def escribir(self):
        file = open("Ejercicio2.txt")
        file.write(self.__linea1)
        file.write(self.__linea2)