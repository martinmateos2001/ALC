#%% Librerias
import numpy as np
from alc_1_2 import *

#%% Test Laboratorio 1
#Observo como se ven las cosas.
def diferenciasFloat64(x,y):
    x_64 = np.float64(x)
    y_64 = np.float64(y)
    print(f'x={x}\nfloat64(x) = {x_64}\ny={y}\nfloat64(y)={y_64}\nabs(y-x)={abs(y-x)}\nerror(x,y)={error(x,y)}')
    print(f'Error Relativo({x},{y})= {error_relativo(x,y)} = {0.1/1.1}')
diferenciasFloat64(1, 1.1)

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
assert(np.allclose(error_relativo(1,-1),2))
assert(matricesIguales(np.diag([1,1]),np.eye(2)))
assert(matricesIguales(np.linalg.inv(np.array([[1,2],[3,4]]))@np.array([[1,2],[3,4]]),np.eye(2)))
assert(not matricesIguales(np.array([[1,2],[3,4]]).T,np.array([[1,2],[3,4]])))

#%% Tests Laboratorio 2
# Tests para rota
assert (np.allclose(rota(0) , np.eye(2))) 
assert (np.allclose(rota(np.pi/2), np.array([[0, -1], [1, 0]]))) 
assert (np.allclose(rota(np.pi), np.array([-1, 0], [0, -1]))) # Tests para escala
assert (np.allclose(escala([2,3]), np.array([[2, 0], [0,3]]))) 
assert (np.allclose(escala([1, 1, 1]), np.eye(3))) 
assert ( np.allclose(escala([0.5,0.25] ), np.array([[0.5, 0], [0,0.25]])) )
# Tests para rota_y_escala 
assert(np.allclose(rota_y_escala (0, [2,3]), np. array([[2, 0], [0, 3]]))) 
assert (np.allclose(rota_y_escala(np.pi /2, [1, 1]), np.array([[0, 1], [1,0]]))) 
assert (np.allclose(rota_y_escala(np.pi, [2, 2]), np.array([-2,0], [0,-2])))
# Tests para afin 
assert (np.allclose(afin(0, [1,1], [1,2]), np.array([[1, 0, 1], [0,1,2], [0,0,1]])))
assert (np.allclose(afin(np.pi/2 , [1, 1] , [0,0]), np.array([[0, 1,0], [1, 0,0], [0, 0,1]])))
assert (np.allclose(afin(0, [2,3], [1,1]), np.array ([[2,0,1] , [0,3,1], [0,0,1]])))
# Tests para trans_afin 
assert (np.allclose(trans_afin(np.array([1 ,0]), np.pi/2, [1,1], [0,0]), np.array([0 ,1]))) 
assert (np.allclose(trans_afin(np.array([1 , 1]) , 0 , [2,3] , [0,0]), np. array ([2,3]))) 
assert (np.allclose(trans_afin(np.array([1 ,0]), np.pi/2, [3, 2], [4,5]), np.array([4,7]) ))
# %%
