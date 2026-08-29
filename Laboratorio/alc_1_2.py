import numpy as np

''' Funciones utilizables de numpy
np.cos()
np.sen()
np.eye()
np.shape()
np.zeros()
np.copy()
np.ones()
np.ndim()
np.arrange()
np.linspace()
np.array()
np.reshape()
Funciones del submódulo np.random que sirvan para generar números pseudo-aleatorios.
Operaciones de slicing
'''

# --- Laboratorio 1 ---

def abs(x):
    if x>=0:
        return x
    else:
        return -x
    
def error(x,y):
    x = np.float64(x)
    y = np.float64(y)
    return (abs(y-x))
'''
Recibe dos numeros x e y, y calcula el error de aproximar x usando y en float64
'''

def error_relativo(x,y):
    y = np.float64(y)
    return error(x,y)/abs(x)
'''
Recibe dos numeros x e y, y calcula el error relativo de aproximar x usando y en float649
'''

def matricesIguales(A,B):
    A = np.array(A, dtype=np.float64)
    B = np.array(B, dtype=np.float64)
    # Comparo las dimensiones.
    if not(A.shape == B.shape):
        return False
    else:
        for i in range(0, A.shape[0]):
            for j in range(0, A.shape[1]):
                a = A[i][j]
                b = B[i][j]
                if (error(a,b) > error_relativo(a,b) or error(a,b) > error_relativo(b,a)): # Si son muy iguales entonces el error(a, b) simpre es menor que el error relativo de ambos.
                    return False
        return True
'''
Devuelve True si ambas matrices son iguales y False en otro caso.
Considerar que las matrices pueden tener distintas dimensiones, ademas de distintos valores.
'''

# --- Laboratorio 2 ---
def rota(theta):
    return None
"""
Recibe un ángulo theta y retorna una matriz de 2x2 que rota un vector dado en un ángulo theta
"""

def escala(s):
    return None
'''
Recibe una tira de números s y retorna una matriz cuadrada de n x n, donde n es el tamaño de s.
La matriz escala la componente i de un vector de Rn en un factor s[i]
'''

def rota_y_escala(theta, s):
    return None
'''
Recibe un ángulo theta y una tira de numeros s, y retorna una matriz 2x2 que rota el vector en un ángulo theta y luego los escala en un factor s.
'''

def afin(theta, s, b):
    return None
'''
Recibe un angulo theta, una tira de numeros s (en R2) y un vector b en R2.
Retorna una matriz 3x3 que rota el vector en un angulo theta, luego lo escala en un factor de s y por ultimo lo mueve en un factor fijo b. 
'''

def trans_afin(v, theta, s, b):
    return None
'''
Recibe un vector v en R2, un angulo theta, una tira de numeros s en R2, y un vector b en R2.
Retorna el vector w resultante de aplicar la transformacion afin a v.
'''