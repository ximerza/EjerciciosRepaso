1#Crear un programa que genere una matriz de números y la imprima en pantalla.
import numpy as np
def mostrar (matriz):
    print(matriz.shape)
    print(type(matriz))
    print(matriz)

mostrar(np.array([[21,5,12,1],[14,16,9,2],[34,29,6,11],[20,0,13,18]]))