# Definir el lenguaje finito
L = {"a", "b", "ab", "ba", "aa"}

# Pedir palabra al usuario
palabra = input("Ingresa una palabra: ")

# Verificar si pertenece
if palabra in L:
    print("La palabra pertenece a L.")
else:
    print("La palabra NO pertenece a L.")
