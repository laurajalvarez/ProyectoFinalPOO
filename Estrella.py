from Hexagono import Hexagono
from Triangulo import Triangulo

class Estrella:
    def __init__(self, x, y, escala = 1 , color="#D3D3D3", colorSombra="#808080"):
        self.setX(x)
        self.setY(y)
        self.setEscala(escala)
        self.color = color
        self.colorSombra = colorSombra

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

    def dibuja(self, lienzo):

        radioEstrella = 10 * self.__escala
        radioHexagono = radioEstrella // 2

        hexagono = Hexagono(self.__x, self.__y, radioHexagono, self.colorSombra)
        hexagono.dibuja(lienzo)

        trianguloSuperior = Triangulo(self.__x, self.__y, radioEstrella, radioEstrella, self.color)
        trianguloInferior = Triangulo(self.__x, self.__y, radioEstrella, radioEstrella, self.color, True)

        trianguloSuperior.dibuja(lienzo)
        trianguloInferior.dibuja(lienzo)