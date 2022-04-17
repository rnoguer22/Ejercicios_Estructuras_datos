class MVC:
    #Constructor
    def __init__(self, linea1, linea2):
        self.linea1 = linea1
        self.linea2 = linea2
        #Convertimos las dos lineas de texto a mayusculas
        self.linea1.upper()
        self.linea2.upper()
