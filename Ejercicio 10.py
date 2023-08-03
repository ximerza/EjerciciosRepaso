#Escribir una función que calcule el factorial de un número dado
print ("Ingrese un número")
n = int(input())
fact = 1
for i in range (1, n+1):
    fact*=i
print("El valor factorial del número " ,n, "es:" ,fact,)