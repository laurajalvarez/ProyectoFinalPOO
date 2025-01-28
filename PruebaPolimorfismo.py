from tkinter import *
from Punto import Punto
from Circulo import Circulo
from Triangulo import Triangulo
from Hexagono import Hexagono
from Luna import Luna
from Estrella import Estrella
from Ovalo import Ovalo
from NaveEspacial import NaveEspacial

ventana = Tk()
ventana.title("P r o y e c t o  f i n a l")
ventana.geometry("1000x1000")

lienzo = Canvas(ventana, width=1000, height=1000, bg="#1F305E")
lienzo.pack()

figuras = [
    # Luna
    Luna(500, 500, 200, "#C9B9B9"),

    # Estrellas
    Estrella(745, 145, 1, "#D3D3D3"),
    Estrella(396, 922, 1.5, "#F5F5DC"),
    Estrella(242, 936, 1, "#D3D3D3"),
    Estrella(704, 858, 1, "#F5F5DC"),
    Estrella(486, 104, 1.5, "#D3D3D3"),
    Estrella(83, 216, 1, "#F5F5DC"),
    Estrella(421, 267, 1, "#D3D3D3"),
    Estrella(969, 334, 1, "#F5F5DC"),
    Estrella(278, 515, 1, "#D3D3D3"),
    Estrella(634, 890, 1, "#F5F5DC"),


    Circulo(598,  232, 5, "#FFFFFF"),
    Circulo(573, 480, 5, "#EEEEEE"),
    Circulo(801, 798, 5, "#DDDDDD"),
    Circulo(773, 151, 5, "#CCCCCC"),
    Circulo(292, 260, 5, "#BBBBBB"),

    Triangulo(906, 756, 3,20, "#FFFF00", True),
    Triangulo(534, 78, 3,15, "#FFD700", False),
    Triangulo( 318, 593, 3,15, "#FFA500", True),
    Triangulo(787, 574, 3,20, "#FFEC8B", False),
    Triangulo(982, 297, 3,15, "#EEE8AA", True),

    Hexagono(420,806, 5, "#DAA520"),
    Hexagono(651,966, 5, "#BDB76B"),
    Hexagono(126,936, 5, "#F0E68C"),
    Hexagono(485,798, 5, "#FAFAD2"),
    Hexagono(437,91, 5, "#FFFACD"),

    NaveEspacial(200, 200, 1)
]

for f in figuras:
    f.dibuja(lienzo)

ventana.mainloop()