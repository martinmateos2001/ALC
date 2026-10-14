from math import isclose

import numpy as np

# ------ Ejercicio 15 ------
def matriz_transicion(n, p):
    # construccion de la matriz de transición.
    P = np.zeros((n+1,n+1))
    P[0,0] = 1
    P[n,n] = 1
    for i in range(1, n):
        P[i+1, i] = p
        P[i-1, i] = 1-p
    return P
'''
Devuelve la matriz de transicion.
n es la distancia del bar a la casa.
p es la probabilidad de dar un paso hacia la casa
1-p es la probabilidad de dar un paso hacia el bar
'''

def estado_limite(n, p, v0):
    P = matriz_transicion(n,p)
    v = v0.copy()   
    for i in range(0,100000):
        v_ant = v.copy()
        v = P @ v
        if(np.allclose(v,v_ant, atol=1e-8)):
            break
    return v
'''
Devuelve el estado limite dado el estado inicial v0.
n pasos, p probalidad, vector canonico que indica donde está
el sujeto dentro del trayecto.
'''

# punto b
n=20
p=0.8
v=np.eye(n+1)[1]
print(estado_limite(n,p,v))