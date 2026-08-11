#%%
import numpy as np
#%% ejercicio 1
def esCuadrada(A):
    return A.shape[0] == A.shape[1]

#%% test ej1
A = np.array([
    [1, 2],
    [3, 4]])
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
A = np.array([
    [1,2,3],
    [1,2,3],
    [1,2,3]
])
infA = triangInf(A)
print(A)
print(infA)

#%% ejercicio 6 
def traspuesta(A):
    dFilas=len(A)
    dColumnas=len(A[0])
    T = np.zeros(dFilas,dColumnas)
    for f in range(0,dFilas):
        for c in range(0,dColumnas):
            T[c][f] = A[f][c]
    return T

#%% 
