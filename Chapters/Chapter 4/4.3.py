import turtle 

bob = turtle.Turtle()

def cuadrado(t):
    for i in range(4):
        
        t.fd(100)
        t.lt(90)
    
# Para hacer que el "turtle vaya para el otro lado"


bob.setheading(180)
cuadrado(bob)

turtle.mainloop()