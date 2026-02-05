import turtle 

# Referenciamos a la pantalla de interfaz con el nombre bob 
bob = turtle.Turtle()

# Cuando imprimimos bob en consola sale el tipo de objeto como tipo turtle
print(bob)

# Mover a la tortuga hacia delante 
#bob.fd(100)
#bob.lt(90)
#bob.fd(100)
#bob.lt(90)
#bob.fd(100)
#bob.lt(90)
#bob.fd(100)
# Lo mantenemos en un loop para verlo porque como no tiene informacion se cerraria 



### ---------------------------------------------------

for i in range(4):
    print("Hola")


for i in range(4):
    bob.fd(100)
    bob.lt(90)






def cuadrado(t): 
    for i in range(4):
        t.fd(100)
        t.lt(90)
    

cuadrado(bob)
turtle.mainloop()