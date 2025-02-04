from Circulo import Circulo
from Ovalo import Ovalo
from Triangulo import Triangulo

class NaveEspacial:
    def __init__(self, x, y, escala = 2, colorBase="#E5E5E5", colorDomo="#87CEEB", colorLuces="#FFD700", colorSombra="#788199"):
        self.setX(x)
        self.setY(y)
        self.setEscala(escala)
        self.colorBase = colorBase
        self.colorDomo = colorDomo
        self.colorLuces = colorLuces
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

    def obtenerCoordenadas(self):
        return (self.__x, self.__y)

    def dibuja(self, lienzo):
        ancho = 120 * self.__escala
        alto = 40 * self.__escala
        radioDomo = 65 * self.__escala
        radioLuz = 10 * self.__escala
        altoAntena = 20 * self.__escala
        anchoAntena = 9 * self.__escala
        altoPuntaFuego = 30 * self.__escala
        anchoPuntaFuego = 20 * self.__escala
        radioBaseFuego = 20 * self.__escala

        # Sombra
        sombraDomo = Circulo(self.__x, self.__y - 3 * self.__escala, radioDomo + 10 * self.__escala , "#FFFFFF" )
        sombraDomo.dibuja(lienzo)
        sombraBase = Ovalo(self.__x, self.__y + 20 * self.__escala, ancho + 15 * self.__escala, alto + 15 * self.__escala , "#FFFFFF")
        sombraBase.dibuja(lienzo)

        # Domo
        delineadoDomo = Circulo(self.__x, self.__y - 3 * self.__escala, radioDomo + 3, "#777777")
        delineadoDomo.dibuja(lienzo)
        domo = Circulo(self.__x, self.__y - 3 * self.__escala, radioDomo, self.colorDomo)
        domo.dibuja(lienzo)

        # Cuerpo base
        delineadoBase = Ovalo(self.__x, self.__y + 20 * self.__escala, ancho + 5, alto + 5, "#777777")
        delineadoBase.dibuja(lienzo)
        base = Ovalo(self.__x, self.__y + 20 * self.__escala, ancho, alto, self.colorBase)
        base.dibuja(lienzo)

        # Sombra inferior
        sombra = Ovalo(self.__x, self.__y + 30 * self.__escala, ancho - 20 * self.__escala, alto - 10 * self.__escala, self.colorSombra)
        sombra.dibuja(lienzo)

        # Antena
        antena = Triangulo(self.__x, self.__y - 40 * self.__escala, anchoAntena, altoAntena, "#EEEEEE")
        antena.dibuja(lienzo)
        luzAntena = Circulo(self.__x, self.__y - 50 * self.__escala, 5 * self.__escala, self.colorLuces)
        luzAntena.dibuja(lienzo)

        #Fuego centro
        puntaFuegoCentro = Triangulo(self.__x, self.__y + 60 * self.__escala, anchoPuntaFuego, altoPuntaFuego, "#FF5537", True)
        baseFuegoCentro = Circulo(self.__x,self.__y + 50 * self.__escala, radioBaseFuego, "#FF5537")

        baseFuegoCentro.dibuja(lienzo)
        puntaFuegoCentro.dibuja(lienzo)

        sombraPuntaFuegoCentro = Triangulo(self.__x, self.__y + 55 * self.__escala, anchoPuntaFuego - 10 * self.__escala, altoPuntaFuego - 10 * self.__escala, "#F7D547",True)
        sombraBaseFuegoCentro = Circulo(self.__x, self.__y + 50 * self.__escala, radioBaseFuego - 10 * self.__escala, "#F7D547")

        sombraPuntaFuegoCentro.dibuja(lienzo)
        sombraBaseFuegoCentro.dibuja(lienzo)

        #Fuego izquierdo
        puntaFuegoIzquierdo = Triangulo(self.__x - 15 * self.__escala, self.__y + 60 * self.__escala, anchoPuntaFuego, altoPuntaFuego, "#FF5537",True)
        baseFuegoIzquierdo = Circulo(self.__x - 15 * self.__escala, self.__y + 50 * self.__escala, radioBaseFuego, "#FF5537")

        baseFuegoIzquierdo.dibuja(lienzo)
        puntaFuegoIzquierdo.dibuja(lienzo)

        sombraPuntaFuegoIzquierdo = Triangulo(self.__x - 15 * self.__escala , self.__y + 55 * self.__escala, anchoPuntaFuego - 10 * self.__escala, altoPuntaFuego - 10 * self.__escala, "#F7D547", True)
        sombraBaseFuegoIzquierdo = Circulo(self.__x - 15 * self.__escala, self.__y + 50 * self.__escala, radioBaseFuego - 10 * self.__escala, "#F7D547")

        sombraPuntaFuegoIzquierdo.dibuja(lienzo)
        sombraBaseFuegoIzquierdo.dibuja(lienzo)

        #Fuego derecho
        puntaFuegoDerecho = Triangulo(self.__x + 15 * self.__escala, self.__y + 60 * self.__escala, anchoPuntaFuego, altoPuntaFuego, "#FF5537", True)
        baseFuegoDerecho = Circulo(self.__x + 15 * self.__escala, self.__y + 50 * self.__escala, radioBaseFuego, "#FF5537")

        baseFuegoDerecho.dibuja(lienzo)
        puntaFuegoDerecho.dibuja(lienzo)

        sombraPuntaFuegoDerecho = Triangulo(self.__x + 15 * self.__escala, self.__y + 55 * self.__escala, anchoPuntaFuego - 10 * self.__escala, altoPuntaFuego - 10 * self.__escala,"#F7D547", True)
        sombraBaseFuegoDerecho = Circulo(self.__x + 15 * self.__escala, self.__y + 50 * self.__escala, radioBaseFuego - 10 * self.__escala, "#F7D547")

        sombraPuntaFuegoDerecho.dibuja(lienzo)
        sombraBaseFuegoDerecho.dibuja(lienzo)

        # Luces en la base
        posiciones_luces = [-40, -20, 0, 20, 40]
        for dx in posiciones_luces:
            luz = Circulo(self.__x + dx * self.__escala, self.__y + 15 * self.__escala, radioLuz, self.colorLuces)
            luz.dibuja(lienzo)
