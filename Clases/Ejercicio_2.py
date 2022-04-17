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