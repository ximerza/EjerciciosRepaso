#Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y division.
numero1 = float(input("Ingrese el segundo numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
if numero2 == 0:
    print("La suma de los numeros es" ,suma, "\n la resta es" ,resta, "\n la multiplicacion es" ,multiplicacion, "\n division: no se puede dividir entre 0" )
else:
    division = numero1 / numero2
    print("La suma de los numeros es" ,suma, "\n la resta es" ,resta, "\n la multiplicacion es" ,multiplicacion, "\n la division es:",division, )
