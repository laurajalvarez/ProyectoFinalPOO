from Punto import Punto

class Ovalo(Punto):

    def __init__(self, x=0, y=0, ancho=0, alto=0, color="black"):
        super().__init__(x, y, color)
        self.setAncho(ancho)
        self.setAlto(alto)

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

    def dibuja(self, lienzo):
        lienzo.create_oval(
            self.getX() - self.__ancho // 2,
            self.getY() - self.__alto // 2,
            self.getX() + self.__ancho // 2,
            self.getY() + self.__alto // 2,
            outline=self.color, fill=self.color
        )

    def __str__(self):
        return "Centro: " + super().__str__() + " ancho: " + str(self.__ancho) + "alto: " + str(self.__alto) + " radio: " + str(self.__radio) + " "