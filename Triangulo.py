from Punto import Punto

class Triangulo(Punto):

    def __init__(self, x, y, ancho=10, alto=10, color="black", invertir=False):
        super().__init__(x, y, color)
        self.setAncho(ancho)
        self.setAlto(alto)
        self.setInvertir(invertir)

    def setAncho(self, ancho):
        if ancho > 0:
            self.__ancho = ancho
        else:
            self.__ancho = 0

    def getAncho(self):
        return self.__ancho

    def setAlto(self, alto):
        if alto > 0:
            self.__alto = alto
        else:
            self.__alto = 0

    def getAlto(self):
        return self.__alto

    def setInvertir(self, invertir):
        self.__invertir = invertir

    def getInvertir(self):
        return self.__invertir

    def dibuja(self, lienzo):
        if self.__invertir:
            # Triángulo invertido
            lienzo.create_polygon(
                self.getX(), self.getY() + self.__alto // 2,  # Vértice inferior (pico inferior)
                self.getX() - self.__ancho // 2, self.getY() - self.__alto // 4,  # Vértice superior izquierdo
                self.getX() + self.__ancho // 2, self.getY() - self.__alto // 4,  # Vértice superior derecho
                outline=self.color, fill=self.color
            )
        else:
            # Triángulo normal
            lienzo.create_polygon(
                self.getX(), self.getY() - self.__alto // 2,  # Vértice superior (pico superior)
                self.getX() - self.__ancho // 2, self.getY() + self.__alto // 4,  # Vértice inferior izquierdo
                self.getX() + self.__ancho // 2, self.getY() + self.__alto // 4,  # Vértice inferior derecho
                outline=self.color, fill=self.color
            )

    def __str__(self):
        return "Centro: " + super().__str__() + " ancho: " + str(self.__ancho) + " alto: " + str(self.__alto) + " invertir: " + str(self.__invertir)