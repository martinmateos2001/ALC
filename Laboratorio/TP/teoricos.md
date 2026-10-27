# Ejercicio 1
#### _Respuesta inciso a_.
##### ¿Cual es el rango de $Q$ para que la solución sea no nula única a menos de un factor de escala?
Para obtener una solución no nula a un factor de escala la dimensión de $Q$ debe ser exactamente igual 1, por el teorema de la dimensión esto significa que el rango de $Q$ es igual a 11.
##### ¿Cuántos puntos, como mínimo, aseguran la solución y qué condición deben cumplir?
Teniendo en cuenta que cada punto aporta dos ecuaciones lineales independientes y el número de ecuaciones debe ser igual 12 por el teorema de la dimensión donde sólo una es combinación lineal de las otras 11, el número mínimo de puntos que aseguran la solución es 6.
La condición que deben cumplir es que no pueden pertenecer a un mismo plano, pues entonces habría dependencia lineal, lo cual disminuiría el rango de la matriz y en consucuencia aumentando la dimensión de su núcleo obteniendo así infinitas soluciones.

#### _Respuesta inciso b_.
En teoría deberíamos hallar la solucion del sistema $Qm = 0$ donde $rg(Q) = 11$. Pero en la práctica, generalmente los errores podrían provocar que $rg(Q) = 12$, obteniendo la solución trivial y la matriz $M$ resultaría nula. Para evitar obtener la solución trivial se busca resolver el problema de mínimos cuadrados homogéneos con restricción de norma.
Toda matriz rectangular posee descomposición en valores singulares por lo que $Q = U \Sigma V^t$. Como $U$ es unitaria se tiene que:
$$
\begin{aligned}
Qm &= U \Sigma V^t m \\
&=  U (\Sigma V^t m) \\
&= \Sigma V^t m
\end{aligned}
$$
Entonces $||Qm||_2 ^2 = ||\Sigma V^t m||_2 ^2$.
Como $V$ es unitaria, tomando como vectores sus columnas, estos forman una base ortonormal de $\mathbb{R}^{12}$ de modo que $m = \sum_{i=1}^{12}\alpha_i v_i$ con $\sum_{i=1}^{12}\alpha_i^2 = 1$. Sea $A = (\alpha_1, \space \alpha_2, \space ... \space, \alpha_{12}) \in \mathbb{R}^{12}$, de forma matricial $m = VA$, luego
$$
\begin{aligned}
\Sigma V^t m &= \Sigma V^t VA \\
&= \Sigma (V^t V)A \\
&= \Sigma A
\end{aligned}
$$
De esta manera,
$$
\begin{aligned}
||Qm||_2 ^2 &= ||\Sigma A||_2 ^2 \\
&= \sum_{i=1}^{12} \sigma_i^2 \alpha_i^2 \\
&\geq \sigma_{12}^2 \sum_{i=1}^{12} \alpha_i^2 = \sigma_{12}^2
\end{aligned}
$$
El valor mínimo de la norma es $\sigma_{12}^{2}$. Este mínimo se alcanza cuando $A=\pm(0, 0, ... , 1)$ y por lo tanto $m = \pm v_{12}$.