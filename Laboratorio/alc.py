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
    return np.float64(res)
    
def normaliza(X, p):
    res = []
    for v in X:
        modulo = norma(v, p)
        w = []
        for e in v:
            w.append(e/modulo)
        res.append(w)
    return np.array(res, dtype=np.float64)
'''
Recibe X, una lista de vectores no vacios, y un escalar p. Devuelve una lista donde cada elemento corresponde a normalizar los elementos de X con la norma p.
'''

def normaMatMC(A,q,p,Np):
    A = np.array(A, dtype=np.float64)
    dim = A.shape[1]
    X = np.random.uniform(-1, 1, size=(Np, dim)) # Np arreglos de dimension dim
    X_normalizado = normaliza(X,p)
    X_normalizado_np = np.array(X_normalizado, dtype=np.float64)
    maximo = -1
    x = None
    for v in X_normalizado_np:
        Ax=A@v
        normAx = norma(Ax, q)
        if (normAx > maximo):
            maximo = normAx
            x = v 
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
    if(isinstance(p, (tuple, list))):
        res = [normaExacta(A, p[0]), normaExacta(A,p[1])]
        return res
    return None

def condMC(A, p):
    invA = np.linalg.inv(A)
    res = normaMatMC(A, p, p, 10000)[0] * normaMatMC(invA, p, p, 10000)[0]
    return res
'''
Devuelve el numero de condicion de A usando la norma inducida p.
'''

def condExacto(A, p):
    invA = np.linalg.inv(A)
    res = normaExacta(A,p) * normaExacta(invA, p) 
    return res
'''
Que devuelve el numero de condicion de A a partir de la formula de la ecuacion (1) usando la norma p.
'''

# --- Laboratorio 4 ---
# NO SE PUEDE USAR @
def esTriangularSuperior(A:np.array) -> bool:
    n = A.shape[0]
    for i in range(1,n-1):
        j = 0
        while j < i:
            if(A[i][j] != 0):
                return False
            j+=1
    return True


    
def calculaLU(A):
    if(A is None):
        return None, None, 0
    # dimensiones
    m = A.shape[0]
    n= A.shape[1]
    if( m!=n):
        return None, None, 0
    Ac = A.copy()
    # Identidad para crear L
    L = np.eye(n)
    ops = 0
    j = 0
    while(j < n-1):
        # si el pivote es nulo no puedo operar
        if(Ac[j][j] == 0):
            return None, None, 0
        i=j+1
        
        while(i<n):
            if(Ac[i][j] != 0):
                m = Ac[i][j] / Ac[j][j]
                ops += 1
                L[i][j]= m
                Ac[i][j]=0.0 # asigno para no contar una operacion.
                Ac[i][j+1:] = Ac[i][j+1:] - m * Ac[j][j+1:]
                ops += 2*(n-(j+1)) # resto los que cambian, de la columna j+1 para atras son ceros.
            i+=1
        j+=1
    return L, Ac, ops

def res_tri(L,b,inferior=True):
    n = L.shape[0]
    X = np.zeros(n)
    if(inferior):
        X[0] = b[0]
        for i in range(1, n):
            f = L[i, 0:i]
            s = 0
            for j in range(0, len(f)):
                s += f[j]*X[j]
            X[i] = b[i] - s
        return X
    
    else:
        X[n-1] = b[-1] / L[n-1, n-1]
        i=n-2
        while i > -1:
            f = L[i, i+1:]
            s = 0
            for j in range(i+1, n):
                s += L[i, j] * X[j]
            X[i] = (b[i] - s) / L[i,i]
            i-=1
        return X
    
def traspuesta(A):
    res = np.zeros(A.shape)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            res[i][j] = A[j][i]
    return res


def inversa(A):
    
    LU = calculaLU(A)
    n = A.shape[0]
    L = LU[0]
    U = LU[1]
    for i in range(0, n):
        if(U[i,i] == 0):
            return None
    #LY = I -> UX = Y -> return X
    Y = np.zeros((n,n))
    I = np.eye(n)
    for i in range(0,n):
        y = res_tri(L,I[i], True)
        Y[i] += y
    X = np.zeros((n,n))
    for i in range(0,n):
        x = res_tri(U,Y[i], False)
        X[i] += x 
    return traspuesta(X)

