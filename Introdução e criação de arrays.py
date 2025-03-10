#Numerical Python

import numpy as np
#Array unidimensional com Nump
numeros = np.array([2,8,6,9,0,2,4,6,7])

print(numeros)
print(numeros.dtype)

numeros[0] = 3
print(numeros[0])


#Array bidimensional com Numpy

M= np.array([[2,4,6],[1,3,5],[7,9,5]])

print(M)

#print(M[2,1])

#M[0,1] = 7
#print(M[0,1])

#Visualizar uma coluna inteira

print('Primeira Coluna:', M[:,0])
print('Segunda Coluna:', M[:,1])
print('Terceira coluna:', M[:,2])

#Visualizar uma linha inteira

print('Segunda Linha', M[1,:])

#Numero de dimensões de um array:

print(numeros.ndim)
print(M.ndim)

#Tamanho do array
print(numeros.shape)
print(M.shape)

#Numero de Elementos de um Array
print(numeros.size)
print(M.size)