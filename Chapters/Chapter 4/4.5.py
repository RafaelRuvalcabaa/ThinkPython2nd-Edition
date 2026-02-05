import turtle

bob = turtle.Turtle()


def cuadrado(t, longitud):
    for i in range(13):
        t.fd(longitud)
        t.lt(90)


cuadrado(bob, 100)


turtle.mainloop()