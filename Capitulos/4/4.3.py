import turtle

t = turtle.Turtle()
bob = turtle.Turtle()

bob.penup() # Levantas la pluma para no dibujar
bob.goto(150, 0)   # Mover a bob a otro lugar
bob.pendown() # Bajar la pluma de nuevo

def cuadrado(t): 
    for i in range(4):
        t.fd(100)
        t.lt(90)

cuadrado(t)
cuadrado(bob)

turtle.mainloop()
