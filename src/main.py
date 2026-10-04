import random
import string
# Clasificador de números
limite = int(input("¿Hasta qué número quieres evaluar? "))

for i in range(1, limite + 1):
    if i % 2 == 0:
        print(f"El número {i} es PAR")
    else:
        print(f"El número {i} es IMPAR")