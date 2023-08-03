#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla
from random import randint
lista = [randint(1,15) for i in range (1,15)]
print(lista)
