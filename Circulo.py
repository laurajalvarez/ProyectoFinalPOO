from Punto import Punto

class Circulo(Punto):

    def __init__(self, x=0, y=0 , radio=0, color="black"):
        super().__init__(x, y, color)
        self.setRadio(radio)

    def setRadio (self, radio):
        if radio > 0:
            self.__radio = radio
        else:
            self.__radio = 0

    def  getRadio(self):
        return self.__radio

    def dibuja(self, lienzo):

        lienzo.create_oval(
            self.getX() - self.__radio // 2,
            self.getY() - self.__radio // 2,
            self.getX() + self.__radio // 2,
            self.getY() + self.__radio // 2,
            outline = self.color, fill = self.color
        )

    def __str__(self):
        return "Centro: " + super().__str__() + " Radio: " + str(self.__radio) + " "