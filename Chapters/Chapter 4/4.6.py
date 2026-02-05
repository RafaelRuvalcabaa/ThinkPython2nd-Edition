import turtle

bob = turtle.Turtle()


def poligono(t, n, longitud):
    angulo = 360 / n
    for i in range(n):
        t.speed(1)
        t.fd(longitud)
        t.lt(angulo)


poligono(bob, 7, 70)