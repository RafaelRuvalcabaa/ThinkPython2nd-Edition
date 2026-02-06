import turtle
import math 


bob = turtle.Turtle()


def poligono(t, n, longitud):
    angulo = 360 / n
    for i in range(n):
        t.speed(4)
        t.fd(longitud)
        t.lt(angulo)


#poligono(bob, 7, 70)


def circulo(t, r):
    perimetro = 2 * math.pi * r
    n = 50
    longitud = perimetro / n
    poligono(t, n, longitud)

circulo(bob, 50)



turtle.mainloop()