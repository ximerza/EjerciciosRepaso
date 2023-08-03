#Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no
palabra = input("Ingrese una cadena de texto: ")
def esPalindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" " , "")
    palabra = palabra.replace("á", "a")
    palabra = palabra.replace("é", "e")
    palabra = palabra.replace("í", "i")
    palabra = palabra.replace("ó", "o")
    palabra = palabra.replace("ú", "u")

    a = 0
    b = len(palabra) - 1
    
    for i in range (0, len(palabra)):
        if palabra[a] == palabra[b]:
            a += 1
            b -= 1
        else:
            return False
        
    return True

print(esPalindromo(palabra))




