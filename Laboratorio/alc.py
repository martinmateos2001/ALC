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
@ para multiplicar.
np.isclose().
'''

# --- Laboratorio 1 ---

def abs(x):
    if x>=0:
        return np.float64(x)
    else:
        return np.float64(-x)
    
def error(x,y):
    x = np.float64(x)
    y = np.float64(y)
    return (abs(y-x))
'''
Recibe dos numeros x e y, y calcula el error de aproximar x usando y en float64
'''

def error_relativo(x,y):
    if not(x == 0):
        return error(x,y)/abs(x)
    return error(x,y)
'''
Recibe dos numeros x e y, y calcula el error relativo de aproximar x usando y en float64
'''

def matricesIguales(A,B):
    A = np.array(A, dtype=np.float64)
    B = np.array(B, dtype=np.float64)
    tolerancia = 1e-07  # Necesito chequear por cifras, ya que las ultimas pueden tener error de redondeo.
    # Comparo las dimensiones.
    if not(A.shape == B.shape):
        return False
    else:
        for i in range(0, A.shape[0]):
            for j in range(0, A.shape[1]):
                a = A[i][j]
                b = B[i][j]
                if (error(a,b) > tolerancia):
                    return False
        return True
'''
Devuelve True si ambas matrices son iguales y False en otro caso.
Considerar que las matrices pueden tener distintas dimensiones, ademas de distintos valores.
'''

# --- Laboratorio 2 ---
def rota(theta):
    res = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    return res
"""
Recibe un ángulo theta y retorna una matriz de 2x2 que rota un vector dado en un ángulo theta
"""

def escala(s):
    res = np.zeros((len(s), len(s)))
    for i in range(0,len(s)):
        res[i][i] = s[i]
    return res
'''
Recibe una tira de números s y retorna una matriz cuadrada de n x n, donde n es el tamaño de s.
La matriz escala la componente i de un vector de Rn en un factor s[i]
'''

def filaXcolumna(fila, columna, A, B):
    res = 0
    for k in range(A.shape[1]):
        res = res + A[fila][k]*B[k][columna]
    return res

def producto(A, B):
    if not(A.shape[1] == B.shape[0]):
        return None
    else:
        res = np.zeros((A.shape[0], B.shape[1]))
        for i in range(0, A.shape[0]):
            for j in range(0, B.shape[1]):  
                res[i][j] = filaXcolumna(i, j, A, B)
        return res


def rota_y_escala(theta, s):
    R = rota(theta)
    S = escala(s)
    res = producto(S, R)
    return res
'''
Recibe un ángulo theta y una tira de numeros s, y retorna una matriz 2x2 que rota el vector en un ángulo theta y luego los escala en un factor s.
'''
def suma(A,B):
    if not(A.shape == B.shape):
        return None
    res = np.zeros(A.shape)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            res[i][j] = A[i][j] + B[i][j]
    return res

def afin(theta, s, b):
    res = np.zeros((3,3))
    sr = rota_y_escala(theta, s)
    for i in range(2):
        for j in range(2):
            res[i][j] = sr[i][j]
        res[i][2] = b[i]
    res[2][2]= 1    
    return res
'''
Recibe un angulo theta, una tira de numeros s (en R2) y un vector b en R2.
Retorna una matriz 3x3 que rota el vector en un angulo theta, luego lo escala en un factor de s y por ultimo lo mueve en un factor fijo b. 
'''

def trans_afin(v, theta, s, b):
    tl = afin(theta, s, b)
    x = tl[0][0]*v[0] + tl[0][1]*v[1] + tl[0][2]
    y = tl[1][0]*v[0] + tl[1][1]*v[1] + tl[1][2]
    res = np.array([x, y])
    return res
'''
Recibe un vector v en R2, un angulo theta, una tira de numeros s en R2, y un vector b en R2.
Retorna el vector w resultante de aplicar la transformacion afin a v.
'''

# --- Laboratorio 3 ---
def norma(x,p):
    res = 0
    if(isinstance(p, (int,float))):
        if (p == 1):
            for e in x:
                res = res + abs(e)
        if(p > 1):
            suma = 0
            for e in x:
                suma = suma + abs(e)**p
            res = suma**(1/p)
    if(p =='inf' and isinstance(p, str)):
        ls = [abs(x[i]) for i in range(0, len(x))]
        res = max(ls)
    return res
    
def normaliza(X, p):
    res = []
    for v in X:
        modulo = norma(v, p)
        w = []
        for e in v:
            w.append(e/modulo)
        res.append(w)
    return res
'''
Recibe X, una lista de vectores no vacios, y un escalar p. Devuelve una lista donde cada elemento corresponde a normalizar los elementos de X con la norma p.
'''

def normaMatMC(A,q,p,Np):
    dim = A.shape[1]
    X = np.random.uniform(-1, 1, size=(Np, dim)) # Np arreglos de dimension dim
    X_normalizdo = normaliza(X,p)
    maximo = -1
    x = None
    for i in range(Np):
        Ax=A@X_normalizdo[i]
        normAx = norma(Ax, q)
        if (normAx > maximo):
            maximo = normAx
            x = X_normalizdo[i] 
    return maximo, x
'''
Devuelve la norma ||A||\_{q,p} y el vector x en el cual se alcanza el maximo.
'''

def normaExacta(A, p=[1,'inf']):
    filas = A.shape[0]
    cols = A.shape[1]
    res = 0

    # Calculo la norma 1
    if(p == 1 and isinstance(p, (int, float))):
        for i in range(cols):
            s = 0
            for f in A:
                s = s + abs(f[i])
            if(s > res):
                res = s
        return res

    # calculo la norma infinito
    if(p=='inf' and isinstance(p, str)):
        for j in range(filas):
            s = 0
            for e in A[j]:
                s = s + abs(e)
            if(s > res):
                res = s
        return res

    return None
def condMC(A, p):
    invA = np.linalg.inv(A)
    res = normaMatMC(A, p, p, 10000)[0] * normaMatMC(invA, p, p, 10000)[0]
    return res
'''
Devuelve el numero de condicion de A usando la norma inducida p.
'''
