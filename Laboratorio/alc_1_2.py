import numpy as np
# --- Laboratorio 1 ---
def error(x,y):
    return 

'''
Recibe dos numeros x e y, y calcula el error de aproximar x usando y en float64
'''

def error_relativo(x,y):
    return 1

'''
Recibe dos numeros x e y, y calcula el error relativo de aproximar x usando y en float649
'''

def matricesIguales(A,B):
    return True

'''
Devuelve True si ambas matrices son iguales y False en otro caso.
Considerar que las matrices pueden tener distintas dimensiones, ademas de distintos valores.
'''
# Test Laboratorio 1
def sonIguales(x,y,atol=1e-08): 
    return np.allclose(error(x,y),0,atol=atol)

assert(not sonIguales(1,1.1))
assert(sonIguales(1,1 + np.finfo('float64').eps))
assert(not sonIguales(1,1 + np.finfo('float32').eps))
assert(not sonIguales(np.float16(1),np.float16(1) + np.finfo('float32').eps))
assert(sonIguales(np.float16(1), np.float16(1) + np.finfo('float16').eps, atol=1e-3))
assert(np.allclose(error_relativo(1,1.1), 0.1))
assert(np.allclose(error_relativo(2,1),0.5))
assert(np.allclose(error_relativo(1,1),0))
assert(np.allclose(error_relativo(1,1),2))
assert(matricesIguales(np.diag([1,1]),np.eye(2)))
assert(matricesIguales(np.linalg.inv(np.array([[1,2],[3,4]]))@np.array([[1,2],[3,4]]),np.eye(2)))
assert(not matricesIguales(np.array([[1,2],[3,4]]).T,np.array([[1,2],[3,4]])))

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
# Tests Laboratorio 2
# Tests para rota
assert (np. allclose ( rota (0) , np. eye (2))) 
assert (np. allclose ( rota (np. pi/2) , np. array ([ [0, -1] , [1, 0]]) )) 
assert (np. allclose ( rota (np. pi) , np. array ([-1, 0] , [0, -1]) )) # Tests para escala
assert (np. allclose ( escala ([2,3]) , np. array ( [ [2 , 0] , [0,3]]))) 
assert (np. allclose ( escala ( [1 , 1 , 1]) , np. eye (3))) 
assert ( np. allclose (escala ([0.5,0.25] ) , np. array ( [ [0.5, 0] , [0,0.25]])) )
# Tests para rota_y_escala 
assert ( np. allclose (rota_y_escala (0 , [2,3]) , np. array ( [ [2 , 0] , [0 ,3]] ) ) ) 
assert (np. allclose ( rota_y_escala (np. pi /2 , [1, 1]) , np. array ([[0, 1] , [1,0]]) )) 
assert (np. allclose (rota_y_escala (np. pi , [2 , 2]) , np. array ([-2,0] , [0,-2])))
# Tests para afin 
assert (np. allclose ( afin (0 , [1,1] , [1,2]), np. array ( [[1 ,0,1] , [0,1,2], [0,0,1]])))
assert (np. allclose ( afin (np. pi /2 , [1 , 1] , [0,0]), np. array ([ [0, 1,0], [1, 0,0], [0, 0,1]])))
assert (np. allclose ( afin (0 , [2,3] , [1,1]), np. array ( [[2,0,1] , [0,3,1], [0,0,1]])))
# Tests para trans_afin 
assert (np. allclose ( trans_afin (np. array ([1 ,0]) , np. pi /2 , [1,1] , [0,0]), np . array ( [0 ,1]) )) 
assert (np. allclose ( trans_afin (np. array ( [1 , 1]) , 0 , [2,3] , [0,0]), np. array ([2,3]) )) 
assert (np. allclose ( trans_afin (np. array ( [1 ,0]) , np. pi /2 , [3 , 2] , [4,5]), np. array ([4,7]) ))