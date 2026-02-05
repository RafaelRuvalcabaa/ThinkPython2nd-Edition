import turtle

bob = turtle.Turtle()

bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)

bob.penup()
bob.fd(100)
bob.pendown()

# bob.goto(100,0) para ir a una posicion exacta

for i in range(4):
    bob.fd(100)
    bob.lt(90)
    

turtle.mainloop()