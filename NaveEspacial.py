from Circulo import Circulo
from Ovalo import Ovalo
from Triangulo import Triangulo

class NaveEspacial:
    def __init__(self, x, y, escala = 1, colorBase="#E5E5E5", colorDomo="#87CEEB", colorLuces="#FFD700", colorSombra="#D2691E"):
        self.x = x
        self.y = y
        self.escala = escala
        self.colorBase = colorBase
        self.colorDomo = colorDomo
        self.colorLuces = colorLuces
        self.colorSombra = colorSombra

    def dibuja(self, lienzo):
        ancho = 120 * self.escala
        alto = 40 * self.escala
        radioDomo = 65 * self.escala
        radioLuz = 10 * self.escala
        altoAntena = 20 * self.escala
        anchoAntena = 9 * self.escala

        # Sombra
        sombraDomo = Circulo(self.x, self.y - 3 * self.escala, radioDomo + 10 , "#FFFFFF" )
        sombraDomo.dibuja(lienzo)
        sombraBase = Ovalo(self.x, self.y + 20 * self.escala, ancho + 15 , alto + 15 , "#FFFFFF")
        sombraBase.dibuja(lienzo)

        # Domo
        delineadoDomo = Circulo(self.x, self.y - 3 * self.escala, radioDomo + 3, "#4D82BC")
        delineadoDomo.dibuja(lienzo)
        domo = Circulo(self.x, self.y - 3 * self.escala, radioDomo, self.colorDomo)
        domo.dibuja(lienzo)

        # Cuerpo base
        delineadoBase = Ovalo(self.x, self.y + 20 * self.escala, ancho + 5, alto + 5, "#777777")
        delineadoBase.dibuja(lienzo)
        base = Ovalo(self.x, self.y + 20 * self.escala, ancho, alto, self.colorBase)
        base.dibuja(lienzo)

        # Sombra inferior
        sombra = Ovalo(self.x, self.y + 30 * self.escala, ancho - 20, alto - 10, self.colorSombra)
        sombra.dibuja(lienzo)

        # Antena
        antena = Triangulo(self.x, self.y - 40 * self.escala, anchoAntena, altoAntena, "#EEEEEE")
        antena.dibuja(lienzo)
        luzAntena = Circulo(self.x, self.y - 50 * self.escala, 5 * self.escala, self.colorLuces)
        luzAntena.dibuja(lienzo)

        # Luces en la base
        posiciones_luces = [-40, -20, 0, 20, 40]
        for dx in posiciones_luces:
            luz = Circulo(self.x + dx * self.escala, self.y + 15 * self.escala, radioLuz, self.colorLuces)
            luz.dibuja(lienzo)

    def __str__(self):
        return