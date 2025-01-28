from Punto import Punto

class Hexagono(Punto):
    def __init__(self, x=0, y=0, radio=50, color="black"):
        super().__init__(x, y, color)
        self.setRadio(radio)

    def setRadio(self, radio):
        if radio > 0:
            self.__radio = radio
        else:
            self.__radio = 0

    def getRadio(self):
        return self.__radio

    def dibuja(self, lienzo):

        # Desplazamientos
        dx = int(self.getRadio() * 0.866)
        dy = int(self.getRadio() // 2)

        lienzo.create_polygon(
            self.getX(), self.getY() - self.getRadio(),  # Vértice superior
            self.getX() + dx, self.getY() - dy,  # Superior derecho
            self.getX() + dx, self.getY() + dy,  # Inferior derecho
            self.getX(), self.getY() + self.getRadio(),  # Vértice inferior
            self.getX() - dx, self.getY() + dy,  # Inferior izquierdo
            self.getX() - dx, self.getY() - dy,  # Superior izquierdo
            outline=self.color, fill=self.color
        )

    def __str__(self):
        return "Centro: " + super().__str__() + " Radio: " + str(self.__radio) + " "