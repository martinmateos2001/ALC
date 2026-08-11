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

