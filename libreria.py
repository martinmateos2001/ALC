#%%
import numpy as np

# Matrices de prueba 
A = np.array([
    [1,2,3],
    [1,2,3],
    [1,2,3]
])

A_simetrica = np.array([
    [1,2,3],
    [2,5,2],
    [3,2,1]
])

#%% ejercicio 1
def esCuadrada(A):
    return A.shape[0] == A.shape[1]

#%% test ej1

B= np.array([
    [1,2,0], 
    [1,2,3]])
C= np.array([
    [1,2],
    [1,2],
    [1,2]])

matrices = [A, B, C]
sol = [True, False, False]
res = []
for m in matrices:
    res.append(esCuadrada(m))
print(sol == res)

#%% ejercicio 2
def triangSup(A):
    if not esCuadrada(A):
        return "La matriz no es cuadrada"
    dim = len(A)
    res = np.zeros((dim, dim))
    for i in range(0, dim):
        for j in range(0,dim):
            if i>j:
                res[i][j]=0
            else:
                if i==j:
                    res[i][i]=1
                else:
                    res[i][j] = A[i][j]
    return res

#%% test ej2
A = np.array([
    [1,2,3],
    [1,2,3],
    [1,2,3]
])
supA = triangSup(A)
print(A)
print(supA)

#%% Ejercicio 3
'''
Crear una matriz cuadrada.
Si con i recorro las filas y con j las columnas para todo elemento e_ij con i<j tengo que e_ij = 0.
e_ii = 1
Para el otro caso simplemento pongo el elemento a_ij perteneciente a A.
'''

def triangInf(A):
    if not esCuadrada(A):
        return "La matriz no es cuadrada"
    dim = len(A)
    res = np.zeros((dim, dim))
    for i in range(0, dim):
        for j in range(0,dim):
            if i<j:
                res[i][j]=0
            else:
                if i==j:
                    res[i][i]=1
                else:
                    res[i][j] = A[i][j]
    return res
#%% test ej3
infA = triangInf(A)
print(A)
print(infA)

#%% ejercicio 4
def diagonal(A):
    if not esCuadrada(A):
        return 'La matriz no es cuadrada'
    res = np.zeros(A.shape)
    for i in range(0, len(A)):
        res[i][i]= A[i][i]
    return res

#%% test ej 4
print(A)
dia = diagonal(A)
print(dia)
for i in range(0,len(A)):
    if not dia[i][i]== A[i][i]:
        print(res)
print(True)

#%% ejercicio 5
def traza(A):
    res = 0
    for i in range(0, len(A)):
        res = res + A[i][i]
    return res

# test
print(6 == traza(A))
#%% ejercicio 6 
def traspuesta(A):
    res = np.zeros(A.shape)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            res[i][j] = A[j][i]
    return res

print(traspuesta(A))
#%% ejercicio 7
def esSimetrica(A):
    return A==traspuesta(A)

#test
print(esSimetrica(A_simetrica))
#%% ejercicio 8
# A cada fila le hago producto punto con el vector de entrada y lo agrego. Uso el metodo de numpy dot.
# se indica que los vectores que componen la matriz con el vector a multiplicar tienen la misma dimensión.
def calcularAx(A, x):
    cantVectores = A.shape[0]
    dimVectores = A.shape[1]
    res = np.zeros((dimVectores,1))
    for i in range(0, cantVectores):
        res[i] = res[i] + np.dot(A[i], x)
    return res

# test
A = np.array([
    [1,2,3],
    [1,2,3],
    [1,2,3]
])
x = np.array([1,1,1])
v = np.array([6,6,6])
print(v == calcularAx(A,x))

# %% ejercicio 9
# ojo, la Fila 1 es la posicion 0 y así sucesivamente.
def intercambiarFilas(A, i, j):
    vectorI = np.array(A[i-1])
    vectorJ= np.array(A[j-1])

    A[i-1] = vectorJ
    A[j-1] = vectorI

# test
B = np.array([
    [1,1],
    [2,2]
])

intercambiarFilas(B,1,2)
print(B)
# %% ejercicio 10
def sumar_fila_numero(A, i, j, s):
    A[i-1] = A[i-1] + s * A[j-1]

#test
A = np.array([
    [1,2],
    [3,4]
])

sumar_fila_numero(A, 1, 2, 3)
print(A)

# %% 11
def esDiagonalmenteDominante(A):
    for i in range(A.shape[0]):
        s = 0
        for v in A[i]:
            if not v==A[i][i]:
                s = s + abs(v)
        if abs(A[i][i]) <= s:
            return False
    return True

# test
A = np.array([
    [5,-2],
    [-1,3]
])
print(esDiagonalmenteDominante(A) == True)

A = np.array([
    [1,3],
    [-2,4]
])
print(esDiagonalmenteDominante(A) == False)

A = np.array([
    [1,3],
    [-2,-4]
])
print(esDiagonalmenteDominante(A) == False)

A = np.array([
    [2,-1,1],
    [-2,-4,1],
    [1,1,3]
])
print(esDiagonalmenteDominante(A) == False)

# %% ejercicio 12

'''
v = [1,0,0]

res=[
[1,0,0],
[0,1,0],
[0,0,1]
]
'''
def matrizCirculante(v):
    n = len(v)
    res = np.zeros((n,n))

    for i in range(0, n):
        for j in range(0, n):
            p = (j+i)%n # en la posicion j+i de res va el valor del vector en j pero como se pasa le puse el resto.
            res[i][p] = v[j]

    return res

# test
v = np.array([1,0,0])
print(matrizCirculante(v))

# %%
