from Triangulo import Triangulo
from Linea import Linea

class EstrellaFugaz:
    def __init__(self, x, y, escala = 1 , color="#D3D3D3"):
        self.setX(x)
        self.setY(y)
        self.setEscala(escala)
        self.color = color

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setEscala(self, escala):
        if escala > 0:
            self.__escala = escala
        else:
            self.__escala = 0

    def getEscala(self):
        return self.__escala

    def obtenerCoordenadas(self):
        return (self.__x, self.__y)

    def dibuja(self, lienzo):

        radioEstrella = 10 * self.__escala
        radioEstrellaPequeña = 5 * self.__escala

        #Rastro de la estrella

        linea1 = Linea(self.__x,self.__y, self.__x - 60 * self.__escala, self.__y + 40 * self.__escala, self.color)
        linea2 = Linea(self.__x, self.__y, self.__x - 60 * self.__escala, self.__y + 60 * self.__escala, self.color)
        linea3 = Linea(self.__x, self.__y, self.__x - 40 * self.__escala, self.__y + 60 * self.__escala, self.color)

        linea1.dibuja(lienzo)
        linea2.dibuja(lienzo)
        linea3.dibuja(lienzo)

        # Estrella grande

        trianguloSuperior = Triangulo(self.__x, self.__y, radioEstrella, radioEstrella, self.color)
        trianguloInferior = Triangulo(self.__x, self.__y, radioEstrella, radioEstrella, self.color, True)

        trianguloSuperior.dibuja(lienzo)
        trianguloInferior.dibuja(lienzo)

        #Estrellas pequeñas

        trianguloSuperiorEstrellaUno = Triangulo(self.__x - 20 * self.__escala , self.__y, radioEstrellaPequeña, radioEstrellaPequeña, self.color)
        trianguloInferiorEstrellaUno = Triangulo(self.__x - 20 * self.__escala , self.__y, radioEstrellaPequeña, radioEstrellaPequeña, self.color, True)

        trianguloSuperiorEstrellaDos = Triangulo(self.__x, self.__y + 20 * self.__escala, radioEstrellaPequeña, radioEstrellaPequeña, self.color)
        trianguloInferiorEstrellaDos = Triangulo(self.__x, self.__y + 20 * self.__escala, radioEstrellaPequeña, radioEstrellaPequeña, self.color, True)

        trianguloSuperiorEstrellaUno.dibuja(lienzo)
        trianguloInferiorEstrellaUno.dibuja(lienzo)

        trianguloSuperiorEstrellaDos.dibuja(lienzo)
        trianguloInferiorEstrellaDos.dibuja(lienzo)

