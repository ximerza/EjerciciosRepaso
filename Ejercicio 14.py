#Escribir una función que calcule la media aritmética de una lista de números.
lista = []
num = print("Cuantos numeros quieres ingresar")
n = int(input())
i = 0
while i < n:
    print("valor numer:" ,i+1)
    v = float(input())
    lista.append(v)
    i+=1
p = sum(lista) / len(lista)
print("La medida aritmerica es: " ,p,)

