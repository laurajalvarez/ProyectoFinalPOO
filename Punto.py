from Figura import Figura

class Punto(Figura):
    def __init__(self, x=0, y=0, color="black"):
        self.setX(x)
        self.setY(y)
        self.color = color

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def dibuja(self, lienzo):
        lienzo.create_oval(self.__x,
                           self.__y,
                           self.__x + 3,
                           self.__y + 3,
                           outline = self.color, fill = self.color)

    def __str__(self):
        return "[" + str(self.__x) + "," + str(self.__y) + "]"