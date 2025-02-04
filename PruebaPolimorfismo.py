from tkinter import *
import random
from Punto import Punto
from Circulo import Circulo
from Triangulo import Triangulo
from Hexagono import Hexagono
from Ovalo import Ovalo
from Linea import Linea
from Luna import Luna
from Estrella import Estrella
from NaveEspacial import NaveEspacial
from EstrellaFugaz import EstrellaFugaz

ventana = Tk()
ventana.title("P r o y e c t o  f i n a l  P O O")
ventana.geometry("1000x1000")

lienzo = Canvas(ventana, width=1000, height=1000)
lienzo.pack()

figurasUno = [

    Circulo(500,500,1500,"#1F305E"),

    # Luna
    Luna(500, 500, 250, "#C9B9B9"),

    # Brillos
    Hexagono(745, 145, 15, "#808080"),
    Hexagono(396, 922, 20, "#808080"),
    Hexagono(242, 936, 15, "#808080"),
    Hexagono(704, 858, 20, "#808080"),
    Hexagono(486, 104, 15, "#808080"),

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

    # Figuras simples extra

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
]

figurasDos = [

    Circulo(500,500,1500,"#1F305E"),

    # Luna
    Luna(500, 500, 250, "#C9B9B9"),

    # Brillos
    Hexagono(83, 216, 20, "#808080"),
    Hexagono(421, 267, 15, "#808080"),
    Hexagono(969, 334, 20, "#808080"),
    Hexagono(278, 515, 15, "#808080"),
    Hexagono(634, 890, 20, "#808080"),

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

    # Figuras simples extra

    Circulo(598, 232, 5, "#FFFFFF"),
    Circulo(573, 480, 5, "#EEEEEE"),
    Circulo(801, 798, 5, "#DDDDDD"),
    Circulo(773, 151, 5, "#CCCCCC"),
    Circulo(292, 260, 5, "#BBBBBB"),

    Triangulo(906, 756, 3, 20, "#FFFF00", True),
    Triangulo(534, 78, 3, 15, "#FFD700", False),
    Triangulo(318, 593, 3, 15, "#FFA500", True),
    Triangulo(787, 574, 3, 20, "#FFEC8B", False),
    Triangulo(982, 297, 3, 15, "#EEE8AA", True),

    Hexagono(420, 806, 5, "#DAA520"),
    Hexagono(651, 966, 5, "#BDB76B"),
    Hexagono(126, 936, 5, "#F0E68C"),
    Hexagono(485, 798, 5, "#FAFAD2"),
    Hexagono(437, 91, 5, "#FFFACD")
]

nave = NaveEspacial(200, 200, 1)
figurasUno.append(nave)
figurasDos.append(nave)

estrellaFugazUno = EstrellaFugaz(0,1000,1.5)
figurasUno.append(estrellaFugazUno)
figurasDos.append(estrellaFugazUno)

estrellaFugazDos = EstrellaFugaz(0,500, 1)
figurasUno.append(estrellaFugazDos)
figurasDos.append(estrellaFugazDos)

estrellaFugazTres = EstrellaFugaz(600,1000, 1)
figurasUno.append(estrellaFugazTres)
figurasDos.append(estrellaFugazTres)


def movimientos():

    # Movimiento estrella fugaz uno

    dx = 3
    dy = 3

    coords = estrellaFugazUno.obtenerCoordenadas()
    x, y = coords[0], coords[1]

    estrellaFugazUno.setX(x + dx)
    estrellaFugazUno.setY(y - dy)

    if x + dx >= 1000:
        estrellaFugazUno.setX(0)
        estrellaFugazUno.setY(1000)

    # Movimiento estrella fugaz dos

    dx = 10
    dy = 10

    coords = estrellaFugazDos.obtenerCoordenadas()
    x, y = coords[0], coords[1]

    estrellaFugazDos.setX(x + dx)
    estrellaFugazDos.setY(y - dy)

    if x + dx >= 1000:
        estrellaFugazDos.setX(0)
        estrellaFugazDos.setY(500)

    # Movimiento estrella fugaz tres

    dx = 5
    dy = 5

    coords = estrellaFugazTres.obtenerCoordenadas()
    x, y = coords[0], coords[1]

    estrellaFugazTres.setX(x + dx)
    estrellaFugazTres.setY(y - dy)

    if x + dx >= 1000:
        estrellaFugazTres.setX(600)
        estrellaFugazTres.setY(1000)

    # Movimiento nave

    dx = random.choice([-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3, -2, -1, 1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    dy = random.choice([-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3, -2, -1, 1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

    coords = nave.obtenerCoordenadas()
    x, y = coords[0], coords[1]

    # Verificar colisión con los bordes y cambiar dirección si es necesario
    if x + dx <= 0 or x + dx >= 1000:
        dx *= -1
    if y + dy <= 0 or y + dy >= 1000:
        dy *= -1

    nave.setX(x + dx)
    nave.setY(y + dy)

    lienzo.delete("all")

    if dx % 2 == 0:
        for f in figurasUno:
            f.dibuja(lienzo)
    else:
        for f in figurasDos:
            f.dibuja(lienzo)

    ventana.after(100, movimientos)  # Volver a llamar movimientos en 100ms

movimientos()
ventana.mainloop()
