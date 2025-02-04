from Punto import Punto

class Linea:

    def __init__(self, x1=0, y1=0, x2=0, y2=0, color="black"):
        self.punto1 = Punto(x1, y1, color)
        self.punto2 = Punto(x2, y2, color)
        self.color = color

    def setPunto1(self, x, y):
        self.punto1.setX(x)
        self.punto1.setY(y)

    def setPunto2(self, x, y):
        self.punto2.setX(x)
        self.punto2.setY(y)

    def getPunto1(self):
        return self.punto1

    def getPunto2(self):
        return self.punto2

    def dibuja(self, lienzo):
        lienzo.create_line(
            self.punto1.getX(), self.punto1.getY(),
            self.punto2.getX(), self.punto2.getY(),
            fill=self.color
        )

    def __str__(self):
        return "Punto1: " + str(self.punto1) + " Punto2: " + str(self.punto2) + " "