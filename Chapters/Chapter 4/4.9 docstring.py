
def polilinea(t,n,longitud, angulo):
    """
    Docstring for polilinea
    Dibujav n segmenetos de linea con la longitud dada y el angulo (en grados) entre ellos.
    """
    for i in range(n):
        t.fd(longitud)
        t.lt(angulo)

