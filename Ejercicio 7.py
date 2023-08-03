#Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.
from random import randint 
lista = [randint(1, 25) for i in range (0,25)]
print (lista)
mayor = 0
menor = 0
i = 1
mayor = max ( lista)
menor = min (lista)
print (lista)
print (mayor)
print (menor)