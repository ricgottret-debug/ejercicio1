# Pedir los tres números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Ordenar los números
numeros_ordenados = sorted([num1, num2, num3])

# Mostrar el resultado
print("Números ordenados de menor a mayor:", numeros_ordenados)