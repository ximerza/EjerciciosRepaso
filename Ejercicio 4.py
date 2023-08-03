#Escribir un programa que determine si un número dado es par o impar
a = int(input("ingresa un numero: "))
if a % 2 == 0:
    print("El numero",a,"es par")
else:
    print("El numero",a,"es inpar")