def calculaLDV(A):
    LU = calculaLU(A)
    L = LU[0]
    U = LU[1]
    Uc = np.copy(U)
    D = np.zeros(A.shape)
    n = A.shape[0]
    for i in range(0, n):
        D[i,i] = Uc[i,i]
        for j in range(i, n):
            if(Uc[i,j] != 0):
                Uc[i,j] = Uc[i,j]/D[i,i]
    return L, D, Uc

def esSDP(A, atol=1e-8):
    n=A.shape[0]
    if(n != A.shape[1]):
        return False
    L,D,V= calculaLDV(A)
    for i in range(0,n):
        if(D[i,i] <= 0):
            return False
        for j in range(0, i+1):
            if not (np.isclose(L[i,j], V[j,i], atol)):
                return False
    return True

# --- Laboratorio 5 ---
def prod_vec(x,y):
    ops = 0
    if(len(x) != len(y)):
        return None, ops
    res = 0
    for i in range(0, len(x)):
        if(x[i] != 0 and y[i]!=0):
            res += x[i]*y[i]
            ops += 1
    return res, ops


def QR_con_GS(A, tol=1e-12, retorna_nops=False):
    ops = 0
    n = A.shape[0]
    At = traspuesta(A) # Cada fila es un vector.
    # Cada fila de X es un vector
    nor = norma(At[0], 2)
    x = At[0] / nor
    for i in range(0,n):
        if(abs(x[i]) <= tol):
            x[i] = 0
    Qt = [x]
    R = np.zeros(A.shape) 
    R[0,0] = nor
    for i in range(1, n):
        v = At[i]
        j = i-1
        while j > -1:
            rji= prod_vec(Qt[j],At[i])[0]
            R[j,i] = rji
            v = v - (rji * Qt[j])
            j -= 1
        nor = norma(v, 2)
        R[i,i] = nor
        v_nor = v / nor
        for j in range(0,n):
            if(abs(v_nor[j]) <= tol):
                v_nor[j] = 0
        Qt.append(v_nor) 
    Q = traspuesta(np.array(Qt))
    if(retorna_nops):
        return Q, R, ops 
    return Q, R
"""
A una matriz de n x n 
tol la tolerancia con la que se filtran elementos nulos en R
retorna_nops permite (opcionalmente) retornar el numero de operaciones realizado
retorna matrices Q y R calculadas con Gram Schmidt (y como tercer argumento opcional, el numero de operaciones).
Si la matriz A no es de n x n, debe retornar None
"""

def QR_con_HH(A,tol=1e-12,extras=False):
    return
"""
A una matriz de m x n (m>=n)
tol la tolerancia con la que se filtran elementos nulos en R
retorna matrices Q y R calculadas con reflexiones de Householder
Si la matriz A no cumple m>=n, debe retornar None
extras : bool, opcional
    Si es True, devuelve informacion extra sobre el proceso de factorizacion.
    Por defecto es False. Esto lo hacemos para poder graficar el proceso.
Devuelve la factorizacion QR de A usando reflectores de Householder.
Devuelve: 
    Q, R, extra_info (si extras es True)
    Q, R (si extras es False)
extra_info es un diccionario con la clave:
    'R_matrices': lista de las matrices R en cada paso
    'Q_matrices': lista de las matrices Q en cada paso
    """

def calculaQR(A,metodo='RH',tol=1e-12):
    return
"""
A una matriz de n x n 
tol la tolerancia con la que se filtran elementos nulos en R    
metodo = ['RH','GS'] usa reflectores de Householder (RH) o Gram Schmidt (GS) para realizar la factorizacion
retorna matrices Q y R calculadas con Gram Schmidt (y como tercer argumento opcional, el numero de operaciones)
Si el metodo no esta entre las opciones, retorna None
"""
    