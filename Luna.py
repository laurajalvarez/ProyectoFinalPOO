from Circulo import Circulo

class Luna(Circulo):
    def __init__(self, x=0, y=0, radio=50, color="#C9B9B9", colorManchas = "#A18989"):
        super().__init__(x, y, radio, color)
        self.colorManchas = colorManchas

    def dibuja(self, lienzo):
        super().dibuja(lienzo)
        self.DibujaManchas(lienzo)

    def DibujaManchas(self, lienzo):

        manchas = [
            (0.3, -0.2, 0.1),
            (-0.3, 0.1, 0.08),
            (-0.4, -0.2, 0.06),
            (0.2, 0.3, 0.09),
            (-0.1, -0.2, 0.04),
            (0.3, -0.3, 0.07),
            (-0.2, 0.3, 0.08),
            (0, 0, 0.015),
            (0.35, 0.1, 0.06),
            (-0.3, -0.25, 0.04),
            (0.1, 0.1, 0.05),
            (0.12, -0.4, 0.02)
        ]

        for dx, dy, factor in manchas:
            manchaRadio = self.getRadio() * factor
            x1 = self.getX() + dx * (self.getRadio() - manchaRadio) - manchaRadio
            y1 = self.getY() + dy * (self.getRadio() - manchaRadio) - manchaRadio
            x2 = x1 + 2 * manchaRadio
            y2 = y1 + 2 * manchaRadio

            lienzo.create_oval(x1, y1, x2, y2, fill=self.colorManchas, outline=self.colorManchas)

    def __str__(self):
        return "Luna: " + super().__str__()