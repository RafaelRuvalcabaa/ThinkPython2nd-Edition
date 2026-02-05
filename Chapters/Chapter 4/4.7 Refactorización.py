import turtle
import math 

bob = turtle.Turtle()

def polilinea(t, n, longitud, angulo):
    for i in range(n):
        t.fd(longitud)
        t.lt(angulo)

def poligono(t, n, longitud):
    angulo = 360.0 / n
    polilinea(t, n, longitud, angulo)

def arco(t, r, angulo):
    longitud_arco = 2 * math.pi * r * angulo / 360
    n = int(longitud_arco / 3) + 1
    longitud_paso = longitud_arco / n
    angulo_paso = float(angulo) / n
    polilinea(t, n, longitud_paso, angulo_paso)

def circulo(t, r):
    arco(t, r, 360)


circulo(bob, 100)

turtle.mainloop()
