#Crear un programa que genere una lista de números pares entre 1 y 100.
x = 1
while x <=100:
    if x % 2 == 0:
        print("El número" ,x, "es par")
    x = x+1