def cuenta_regresiva(numero):
    """
    Docstring for cuenta_regresiva
    
    :param numero: This number is where you want to begin the countdown

    """

    if numero <= 0:
        print("Let go....")
    else: 
        cuenta_regresiva(numero-1)
        print(numero)


cuenta_regresiva(3)


def repetir(texto, numero):
    if numero < 0:
        return 
    print(texto)
    repetir(texto,numero-1)


repetir("Hola", 3)


