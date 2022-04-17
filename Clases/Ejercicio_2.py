import string
import time


class MVC:
    #Constructor
    def __init__(self, linea1, linea2):
        self.__linea1 = linea1
        self.__linea2 = linea2
        #Convertimos las dos lineas de texto a mayusculas
        #Ademas, nos aseguramos que ambas lineas de texto sean cadenas de texto
        if isinstance(self.__linea1 and self.__linea2, string):
            self.__linea1.upper()
            self.__linea2.upper()
        else:
            raise ValueError("Las lineas deben de ser cadenas de texto")
        
    def escribir(self):
        file = open("Ejercicio2.txt")
        file.write(self.__linea1)
        file.write(self.__linea2)
        #Dentro de 10 segundos el archivo se cierra
        time.sleep(10)
        file.close()


linea_1 = "Yo vivia con mi tio Sam"
linea_2 = "Y un dia me mando a comprar el pan"

#Declaramos la variable cosa_guapa como instancia de la clase MVC
cosa_guapa = MVC(linea_1, linea_2)
cosa_guapa.escribir()