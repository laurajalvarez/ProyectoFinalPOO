from Hexagono import Hexagono
from Triangulo import Triangulo

class Estrella:
    def __init__(self, x, y, escala = 1 , color="#D3D3D3"):
        self.x = x
        self.y = y
        self.escala = escala
        self.color = color

    def dibuja(self, lienzo):

        radioEstrella = 10 * self.escala
        radioHexagono = radioEstrella // 2

        hexagono = Hexagono(self.x, self.y, radioHexagono, "#808080")
        hexagono.dibuja(lienzo)

        trianguloSuperior = Triangulo(self.x, self.y, radioEstrella, radioEstrella, self.color)
        trianguloInferior = Triangulo(self.x, self.y, radioEstrella, radioEstrella, self.color, True)

        trianguloSuperior.dibuja(lienzo)
        trianguloInferior.dibuja(lienzo)

