#Crear una función que convierta grados Fahrenheit a grados Celsius
def fahrenheit(f):
    c = (f-32) * 5/9
    return c
f = float(input("ingresar los grados fahrenheit: " ))
print (f"La conversion a grados celsius es: {fahrenheit(f)}")
